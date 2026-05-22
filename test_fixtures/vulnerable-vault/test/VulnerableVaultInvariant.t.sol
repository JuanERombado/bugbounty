// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {FixedVault, VulnerableVault} from "../src/VulnerableVault.sol";

contract Actor {
    receive() external payable {}

    function depositTo(VulnerableVault vault) external payable {
        vault.deposit{value: msg.value}();
    }

    function withdrawFrom(VulnerableVault vault, uint256 amount) external {
        vault.withdraw(amount);
    }

    function changeFeeRecipient(VulnerableVault vault, address recipient) external {
        vault.setFeeRecipient(recipient);
    }

    function depositToFixed(FixedVault vault) external payable {
        vault.deposit{value: msg.value}();
    }

    function withdrawFromFixed(FixedVault vault, uint256 amount) external {
        vault.withdraw(amount);
    }

    function changeFixedFeeRecipient(FixedVault vault, address recipient) external {
        vault.setFeeRecipient(recipient);
    }
}

contract VulnerableVaultInvariantTest {
    function testInvariant_VulnerableVault_AllDepositsWithdrawable() public {
        VulnerableVault vault = new VulnerableVault();
        Actor actor = new Actor();

        actor.depositTo{value: 1 ether}(vault);
        actor.withdrawFrom(vault, 1 ether);

        require(vault.accountingInvariant(), "BUG: vault balance no longer equals totalDeposits");
    }

    function testInvariant_VulnerableVault_OnlyOwnerCanSetFeeRecipient() public {
        VulnerableVault vault = new VulnerableVault();
        Actor attacker = new Actor();

        attacker.changeFeeRecipient(vault, address(0xBEEF));

        require(vault.feeRecipient() != address(0xBEEF), "BUG: non-owner changed fee recipient");
    }
}

contract FixedVaultInvariantTest {
    function testInvariant_FixedVault_AllDepositsWithdrawable() public {
        FixedVault vault = new FixedVault();
        Actor actor = new Actor();

        actor.depositToFixed{value: 1 ether}(vault);
        actor.withdrawFromFixed(vault, 1 ether);

        require(vault.accountingInvariant(), "fixed vault accounting invariant failed");
    }

    function testInvariant_FixedVault_OnlyOwnerCanSetFeeRecipient() public {
        FixedVault vault = new FixedVault();
        Actor attacker = new Actor();

        try attacker.changeFixedFeeRecipient(vault, address(0xBEEF)) {
            revert("fixed vault allowed non-owner fee recipient change");
        } catch {}

        require(vault.feeRecipient() != address(0xBEEF), "fixed vault fee recipient changed");
    }
}
