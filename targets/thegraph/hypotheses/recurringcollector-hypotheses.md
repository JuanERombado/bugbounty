# RecurringCollector Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`, `covered-existing-tests`, `likely-intended`.

## RC1: Zero-Token Collection Advances Time Without Paying

- Status: covered-existing-tests
- Asset: `RecurringCollector.collect`.
- Hypothesis: a data service can call `collect` with zero tokens to advance `lastCollectionAt` and reduce future collectable value.
- Why it might matter: this could grief the service provider or break accounting.
- Result: the contract enforces `minSecondsPerCollection` even when requested tokens are zero.
- Evidence file: `external/thegraph-contracts/packages/horizon/test/unit/payments/recurring-collector/collect.t.sol`.
- Next check: none unless agreement-manager behavior creates a separate incentive.

## RC2: Pending Updates Can Under-Reserve Escrow

- Status: covered-existing-tests
- Asset: `getMaxNextClaim` plus `update`.
- Hypothesis: a pending update can raise rate or max collection window so the post-update collection exceeds the pre-update escrow reservation.
- Why it might matter: under-reserved agreements could revert during collection or create accounting gaps.
- Result: existing tests assert the post-update collection fits inside the pre-update max-claim envelope.
- Evidence file: `external/thegraph-contracts/packages/horizon/test/unit/payments/recurring-collector/getMaxNextClaim.t.sol`.
- Next check: inspect `RecurringAgreementManager` to confirm it actually uses this envelope correctly.

## RC3: Idempotent Accept or Update Skips Fresh Authorization

- Status: likely-intended
- Asset: `accept` and `update`.
- Hypothesis: repeating the same accepted agreement or active update skips deadline and authorization checks.
- Why it might matter: stale signatures sometimes become reusable in surprising states.
- Result: the shortcut only returns when the active hash already matches, so it creates no new payment authority.
- Evidence file: `external/thegraph-contracts/packages/horizon/test/unit/payments/recurring-collector/accept.t.sol`.
- Next check: keep in mind for state-transition review, but not a live hypothesis.

## RC4: Payer Cancellation Allows Unexpected Final Collection

- Status: covered-existing-tests
- Asset: cancellation plus `_getCollectionInfo`.
- Hypothesis: after payer cancellation, the data service can collect more than the elapsed amount.
- Why it might matter: cancellation should stop future accrual while still allowing owed elapsed fees.
- Result: tests cover service-provider cancellation blocking collection and payer cancellation allowing only elapsed final collection.
- Evidence file: `external/thegraph-contracts/packages/horizon/test/unit/payments/recurring-collector/coverageGaps.t.sol`.
- Next check: compare this with `RecurringAgreementManager` escrow release behavior after cancellation.

## RC5: Payer Callback Failures Bypass Payer Protections

- Status: likely-intended
- Asset: agreement callback conditions.
- Hypothesis: `beforeCollection` or `afterCollection` failure only emits an event and does not revert collection.
- Why it might matter: payers may expect callback failure to block collection.
- Result: eligibility returning explicit false blocks collection; notification callback failures are treated as non-blocking.
- Evidence files: `afterCollection.t.sol`, `eligibility.t.sol`, and `returndataBomb.t.sol`.
- Next check: confirm docs or interfaces describe these callbacks as notifications rather than hard authorization.

## RC6: Callback Interface Support Can Change After Acceptance

- Status: new
- Asset: condition validation and payer callbacks.
- Hypothesis: a payer contract can support required interfaces at acceptance, then later stop supporting them or change callback behavior.
- Why it might matter: assumptions checked at acceptance may not hold when collection occurs.
- Local test idea: model an upgradeable payer that reports interface support during `accept`, then changes behavior before `collect`.
- Expected impact: probably low or intended, because the payer controls this behavior and can already cancel or refuse service through eligibility.

## Next Step

Review `RecurringAgreementManager` escrow reservation and release logic, because that is where a collector math issue could become a payment-impact issue.
