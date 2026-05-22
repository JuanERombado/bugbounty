# Rewards R1 Test Plan

## Question

Can changing `minimumSubgraphSignal` unexpectedly redirect or drop pending rewards?

## Local-Only Setup

- Files:
  - `external/thegraph-contracts/packages/contracts/contracts/rewards/RewardsManager.sol`
  - `external/thegraph-contracts/packages/contracts-test/tests/unit/rewards/rewards.test.ts`
  - `external/thegraph-contracts/packages/contracts-test/tests/unit/rewards/rewards-reclaim.test.ts`
- Contract under test: `RewardsManager`

## Test Used

- `should return zero rewards when subgraph signal is below minimum threshold`
- `does not revert with an underflow if the minimum signal changes`
- `does not revert with an underflow if the minimum signal changes, and signal came after allocation`
- `should reclaim when signal below minimum and BELOW_MINIMUM_SIGNAL address set`
- `should not reclaim when signal at or above minimum`
- `should drop rewards when below minimum and no reclaim address`
- `should use BELOW_MINIMUM_SIGNAL when denied but SUBGRAPH_DENIED address not configured`

## Expected Safe Behavior

Below-minimum rewards should either be reclaimed to a configured address or dropped, and threshold changes should not break accounting.

## Result

Rejected.

The threshold behavior is real, but it is explicitly documented as retroactive and covered by local tests.

## Command

```powershell
pnpm exec hardhat test --network hardhat tests/unit/rewards/rewards.test.ts tests/unit/rewards/rewards-reclaim.test.ts --grep "minimum signal changes|BELOW_MINIMUM_SIGNAL|below minimum"
```

## Evidence

- `7 passing`
- Below-minimum rewards are excluded.
- Threshold-change cases do not underflow.
- Reclaim routing works when a reclaim address exists.
- Rewards are dropped when no reclaim address exists.

## Next Step

Test R3 by checking whether reclaim address changes redirect old pending rewards exactly as the code comments document.
