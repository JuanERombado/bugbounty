# SubgraphService Real H3 Validation 001

## Goal

Validate `SUBGRAPH-INV-3` against the real local The Graph SubgraphService Foundry harness.

## Hypothesis

An indexing agreement update with extreme `tokensPerEntityPerSecond` can make multi-entity collection revert before the recurring collector cap is applied.

## Local-Only Test

```powershell
forge test --match-test test_SubgraphService_CollectIndexingFees_Reverts_WhenEntityFeeRequestOverflowsBeforeCap -vv
```

Working directory:

```text
external/thegraph-contracts/packages/subgraph-service
```

## Harness Fixes

1. Moved `epochManager.currentEpochBlock()` before `vm.expectRevert()` so Foundry expects the intended `collect` call to revert.
2. Replaced `skip(1)` with `skip(uint256(rcau.minSecondsPerCollection) + 1)` so the test respects the agreement's collection interval.

## Result

The targeted test passed across 256 fuzz runs.

```text
[PASS] test_SubgraphService_CollectIndexingFees_Reverts_WhenEntityFeeRequestOverflowsBeforeCap(...) (runs: 256)
1 tests passed, 0 failed, 0 skipped
```

## Judgment

Status: `alive_not_report_ready`

This is useful local evidence that the overflow branch is reachable under payer-signed extreme terms, and that zero-entity collection can recover liveness afterward.

It is not report-ready because the current evidence looks like payer-approved pathological pricing rather than an unauthorized loss, insolvency, or accepted Immunefi impact.

## Next Step

Decide whether to kill H3 as low-value/self-harm or mutate it into a stronger invariant: "Can an indexer or third party force this revert or block honest collection without payer-approved pathological terms?"
