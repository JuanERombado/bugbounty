// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

/// @notice Placeholder harness for SubgraphService.
/// @dev Replace this model with imports/mocks for: external/thegraph-contracts/packages/subgraph-service/contracts/SubgraphService.sol
contract ValidationHarness {
    uint256 public deposits;
    uint256 public paidOut;
    uint256 public lastRate;
    address public authorizedActor;
    bool public valueAffectingState;

    constructor() {
        authorizedActor = msg.sender;
    }

    function modelDeposit(uint256 amount) external {
        amount = bound(amount, 0, 1e30);
        deposits += amount;
    }

    function modelCollect(uint256 elapsed, uint256 rate, uint256 entities) external {
        elapsed = bound(elapsed, 0, 365 days);
        rate = bound(rate, 0, 1e24);
        entities = bound(entities, 0, 1e9);
        lastRate = rate;

        uint256 requested = elapsed * rate * (entities + 1);
        if (requested > deposits - paidOut) {
            requested = deposits - paidOut;
        }
        paidOut += requested;
    }

    function modelUnauthorizedStateChange(address caller) external {
        if (caller == authorizedActor) {
            valueAffectingState = true;
        }
    }

    function solvencyHolds() external view returns (bool) {
        return paidOut <= deposits;
    }

    function bound(uint256 value, uint256 min, uint256 max) internal pure returns (uint256) {
        if (max <= min) return min;
        return min + (value % (max - min + 1));
    }
}
