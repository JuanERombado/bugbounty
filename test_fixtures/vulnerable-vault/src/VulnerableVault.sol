// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

contract VulnerableVault {
    mapping(address => uint256) public balances;
    uint256 public totalDeposits;
    address public owner;
    address public feeRecipient;

    constructor() {
        owner = msg.sender;
        feeRecipient = msg.sender;
    }

    function deposit() external payable {
        balances[msg.sender] += msg.value;
        totalDeposits += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "insufficient balance");
        balances[msg.sender] -= amount;
        // BUG: totalDeposits is not decremented, so accounting claims funds still exist.
        payable(msg.sender).transfer(amount);
    }

    function setFeeRecipient(address newFeeRecipient) external {
        // BUG: missing only-owner check lets any caller redirect fee recipient state.
        feeRecipient = newFeeRecipient;
    }

    function accountingInvariant() external view returns (bool) {
        return address(this).balance == totalDeposits;
    }
}

contract FixedVault {
    mapping(address => uint256) public balances;
    uint256 public totalDeposits;
    address public owner;
    address public feeRecipient;

    constructor() {
        owner = msg.sender;
        feeRecipient = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "only owner");
        _;
    }

    function deposit() external payable {
        balances[msg.sender] += msg.value;
        totalDeposits += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "insufficient balance");
        balances[msg.sender] -= amount;
        totalDeposits -= amount;
        payable(msg.sender).transfer(amount);
    }

    function setFeeRecipient(address newFeeRecipient) external onlyOwner {
        feeRecipient = newFeeRecipient;
    }

    function accountingInvariant() external view returns (bool) {
        return address(this).balance == totalDeposits;
    }
}
