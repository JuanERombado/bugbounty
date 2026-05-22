# Dispute D5 Test Plan

## Question

Can a related conflict dispute be finalized again after the other side already resolved it?

## Local-Only Setup

- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/disputes/query.test.ts`
- Contract under test: `DisputeManager`
- Flow: create linked conflict disputes, resolve one side, then try to accept/reject/draw the related side.

## Tests Added

- `rejects resolving a related dispute after accepting the other side`
- `rejects resolving a related dispute after drawing the other side`

## Expected Safe Behavior

The related dispute should no longer be pending, so later resolution attempts should revert.

## Result

Rejected.

The related dispute cannot be finalized again.

## Command

```powershell
pnpm exec hardhat test --network hardhat tests/unit/disputes/query.test.ts --grep "rejects resolving a related dispute"
```

## Evidence

- `2 passing`
- Accepting one side blocks accept/reject/draw on the related dispute.
- Drawing one side blocks accept/reject/draw on the related dispute.

## Next Step

Test D4 by checking how stake changes between dispute creation and acceptance affect the slash amount.
