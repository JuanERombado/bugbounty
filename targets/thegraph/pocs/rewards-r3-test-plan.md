# Rewards R3 Test Plan

## Question

Can changing a reclaim address redirect rewards that accrued before the address change?

## Local-Only Setup

- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/rewards/rewards-reclaim.test.ts`
- Contract under test: `RewardsManager`
- Flow: accrue allocation rewards, change `SUBGRAPH_DENIED` reclaim address, deny the subgraph, close the allocation.

## Test Added

- `should send accrued pre-denial rewards to the current reclaim address`

## Expected Safe Behavior

The current reclaim address receives reclaimed rewards, and the old reclaim address does not receive newly reclaimed rewards after it is replaced.

## Result

Rejected.

The behavior is real, but it matches the explicit contract comments and is governor-only.

## Command

```powershell
pnpm exec hardhat test --network hardhat tests/unit/rewards/rewards-reclaim.test.ts --grep "current reclaim address"
```

## Evidence

- `1 passing`
- The old reclaim wallet balance did not increase.
- The new reclaim wallet received the accrued pre-denial rewards.

## Next Step

Test R5 by connecting reward issuance assumptions to L1 bridge mint allowance limits.
