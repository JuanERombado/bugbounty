# SubgraphService H3 Replay Gate 001

## Goal

Check whether `SUBGRAPH-INV-3` becomes bounty-relevant through stale update replay.

## Stronger Question

Can a stale payer-signed update with overflow-prone terms be replayed after a later safe update and restore dangerous collection terms?

## Local-Only Test

```powershell
forge test --match-test test_SubgraphService_UpdateIndexingAgreement_ReplayDoesNotRestoreOverflowTerms -vv
```

Working directory:

```text
external/thegraph-contracts/packages/subgraph-service
```

## Test Shape

1. Accept an indexing agreement.
2. Apply an update with `tokensPerEntityPerSecond = type(uint256).max`.
3. Apply a later safe update with zero per-entity pricing.
4. Replay the old bad update.
5. Collect with two entities and confirm the stale bad terms were not restored.

## Result

The targeted test passed across 256 fuzz runs.

```text
[PASS] test_SubgraphService_UpdateIndexingAgreement_ReplayDoesNotRestoreOverflowTerms(...) (runs: 256)
1 tests passed, 0 failed, 0 skipped
```

## Judgment

Status: `rejected_replay_path`

The stale replay branch does not currently support a paid-report path because the collector rejects the stale nonce and the SubgraphService-local terms remain safe after the revert.

## Next Step

Move from stale replay to actor-control: test whether a non-payer actor, contract-payer callback, or indexer-controlled field can cause the overflow-prone terms without fresh payer approval.
