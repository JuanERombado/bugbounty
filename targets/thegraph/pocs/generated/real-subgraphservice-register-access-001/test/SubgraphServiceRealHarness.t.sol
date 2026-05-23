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

    function setStaking(address staking_) external {
        staking = staking_;
    }

    function getContractProxy(bytes32 id) external view returns (address) {
        if (id == keccak256(bytes("Staking"))) return staking;
        return dummy;
    }
}

contract MockHorizonStaking {
    mapping(address => bool) internal authorized;
    mapping(address => IHorizonStakingTypes.Provision) internal provisions;

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
}

contract MockDisputeManager {
    function getDisputePeriod() external pure returns (uint64) {
        return 1;
    }

    function getFishermanRewardCut() external pure returns (uint32) {
        return 0;
    }
}

contract SubgraphServiceRealHarnessTest is Test {
    address internal owner = address(0xA11CE);
    address internal indexer = address(0x1D3A);
    address internal attacker = address(0xB0B);
    address internal paymentsDestination = address(0xFEE);
    MockHorizonStaking internal staking;
    SubgraphService internal service;

    function setUp() public {
        staking = new MockHorizonStaking();
        MockDisputeManager disputeManager = new MockDisputeManager();
        MockGraphController controller = new MockGraphController();
        controller.setStaking(address(staking));

        SubgraphService implementation = new SubgraphService(
            address(controller),
            address(disputeManager),
            address(0x1003),
            address(0x1004),
            address(0x1005)
        );
        bytes memory initData = abi.encodeCall(SubgraphService.initialize, (owner, 1 ether, 10, 1));
        service = SubgraphService(address(new ERC1967Proxy(address(implementation), initData)));
    }

    // Hypothesis: REGISTER-ACCESS-001
    // Local-only invariant: register should require an authorized, valid provision and update only indexer metadata.
    function test_REGISTER_ACCESS_001_authorizedIndexerCanRegisterAndSetPaymentDestination() public {
        staking.setAuthorized(indexer, true);
        staking.setProvision(indexer, 2 ether);

        bytes memory data = abi.encode("https://indexer.local", "9q8yy", paymentsDestination);
        vm.prank(indexer);
        service.register(indexer, data);

        (string memory url, string memory geoHash) = service.indexers(indexer);
        assertEq(url, "https://indexer.local");
        assertEq(geoHash, "9q8yy");
        assertEq(service.paymentsDestination(indexer), paymentsDestination);
    }

    function test_REGISTER_ACCESS_001_unauthorizedCallerCannotRegisterIndexer() public {
        staking.setAuthorized(indexer, true);
        staking.setProvision(indexer, 2 ether);

        bytes memory data = abi.encode("https://indexer.local", "9q8yy", paymentsDestination);
        vm.prank(attacker);
        vm.expectRevert();
        service.register(indexer, data);
    }

    function test_REGISTER_ACCESS_001_missingProvisionCannotRegister() public {
        staking.setAuthorized(indexer, true);

        bytes memory data = abi.encode("https://indexer.local", "9q8yy", paymentsDestination);
        vm.prank(indexer);
        vm.expectRevert();
        service.register(indexer, data);
    }
}
