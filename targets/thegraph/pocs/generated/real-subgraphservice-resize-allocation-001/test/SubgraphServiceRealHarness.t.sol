// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {Test} from "forge-std/Test.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {IHorizonStaking} from "@graphprotocol/interfaces/contracts/horizon/IHorizonStaking.sol";
import {IHorizonStakingTypes} from "@graphprotocol/interfaces/contracts/horizon/internal/IHorizonStakingTypes.sol";
import {SubgraphService} from "packages/subgraph-service/contracts/SubgraphService.sol";

contract MockGraphController {
    address internal dummy = address(0xCAFE);
    address internal staking;
    address internal epochManager;
    address internal rewardsManager;

    function setStaking(address staking_) external { staking = staking_; }
    function setEpochManager(address epochManager_) external { epochManager = epochManager_; }
    function setRewardsManager(address rewardsManager_) external { rewardsManager = rewardsManager_; }

    function getContractProxy(bytes32 id) external view returns (address) {
        if (id == keccak256(bytes("Staking"))) return staking;
        if (id == keccak256(bytes("EpochManager"))) return epochManager;
        if (id == keccak256(bytes("RewardsManager"))) return rewardsManager;
        return dummy;
    }
}

contract MockHorizonStaking {
    mapping(address => bool) internal authorized;
    mapping(address => IHorizonStakingTypes.Provision) internal provisions;
    mapping(address => bool) internal legacyAllocations;

    function setAuthorized(address serviceProvider, bool allowed) external {
        authorized[serviceProvider] = allowed;
    }

    function setProvision(address serviceProvider, uint256 tokens) external {
        provisions[serviceProvider] = IHorizonStakingTypes.Provision({
            tokens: tokens,
            tokensThawing: 0,
            sharesThawing: 0,
            maxVerifierCut: 0,
            thawingPeriod: 1,
            createdAt: 1,
            maxVerifierCutPending: 0,
            thawingPeriodPending: 1,
            lastParametersStagedAt: 0,
            thawingNonce: 0
        });
    }

    function isAuthorized(address serviceProvider, address, address operator) external view returns (bool) {
        return authorized[serviceProvider] && operator == serviceProvider;
    }

    function getProvision(address serviceProvider, address) external view returns (IHorizonStaking.Provision memory) {
        return provisions[serviceProvider];
    }

    function getTokensAvailable(address serviceProvider, address, uint32) external view returns (uint256) {
        IHorizonStakingTypes.Provision memory provision = provisions[serviceProvider];
        return provision.tokens - provision.tokensThawing;
    }

    function isAllocation(address allocationId) external view returns (bool) {
        return legacyAllocations[allocationId];
    }
}

contract MockDisputeManager {
    function getDisputePeriod() external pure returns (uint64) { return 1; }
    function getFishermanRewardCut() external pure returns (uint32) { return 0; }
}

contract MockEpochManager {
    function currentEpoch() external pure returns (uint256) { return 7; }
}

contract MockRewardsManager {
    function onSubgraphAllocationUpdate(bytes32) external pure returns (uint256) { return 0; }
    function calcRewards(uint256 tokens, uint256 accRewardsPerAllocatedToken) external pure returns (uint256) {
        return tokens * accRewardsPerAllocatedToken;
    }
    function isDenied(bytes32) external pure returns (bool) { return false; }
    function takeRewards(address) external pure returns (uint256) { return 0; }
    function reclaimRewards(bytes32, address) external pure returns (uint256) { return 0; }
}

contract SubgraphServiceRealHarnessTest is Test {
    uint256 internal allocationPrivateKey = 0xA110CA710;
    address internal owner = address(0xA11CE);
    address internal indexer = address(0x1D3A);
    address internal attacker = address(0xB0B);
    address internal allocationId;
    bytes32 internal subgraphDeploymentId = keccak256("subgraph-deployment");
    MockHorizonStaking internal staking;
    SubgraphService internal service;

    function setUp() public {
        allocationId = vm.addr(allocationPrivateKey);
        staking = new MockHorizonStaking();
        MockDisputeManager disputeManager = new MockDisputeManager();
        MockEpochManager epochManager = new MockEpochManager();
        MockRewardsManager rewardsManager = new MockRewardsManager();
        MockGraphController controller = new MockGraphController();
        controller.setStaking(address(staking));
        controller.setEpochManager(address(epochManager));
        controller.setRewardsManager(address(rewardsManager));

        SubgraphService implementation = new SubgraphService(
            address(controller),
            address(disputeManager),
            address(0x1003),
            address(0x1004),
            address(0x1005)
        );
        bytes memory initData = abi.encodeCall(SubgraphService.initialize, (owner, 1 ether, 10, 1));
        service = SubgraphService(address(new ERC1967Proxy(address(implementation), initData)));

        staking.setAuthorized(indexer, true);
        staking.setProvision(indexer, 10 ether);
        vm.prank(indexer);
        service.register(indexer, abi.encode("https://indexer.local", "9q8yy", address(0)));
        _startAllocation(2 ether);
    }

    // Hypothesis: RESIZE-ALLOCATION-001
    // Local-only invariant: resizing should keep allocation, subgraph, and locked provision accounting synchronized.
    function test_RESIZE_ALLOCATION_001_resizeUpAndDownKeepsAccountingInSync() public {
        _assertAllocationAccounting(2 ether);

        vm.prank(indexer);
        service.resizeAllocation(indexer, allocationId, 5 ether);
        _assertAllocationAccounting(5 ether);

        vm.prank(indexer);
        service.resizeAllocation(indexer, allocationId, 1 ether);
        _assertAllocationAccounting(1 ether);
    }

    function test_RESIZE_ALLOCATION_001_sameSizeResizeReverts() public {
        vm.prank(indexer);
        vm.expectRevert();
        service.resizeAllocation(indexer, allocationId, 2 ether);
    }

    function test_RESIZE_ALLOCATION_001_unauthorizedResizeReverts() public {
        vm.prank(attacker);
        vm.expectRevert();
        service.resizeAllocation(indexer, allocationId, 5 ether);
    }

    function _startAllocation(uint256 tokens) internal {
        bytes memory data = abi.encode(subgraphDeploymentId, tokens, allocationId, _allocationProof(indexer, allocationId));
        vm.prank(indexer);
        service.startService(indexer, data);
    }

    function _assertAllocationAccounting(uint256 expectedTokens) internal view {
        (bool isOpen, address actualIndexer, bytes32 actualSubgraph, uint256 actualTokens, , ) =
            service.getAllocationData(allocationId);
        assertTrue(isOpen);
        assertEq(actualIndexer, indexer);
        assertEq(actualSubgraph, subgraphDeploymentId);
        assertEq(actualTokens, expectedTokens);
        assertEq(service.getSubgraphAllocatedTokens(subgraphDeploymentId), expectedTokens);
        assertEq(service.allocationProvisionTracker(indexer), expectedTokens);
    }

    function _allocationProof(address indexer_, address allocationId_) internal view returns (bytes memory) {
        bytes32 digest = service.encodeAllocationProof(indexer_, allocationId_);
        (uint8 v, bytes32 r, bytes32 s) = vm.sign(allocationPrivateKey, digest);
        return abi.encodePacked(r, s, v);
    }
}
