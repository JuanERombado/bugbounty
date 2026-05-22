# Dispute D4 Test Plan

## Question

Does `DisputeManager` slash current stake or stake at the time the dispute was created?

## Local-Only Setup

- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/disputes/query.test.ts`
- Contract under test: `DisputeManager`
- Flow: create a query dispute, increase indexer stake, then accept the dispute.

## Test Added

- `slashes current stake after stake increases post-dispute creation`

## Expected Behavior

The contract should do exactly what its accounting model implies; in this version, there is no dispute-time stake snapshot.

## Result

Rejected as a candidate finding.

The slash amount is based on current stake at acceptance time.

## Command

```powershell
pnpm exec hardhat test --network hardhat tests/unit/disputes/query.test.ts --grep "slashes current stake"
```

## Evidence

- `1 passing`
- Increasing stake after dispute creation increased the base used for the accepted-dispute slash.

## Next Step

Test D2 by confirming linked conflict disputes resolve both sides consistently in accept and draw paths.
