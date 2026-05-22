# SubgraphService H3 Actor-Control Gate 001

## Goal

Check whether `SUBGRAPH-INV-3` becomes bounty-relevant through unauthorized actor control.

## Stronger Question

Can a non-payer signer introduce overflow-prone indexing agreement terms and leave SubgraphService in a dangerous local state even if the collector rejects the update?

## Local-Only Test

```powershell
forge test --match-test "test_SubgraphService_UpdateIndexingAgreement_InvalidSignerDoesNotPersistOverflowTerms|test_SubgraphService_UpdateIndexingAgreement_ReplayDoesNotRestoreOverflowTerms" -vv
```

Working directory:

```text
external/thegraph-contracts/packages/subgraph-service
```

## Test Shape

1. Accept a normal indexing agreement.
2. Build an update with `tokensPerEntityPerSecond = type(uint256).max`.
3. Sign the update with a key that is not authorized by the payer.
4. Confirm the collector rejects the update with `RecurringCollectorInvalidSigner`.
5. Collect afterward with two entities and confirm overflow-prone terms were not persisted.

## Result

The targeted actor-control and replay tests passed across 256 fuzz runs each.

```text
[PASS] test_SubgraphService_UpdateIndexingAgreement_InvalidSignerDoesNotPersistOverflowTerms(...) (runs: 256)
[PASS] test_SubgraphService_UpdateIndexingAgreement_ReplayDoesNotRestoreOverflowTerms(...) (runs: 256)
2 tests passed, 0 failed, 0 skipped
```

## Judgment

Status: `rejected_unauthorized_signer_path`

The unauthorized-signer branch does not currently support a paid-report path because collector authorization failure rolls back SubgraphService term writes.

## Next Step

Run the final H3 authorization branch: contract-payer or stored-offer update approval, then decide whether H3 is dead or only a low-value self-approved edge case.
