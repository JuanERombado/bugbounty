# Dispute D1 Test Plan

## Question

Can the same query attestation be disputed by multiple fishermen and accepted more than once?

## Local-Only Setup

- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/disputes/query.test.ts`
- Contract under test: `packages/contracts/contracts/disputes/DisputeManager.sol`
- Flow: create a normal query dispute, create a duplicate dispute with the same attestation from a second fisherman, then accept both.

## Test Added

- `accepts duplicate query disputes from different fishermen and slashes twice`

## Expected Safe Behavior

If the protocol intends one slash per underlying attestation, the second accepted dispute should not slash again.

## Observed Behavior

Confirmed locally, then rejected as a candidate finding.

The second fisherman can create a dispute for the same attestation, and the arbitrator can accept both disputes, causing two separate slashes.

## Command

```powershell
pnpm exec hardhat test --network hardhat tests/unit/disputes/query.test.ts --grep "accepts duplicate query disputes"
```

## Evidence

- `1 passing`
- After the first accept, indexer stake decreased by the first computed slash.
- After the second accept, indexer stake decreased again by a second computed slash.

## Reportability Check

Do not report.

OpenZeppelin's 2023 Dispute Manager audit explicitly documents that different fishermen can create query disputes against the same resolved attestation, and says responsibility falls on the arbitrator.

This is also slashing-centered, which is a scope trap for The Graph's listed critical impact.

## Next Step

Test D5 by trying to resolve related conflict disputes after one side has already finalized.
