// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {Test} from "forge-std/Test.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {SubgraphService} from "packages/subgraph-service/contracts/SubgraphService.sol";

contract MockGraphController {
    address internal dummy = address(0xCAFE);

    function getContractProxy(bytes32) external view returns (address) {
        return dummy;
    }
}

contract SubgraphServiceRealHarnessTest is Test {
    address internal owner = address(0xA11CE);
    address internal attacker = address(0xB0B);
    SubgraphService internal service;

    function setUp() public {
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
    }

    // Hypothesis: OWNER-ACCESS-001
    // Local-only invariant: owner-only economic configuration setters must reject arbitrary callers.
    function test_OWNER_ACCESS_001_nonOwnerCannotChangeEconomicSettings() public {
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
    }

    function test_OWNER_ACCESS_001_ownerCanChangeEconomicSettings() public {
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
    }
}
