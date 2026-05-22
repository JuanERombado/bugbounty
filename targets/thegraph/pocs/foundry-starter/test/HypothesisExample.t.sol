// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {HypothesisExample} from "../src/HypothesisExample.sol";

contract HypothesisExampleTest {
    HypothesisExample internal example;

    function setUp() public {
        example = new HypothesisExample();
    }

    function testLocalAccountingInvariant() public {
        example.deposit{value: 1 ether}();

        require(example.balances(address(this)) == 1 ether, "wrong recorded balance");
        require(address(example).balance == 1 ether, "wrong contract balance");
    }
}
