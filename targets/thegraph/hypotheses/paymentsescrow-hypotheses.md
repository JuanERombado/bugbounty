# PaymentsEscrow Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`, `covered-existing-tests`.

## PE1: Third-Party `depositTo` Can Distort Payer Escrow State

- Status: likely-intended
- Asset: PaymentsEscrow.
- Hypothesis: anyone can deposit tokens into another payer's escrow tuple, possibly affecting collectable balance or thaw/withdraw behavior.
- Why it might matter: unsolicited funds can change account state that other contracts may read.
- Impact if true: likely donation/griefing only, because the caller supplies the tokens and cannot withdraw them.
- Existing evidence: `testDepositTo_Tokens` covers third-party funding as expected behavior.
- Next check: see whether `RecurringCollector` or agreement manager incorrectly treats third-party top-ups as payer authorization.

## PE2: Collection During Thawing Can Leave Incorrect Thaw State

- Status: covered-existing-tests
- Asset: PaymentsEscrow collect/thaw accounting.
- Hypothesis: collecting while tokens are thawing can leave `tokensThawing` above `balance` or preserve a stale thaw timer.
- Why it might matter: payer withdrawal or collector collection could break.
- Result: existing tests cover full-balance collection resetting thaw state and partial collection capping `tokensThawing`.
- Evidence file: `external/thegraph-contracts/packages/horizon/test/unit/escrow/collect.t.sol`.

## PE3: `adjustThaw` Timer Semantics Can Surprise Payers

- Status: covered-existing-tests
- Asset: PaymentsEscrow thaw timer.
- Hypothesis: increasing or decreasing thaw amount can reset or preserve the timer unexpectedly.
- Why it might matter: payer funds may be delayed.
- Result: existing tests cover simple `thaw` timer reset, `adjustThaw` preserving timer on decrease, and `evenIfTimerReset=false`.
- Evidence file: `external/thegraph-contracts/packages/horizon/test/unit/escrow/thaw.t.sol`.

## PE4: External Payment Collection Can Desynchronize Escrow Balance

- Status: covered-existing-tests
- Asset: PaymentsEscrow collect external call to GraphPayments.
- Hypothesis: `GraphPayments.collect` could fail to pull exactly the approved amount, leaving escrow state inconsistent.
- Why it might matter: account balance could be debited without token movement.
- Result: code checks escrow token balance before/after collection; tests mock a no-op payment collector and expect revert.
- Evidence file: `external/thegraph-contracts/packages/horizon/test/unit/escrow/collect.t.sol`.

## Next Step

Map `RecurringCollector` authorization and time-based claim logic.
