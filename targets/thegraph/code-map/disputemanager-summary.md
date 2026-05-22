# DisputeManager Summary

## Plain-English Purpose

`DisputeManager` lets challengers create query or indexing disputes, then lets the arbitrator accept, reject, or draw those disputes.

## Value Movement

- Creating a normal query or indexing dispute pulls a GRT deposit from the fisherman into `DisputeManager`.
- Accepting a dispute slashes the indexer through `Staking`, returns the fisherman deposit, and pays the fisherman a cut of the slashed stake.
- Rejecting a dispute burns the fisherman deposit.
- Drawing a dispute returns the fisherman deposit without slashing the indexer.
- Conflict disputes have zero deposit and create two linked disputes from conflicting attestations.

## Role Checks

- Only governance can set the arbitrator, minimum deposit, fisherman reward percentage, and slashing percentages.
- Only the arbitrator can accept, reject, or draw disputes.
- `DisputeManager` must be approved as a slasher in `Staking` before accepted disputes can slash indexers.

## Dispute Identity

- Indexing dispute ID: `keccak256(allocationID)`.
- Query dispute ID: `keccak256(requestCID, responseCID, subgraphDeploymentID, indexer, fisherman)`.
- Because the query dispute ID includes `fisherman`, different fishermen can create separate disputes for the same attestation.

## Important Invariants

- One underlying bad action should not be slashable more times than intended.
- A dispute should only move from `Pending` to one final status.
- Deposits should be returned, burned, or left untouched exactly once.
- Conflict disputes should resolve both sides consistently.
- Slashing should never exceed the configured percentage of the current slashable stake.

## First Things To Hunt

- Duplicate query disputes for the same attestation but different fishermen.
- Accepting one conflict dispute resolving the related dispute correctly.
- Draw/reject paths returning or burning deposits exactly once.
- Zero slashing configuration and missing slasher permission edge cases.
- Stale or withdrawn indexer stake between dispute creation and acceptance.
