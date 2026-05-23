"""Generate Foundry harnesses that import real target contracts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def generate_real_foundry_harness(
    project_dir: Path,
    *,
    workspace: Path,
    target: str,
    repo_root: Path,
    contract_path: str,
    contract_name: str,
    hypothesis_id: str,
    run_id: str,
) -> list[Path]:
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "test").mkdir(exist_ok=True)

    repo_root = repo_root.resolve()
    contract_import = _normalize_import(contract_path)
    metadata = {
        "run_id": run_id,
        "target": target,
        "repo_root": str(repo_root),
        "contract_path": contract_path,
        "contract_name": contract_name,
        "hypothesis_id": hypothesis_id,
        "status": "real_harness_generated",
        "report_ready": False,
    }

    written = [
        _write(project_dir / "foundry.toml", _foundry_toml(workspace, repo_root, contract_path)),
        _write(project_dir / "test" / f"{contract_name}RealHarness.t.sol", _test_source(contract_import, contract_name, hypothesis_id)),
        _write(project_dir / "README.md", _readme(metadata)),
        _write(project_dir / "harness.json", json.dumps(metadata, indent=2) + "\n"),
    ]
    return written


def _write(path: Path, content: str) -> Path:
    path.write_text(content, encoding="utf-8")
    return path


def _normalize_import(contract_path: str) -> str:
    return contract_path.replace("\\", "/").lstrip("/")


def _foundry_toml(workspace: Path, repo_root: Path, contract_path: str) -> str:
    workspace_s = workspace.resolve().as_posix()
    repo_s = repo_root.resolve().as_posix()
    package_root = _package_root(repo_root, contract_path)
    package_s = package_root.resolve().as_posix()
    return f"""[profile.default]
src = "src"
test = "test"
out = "out"
libs = ["lib", "{package_s}/node_modules", "{repo_s}/node_modules", "{repo_s}/lib"]
solc_version = "0.8.27"
optimizer = true
optimizer_runs = 200
remappings = [
  "@graphprotocol/={repo_s}/packages/",
  "@openzeppelin/={package_s}/node_modules/@openzeppelin/",
  "packages/={repo_s}/packages/",
  "forge-std/={package_s}/node_modules/forge-std/src/",
  "external/={workspace_s}/external/"
]

[fmt]
line_length = 120
tab_width = 4
bracket_spacing = true
"""


def _package_root(repo_root: Path, contract_path: str) -> Path:
    parts = Path(contract_path).parts
    if len(parts) >= 2 and parts[0] == "packages":
        candidate = repo_root / parts[0] / parts[1]
        if candidate.exists():
            return candidate
    return repo_root


def _test_source(contract_import: str, contract_name: str, hypothesis_id: str) -> str:
    if contract_name == "SubgraphService" and _safe_identifier(hypothesis_id) == "OWNER_ACCESS_001":
        return _subgraph_service_owner_access_source(contract_import, hypothesis_id)
    if contract_name == "SubgraphService" and _safe_identifier(hypothesis_id) == "REGISTER_ACCESS_001":
        return _subgraph_service_register_access_source(contract_import, hypothesis_id)
    if contract_name == "SubgraphService" and _safe_identifier(hypothesis_id) == "STARTSERVICE_ALLOCATION_001":
        return _subgraph_service_start_service_allocation_source(contract_import, hypothesis_id)
    if contract_name == "SubgraphService" and _safe_identifier(hypothesis_id) == "RESIZE_ALLOCATION_001":
        return _subgraph_service_resize_allocation_source(contract_import, hypothesis_id)
    if contract_name == "SubgraphService" and _safe_identifier(hypothesis_id) == "STOPSERVICE_ACCOUNTING_001":
        return _subgraph_service_stop_service_accounting_source(contract_import, hypothesis_id)

    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {{{contract_name}}} from "{contract_import}";

contract {contract_name}RealHarnessTest {{
    {contract_name} internal target;

    // Hypothesis: {hypothesis_id}
    // This file only proves whether a real-contract harness can compile.
    // Replace this constructor path with mocks/setup before interpreting runtime failures.
    function test_{_safe_identifier(hypothesis_id)}_realHarnessCompiles() public view {{
        target;
    }}
}}
"""


def _subgraph_service_owner_access_source(contract_import: str, hypothesis_id: str) -> str:
    safe_id = _safe_identifier(hypothesis_id)
    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {{Test}} from "forge-std/Test.sol";
import {{ERC1967Proxy}} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {{SubgraphService}} from "{contract_import}";

contract MockGraphController {{
    address internal dummy = address(0xCAFE);

    function getContractProxy(bytes32) external view returns (address) {{
        return dummy;
    }}
}}

contract SubgraphServiceRealHarnessTest is Test {{
    address internal owner = address(0xA11CE);
    address internal attacker = address(0xB0B);
    SubgraphService internal service;

    function setUp() public {{
        MockGraphController controller = new MockGraphController();
        SubgraphService implementation = new SubgraphService(
            address(controller),
            address(0x1002),
            address(0x1003),
            address(0x1004),
            address(0x1005)
        );
        bytes memory initData = abi.encodeCall(SubgraphService.initialize, (owner, 1 ether, 10, 1));
        service = SubgraphService(address(new ERC1967Proxy(address(implementation), initData)));
    }}

    // Hypothesis: {hypothesis_id}
    // Local-only invariant: owner-only economic configuration setters must reject arbitrary callers.
    function test_{safe_id}_nonOwnerCannotChangeEconomicSettings() public {{
        vm.startPrank(attacker);
        vm.expectRevert();
        service.setStakeToFeesRatio(2);
        vm.expectRevert();
        service.setCurationCut(1);
        vm.expectRevert();
        service.setIndexingFeesCut(1);
        vm.expectRevert();
        service.setDelegationRatio(11);
        vm.stopPrank();
    }}

    function test_{safe_id}_ownerCanChangeEconomicSettings() public {{
        vm.startPrank(owner);
        service.setStakeToFeesRatio(2);
        service.setCurationCut(1);
        service.setIndexingFeesCut(1);
        service.setDelegationRatio(11);
        vm.stopPrank();

        assertEq(service.stakeToFeesRatio(), 2);
        assertEq(service.curationFeesCut(), 1);
        assertEq(service.indexingFeesCut(), 1);
        assertEq(service.getDelegationRatio(), 11);
    }}
}}
"""


def _subgraph_service_register_access_source(contract_import: str, hypothesis_id: str) -> str:
    safe_id = _safe_identifier(hypothesis_id)
    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {{Test}} from "forge-std/Test.sol";
import {{ERC1967Proxy}} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {{IHorizonStaking}} from "@graphprotocol/interfaces/contracts/horizon/IHorizonStaking.sol";
import {{IHorizonStakingTypes}} from "@graphprotocol/interfaces/contracts/horizon/internal/IHorizonStakingTypes.sol";
import {{SubgraphService}} from "{contract_import}";

contract MockGraphController {{
    address internal dummy = address(0xCAFE);
    address internal staking;

    function setStaking(address staking_) external {{
        staking = staking_;
    }}

    function getContractProxy(bytes32 id) external view returns (address) {{
        if (id == keccak256(bytes("Staking"))) return staking;
        return dummy;
    }}
}}

contract MockHorizonStaking {{
    mapping(address => bool) internal authorized;
    mapping(address => IHorizonStakingTypes.Provision) internal provisions;

    function setAuthorized(address serviceProvider, bool allowed) external {{
        authorized[serviceProvider] = allowed;
    }}

    function setProvision(address serviceProvider, uint256 tokens) external {{
        provisions[serviceProvider] = IHorizonStakingTypes.Provision({{
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
        }});
    }}

    function isAuthorized(address serviceProvider, address, address operator) external view returns (bool) {{
        return authorized[serviceProvider] && operator == serviceProvider;
    }}

    function getProvision(address serviceProvider, address) external view returns (IHorizonStaking.Provision memory) {{
        return provisions[serviceProvider];
    }}

    function getTokensAvailable(address serviceProvider, address, uint32) external view returns (uint256) {{
        IHorizonStakingTypes.Provision memory provision = provisions[serviceProvider];
        return provision.tokens - provision.tokensThawing;
    }}
}}

contract MockDisputeManager {{
    function getDisputePeriod() external pure returns (uint64) {{
        return 1;
    }}

    function getFishermanRewardCut() external pure returns (uint32) {{
        return 0;
    }}
}}

contract SubgraphServiceRealHarnessTest is Test {{
    address internal owner = address(0xA11CE);
    address internal indexer = address(0x1D3A);
    address internal attacker = address(0xB0B);
    address internal paymentsDestination = address(0xFEE);
    MockHorizonStaking internal staking;
    SubgraphService internal service;

    function setUp() public {{
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
    }}

    // Hypothesis: {hypothesis_id}
    // Local-only invariant: register should require an authorized, valid provision and update only indexer metadata.
    function test_{safe_id}_authorizedIndexerCanRegisterAndSetPaymentDestination() public {{
        staking.setAuthorized(indexer, true);
        staking.setProvision(indexer, 2 ether);

        bytes memory data = abi.encode("https://indexer.local", "9q8yy", paymentsDestination);
        vm.prank(indexer);
        service.register(indexer, data);

        (string memory url, string memory geoHash) = service.indexers(indexer);
        assertEq(url, "https://indexer.local");
        assertEq(geoHash, "9q8yy");
        assertEq(service.paymentsDestination(indexer), paymentsDestination);
    }}

    function test_{safe_id}_unauthorizedCallerCannotRegisterIndexer() public {{
        staking.setAuthorized(indexer, true);
        staking.setProvision(indexer, 2 ether);

        bytes memory data = abi.encode("https://indexer.local", "9q8yy", paymentsDestination);
        vm.prank(attacker);
        vm.expectRevert();
        service.register(indexer, data);
    }}

    function test_{safe_id}_missingProvisionCannotRegister() public {{
        staking.setAuthorized(indexer, true);

        bytes memory data = abi.encode("https://indexer.local", "9q8yy", paymentsDestination);
        vm.prank(indexer);
        vm.expectRevert();
        service.register(indexer, data);
    }}
}}
"""


def _subgraph_service_start_service_allocation_source(contract_import: str, hypothesis_id: str) -> str:
    safe_id = _safe_identifier(hypothesis_id)
    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {{Test}} from "forge-std/Test.sol";
import {{ERC1967Proxy}} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {{IHorizonStaking}} from "@graphprotocol/interfaces/contracts/horizon/IHorizonStaking.sol";
import {{IHorizonStakingTypes}} from "@graphprotocol/interfaces/contracts/horizon/internal/IHorizonStakingTypes.sol";
import {{SubgraphService}} from "{contract_import}";

contract MockGraphController {{
    address internal dummy = address(0xCAFE);
    address internal staking;
    address internal epochManager;
    address internal rewardsManager;

    function setStaking(address staking_) external {{ staking = staking_; }}
    function setEpochManager(address epochManager_) external {{ epochManager = epochManager_; }}
    function setRewardsManager(address rewardsManager_) external {{ rewardsManager = rewardsManager_; }}

    function getContractProxy(bytes32 id) external view returns (address) {{
        if (id == keccak256(bytes("Staking"))) return staking;
        if (id == keccak256(bytes("EpochManager"))) return epochManager;
        if (id == keccak256(bytes("RewardsManager"))) return rewardsManager;
        return dummy;
    }}
}}

contract MockHorizonStaking {{
    mapping(address => bool) internal authorized;
    mapping(address => IHorizonStakingTypes.Provision) internal provisions;
    mapping(address => bool) internal legacyAllocations;

    function setAuthorized(address serviceProvider, bool allowed) external {{
        authorized[serviceProvider] = allowed;
    }}

    function setProvision(address serviceProvider, uint256 tokens) external {{
        provisions[serviceProvider] = IHorizonStakingTypes.Provision({{
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
        }});
    }}

    function setLegacyAllocation(address allocationId, bool exists) external {{
        legacyAllocations[allocationId] = exists;
    }}

    function isAuthorized(address serviceProvider, address, address operator) external view returns (bool) {{
        return authorized[serviceProvider] && operator == serviceProvider;
    }}

    function getProvision(address serviceProvider, address) external view returns (IHorizonStaking.Provision memory) {{
        return provisions[serviceProvider];
    }}

    function getTokensAvailable(address serviceProvider, address, uint32) external view returns (uint256) {{
        IHorizonStakingTypes.Provision memory provision = provisions[serviceProvider];
        return provision.tokens - provision.tokensThawing;
    }}

    function isAllocation(address allocationId) external view returns (bool) {{
        return legacyAllocations[allocationId];
    }}
}}

contract MockDisputeManager {{
    function getDisputePeriod() external pure returns (uint64) {{ return 1; }}
    function getFishermanRewardCut() external pure returns (uint32) {{ return 0; }}
}}

contract MockEpochManager {{
    function currentEpoch() external pure returns (uint256) {{ return 7; }}
}}

contract MockRewardsManager {{
    function onSubgraphAllocationUpdate(bytes32) external pure returns (uint256) {{ return 0; }}
    function calcRewards(uint256 tokens, uint256 accRewardsPerAllocatedToken) external pure returns (uint256) {{
        return tokens * accRewardsPerAllocatedToken;
    }}
    function isDenied(bytes32) external pure returns (bool) {{ return false; }}
    function takeRewards(address) external pure returns (uint256) {{ return 0; }}
    function reclaimRewards(bytes32, address) external pure returns (uint256) {{ return 0; }}
}}

contract SubgraphServiceRealHarnessTest is Test {{
    uint256 internal allocationPrivateKey = 0xA110CA710;
    address internal owner = address(0xA11CE);
    address internal indexer = address(0x1D3A);
    address internal allocationId;
    bytes32 internal subgraphDeploymentId = keccak256("subgraph-deployment");
    MockHorizonStaking internal staking;
    SubgraphService internal service;

    function setUp() public {{
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
    }}

    // Hypothesis: {hypothesis_id}
    // Local-only invariant: startService should create exactly one allocation and update subgraph accounting.
    function test_{safe_id}_startServiceCreatesAllocationAndTracksSubgraphTokens() public {{
        uint256 tokens = 2 ether;
        bytes memory allocationProof = _allocationProof(indexer, allocationId);
        bytes memory data = abi.encode(subgraphDeploymentId, tokens, allocationId, allocationProof);

        vm.prank(indexer);
        service.startService(indexer, data);

        (bool isOpen, address actualIndexer, bytes32 actualSubgraph, uint256 actualTokens, , ) =
            service.getAllocationData(allocationId);
        assertTrue(isOpen);
        assertEq(actualIndexer, indexer);
        assertEq(actualSubgraph, subgraphDeploymentId);
        assertEq(actualTokens, tokens);
        assertEq(service.getSubgraphAllocatedTokens(subgraphDeploymentId), tokens);
    }}

    function test_{safe_id}_cannotReuseAllocationId() public {{
        uint256 tokens = 2 ether;
        bytes memory data = abi.encode(subgraphDeploymentId, tokens, allocationId, _allocationProof(indexer, allocationId));

        vm.prank(indexer);
        service.startService(indexer, data);

        vm.prank(indexer);
        vm.expectRevert();
        service.startService(indexer, data);
    }}

    function test_{safe_id}_invalidAllocationProofCannotStartService() public {{
        address wrongAllocationId = address(0xBAD);
        bytes memory data = abi.encode(
            subgraphDeploymentId,
            2 ether,
            wrongAllocationId,
            _allocationProof(indexer, allocationId)
        );

        vm.prank(indexer);
        vm.expectRevert();
        service.startService(indexer, data);
    }}

    function _allocationProof(address indexer_, address allocationId_) internal view returns (bytes memory) {{
        bytes32 digest = service.encodeAllocationProof(indexer_, allocationId_);
        (uint8 v, bytes32 r, bytes32 s) = vm.sign(allocationPrivateKey, digest);
        return abi.encodePacked(r, s, v);
    }}
}}
"""


def _subgraph_service_resize_allocation_source(contract_import: str, hypothesis_id: str) -> str:
    safe_id = _safe_identifier(hypothesis_id)
    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {{Test}} from "forge-std/Test.sol";
import {{ERC1967Proxy}} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {{IHorizonStaking}} from "@graphprotocol/interfaces/contracts/horizon/IHorizonStaking.sol";
import {{IHorizonStakingTypes}} from "@graphprotocol/interfaces/contracts/horizon/internal/IHorizonStakingTypes.sol";
import {{SubgraphService}} from "{contract_import}";

contract MockGraphController {{
    address internal dummy = address(0xCAFE);
    address internal staking;
    address internal epochManager;
    address internal rewardsManager;

    function setStaking(address staking_) external {{ staking = staking_; }}
    function setEpochManager(address epochManager_) external {{ epochManager = epochManager_; }}
    function setRewardsManager(address rewardsManager_) external {{ rewardsManager = rewardsManager_; }}

    function getContractProxy(bytes32 id) external view returns (address) {{
        if (id == keccak256(bytes("Staking"))) return staking;
        if (id == keccak256(bytes("EpochManager"))) return epochManager;
        if (id == keccak256(bytes("RewardsManager"))) return rewardsManager;
        return dummy;
    }}
}}

contract MockHorizonStaking {{
    mapping(address => bool) internal authorized;
    mapping(address => IHorizonStakingTypes.Provision) internal provisions;
    mapping(address => bool) internal legacyAllocations;

    function setAuthorized(address serviceProvider, bool allowed) external {{
        authorized[serviceProvider] = allowed;
    }}

    function setProvision(address serviceProvider, uint256 tokens) external {{
        provisions[serviceProvider] = IHorizonStakingTypes.Provision({{
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
        }});
    }}

    function isAuthorized(address serviceProvider, address, address operator) external view returns (bool) {{
        return authorized[serviceProvider] && operator == serviceProvider;
    }}

    function getProvision(address serviceProvider, address) external view returns (IHorizonStaking.Provision memory) {{
        return provisions[serviceProvider];
    }}

    function getTokensAvailable(address serviceProvider, address, uint32) external view returns (uint256) {{
        IHorizonStakingTypes.Provision memory provision = provisions[serviceProvider];
        return provision.tokens - provision.tokensThawing;
    }}

    function isAllocation(address allocationId) external view returns (bool) {{
        return legacyAllocations[allocationId];
    }}
}}

contract MockDisputeManager {{
    function getDisputePeriod() external pure returns (uint64) {{ return 1; }}
    function getFishermanRewardCut() external pure returns (uint32) {{ return 0; }}
}}

contract MockEpochManager {{
    function currentEpoch() external pure returns (uint256) {{ return 7; }}
}}

contract MockRewardsManager {{
    function onSubgraphAllocationUpdate(bytes32) external pure returns (uint256) {{ return 0; }}
    function calcRewards(uint256 tokens, uint256 accRewardsPerAllocatedToken) external pure returns (uint256) {{
        return tokens * accRewardsPerAllocatedToken;
    }}
    function isDenied(bytes32) external pure returns (bool) {{ return false; }}
    function takeRewards(address) external pure returns (uint256) {{ return 0; }}
    function reclaimRewards(bytes32, address) external pure returns (uint256) {{ return 0; }}
}}

contract SubgraphServiceRealHarnessTest is Test {{
    uint256 internal allocationPrivateKey = 0xA110CA710;
    address internal owner = address(0xA11CE);
    address internal indexer = address(0x1D3A);
    address internal attacker = address(0xB0B);
    address internal allocationId;
    bytes32 internal subgraphDeploymentId = keccak256("subgraph-deployment");
    MockHorizonStaking internal staking;
    SubgraphService internal service;

    function setUp() public {{
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
    }}

    // Hypothesis: {hypothesis_id}
    // Local-only invariant: resizing should keep allocation, subgraph, and locked provision accounting synchronized.
    function test_{safe_id}_resizeUpAndDownKeepsAccountingInSync() public {{
        _assertAllocationAccounting(2 ether);

        vm.prank(indexer);
        service.resizeAllocation(indexer, allocationId, 5 ether);
        _assertAllocationAccounting(5 ether);

        vm.prank(indexer);
        service.resizeAllocation(indexer, allocationId, 1 ether);
        _assertAllocationAccounting(1 ether);
    }}

    function test_{safe_id}_sameSizeResizeReverts() public {{
        vm.prank(indexer);
        vm.expectRevert();
        service.resizeAllocation(indexer, allocationId, 2 ether);
    }}

    function test_{safe_id}_unauthorizedResizeReverts() public {{
        vm.prank(attacker);
        vm.expectRevert();
        service.resizeAllocation(indexer, allocationId, 5 ether);
    }}

    function _startAllocation(uint256 tokens) internal {{
        bytes memory data = abi.encode(subgraphDeploymentId, tokens, allocationId, _allocationProof(indexer, allocationId));
        vm.prank(indexer);
        service.startService(indexer, data);
    }}

    function _assertAllocationAccounting(uint256 expectedTokens) internal view {{
        (bool isOpen, address actualIndexer, bytes32 actualSubgraph, uint256 actualTokens, , ) =
            service.getAllocationData(allocationId);
        assertTrue(isOpen);
        assertEq(actualIndexer, indexer);
        assertEq(actualSubgraph, subgraphDeploymentId);
        assertEq(actualTokens, expectedTokens);
        assertEq(service.getSubgraphAllocatedTokens(subgraphDeploymentId), expectedTokens);
        assertEq(service.allocationProvisionTracker(indexer), expectedTokens);
    }}

    function _allocationProof(address indexer_, address allocationId_) internal view returns (bytes memory) {{
        bytes32 digest = service.encodeAllocationProof(indexer_, allocationId_);
        (uint8 v, bytes32 r, bytes32 s) = vm.sign(allocationPrivateKey, digest);
        return abi.encodePacked(r, s, v);
    }}
}}
"""


def _subgraph_service_stop_service_accounting_source(contract_import: str, hypothesis_id: str) -> str:
    safe_id = _safe_identifier(hypothesis_id)
    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {{Test}} from "forge-std/Test.sol";
import {{ERC1967Proxy}} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {{IHorizonStaking}} from "@graphprotocol/interfaces/contracts/horizon/IHorizonStaking.sol";
import {{IHorizonStakingTypes}} from "@graphprotocol/interfaces/contracts/horizon/internal/IHorizonStakingTypes.sol";
import {{SubgraphService}} from "{contract_import}";

contract MockGraphController {{
    address internal dummy = address(0xCAFE);
    address internal staking;
    address internal epochManager;
    address internal rewardsManager;

    function setStaking(address staking_) external {{ staking = staking_; }}
    function setEpochManager(address epochManager_) external {{ epochManager = epochManager_; }}
    function setRewardsManager(address rewardsManager_) external {{ rewardsManager = rewardsManager_; }}

    function getContractProxy(bytes32 id) external view returns (address) {{
        if (id == keccak256(bytes("Staking"))) return staking;
        if (id == keccak256(bytes("EpochManager"))) return epochManager;
        if (id == keccak256(bytes("RewardsManager"))) return rewardsManager;
        return dummy;
    }}
}}

contract MockHorizonStaking {{
    mapping(address => bool) internal authorized;
    mapping(address => IHorizonStakingTypes.Provision) internal provisions;
    mapping(address => bool) internal legacyAllocations;

    function setAuthorized(address serviceProvider, bool allowed) external {{
        authorized[serviceProvider] = allowed;
    }}

    function setProvision(address serviceProvider, uint256 tokens) external {{
        provisions[serviceProvider] = IHorizonStakingTypes.Provision({{
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
        }});
    }}

    function isAuthorized(address serviceProvider, address, address operator) external view returns (bool) {{
        return authorized[serviceProvider] && operator == serviceProvider;
    }}

    function getProvision(address serviceProvider, address) external view returns (IHorizonStaking.Provision memory) {{
        return provisions[serviceProvider];
    }}

    function getTokensAvailable(address serviceProvider, address, uint32) external view returns (uint256) {{
        IHorizonStakingTypes.Provision memory provision = provisions[serviceProvider];
        return provision.tokens - provision.tokensThawing;
    }}

    function isAllocation(address allocationId) external view returns (bool) {{
        return legacyAllocations[allocationId];
    }}
}}

contract MockDisputeManager {{
    function getDisputePeriod() external pure returns (uint64) {{ return 1; }}
    function getFishermanRewardCut() external pure returns (uint32) {{ return 0; }}
}}

contract MockEpochManager {{
    function currentEpoch() external pure returns (uint256) {{ return 7; }}
}}

contract MockRewardsManager {{
    function onSubgraphAllocationUpdate(bytes32) external pure returns (uint256) {{ return 0; }}
    function calcRewards(uint256 tokens, uint256 accRewardsPerAllocatedToken) external pure returns (uint256) {{
        return tokens * accRewardsPerAllocatedToken;
    }}
    function isDenied(bytes32) external pure returns (bool) {{ return false; }}
    function takeRewards(address) external pure returns (uint256) {{ return 0; }}
    function reclaimRewards(bytes32, address) external pure returns (uint256) {{ return 0; }}
}}

contract SubgraphServiceRealHarnessTest is Test {{
    uint256 internal allocationPrivateKey = 0xA110CA710;
    address internal owner = address(0xA11CE);
    address internal indexer = address(0x1D3A);
    address internal attacker = address(0xB0B);
    address internal allocationId;
    bytes32 internal subgraphDeploymentId = keccak256("subgraph-deployment");
    MockHorizonStaking internal staking;
    SubgraphService internal service;

    function setUp() public {{
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
    }}

    // Hypothesis: {hypothesis_id}
    // Local-only invariant: stopService should close the allocation and release aggregate accounting.
    function test_{safe_id}_stopServiceClosesAllocationAndReleasesAccounting() public {{
        _assertOpenAccounting(2 ether);

        vm.warp(100);
        vm.prank(indexer);
        service.stopService(indexer, abi.encode(allocationId));

        (bool isOpen, address actualIndexer, bytes32 actualSubgraph, uint256 actualTokens, , ) =
            service.getAllocationData(allocationId);
        assertFalse(isOpen);
        assertEq(actualIndexer, indexer);
        assertEq(actualSubgraph, subgraphDeploymentId);
        assertEq(actualTokens, 2 ether);
        assertEq(service.getSubgraphAllocatedTokens(subgraphDeploymentId), 0);
        assertEq(service.allocationProvisionTracker(indexer), 0);
    }}

    function test_{safe_id}_cannotStopClosedAllocationTwice() public {{
        vm.warp(100);
        vm.prank(indexer);
        service.stopService(indexer, abi.encode(allocationId));

        vm.prank(indexer);
        vm.expectRevert();
        service.stopService(indexer, abi.encode(allocationId));
    }}

    function test_{safe_id}_unauthorizedStopServiceReverts() public {{
        vm.prank(attacker);
        vm.expectRevert();
        service.stopService(indexer, abi.encode(allocationId));
    }}

    function _startAllocation(uint256 tokens) internal {{
        bytes memory data = abi.encode(subgraphDeploymentId, tokens, allocationId, _allocationProof(indexer, allocationId));
        vm.prank(indexer);
        service.startService(indexer, data);
    }}

    function _assertOpenAccounting(uint256 expectedTokens) internal view {{
        (bool isOpen, address actualIndexer, bytes32 actualSubgraph, uint256 actualTokens, , ) =
            service.getAllocationData(allocationId);
        assertTrue(isOpen);
        assertEq(actualIndexer, indexer);
        assertEq(actualSubgraph, subgraphDeploymentId);
        assertEq(actualTokens, expectedTokens);
        assertEq(service.getSubgraphAllocatedTokens(subgraphDeploymentId), expectedTokens);
        assertEq(service.allocationProvisionTracker(indexer), expectedTokens);
    }}

    function _allocationProof(address indexer_, address allocationId_) internal view returns (bytes memory) {{
        bytes32 digest = service.encodeAllocationProof(indexer_, allocationId_);
        (uint8 v, bytes32 r, bytes32 s) = vm.sign(allocationPrivateKey, digest);
        return abi.encodePacked(r, s, v);
    }}
}}
"""


def _safe_identifier(value: str) -> str:
    safe = "".join(char if char.isalnum() else "_" for char in value)
    return safe.strip("_") or "hypothesis"


def _readme(metadata: dict[str, Any]) -> str:
    return f"""# Real Foundry Harness

Target: `{metadata["target"]}`

Contract: `{metadata["contract_name"]}`

Hypothesis: `{metadata["hypothesis_id"]}`

This harness imports the real contract path and runs `forge test`.

Statuses are conservative:

- `compile_failed`: imports/remappings/mocks need work.
- `harness_needs_mocks`: constructor or setup is not wired.
- `clean`: generated compile smoke passed.

Generated tests alone are never report-ready.
"""
