# RecurringAgreementManager Summary

## Plain-English Purpose

`RecurringAgreementManager` manages protocol-owned escrow for recurring collector agreements, using minted GRT to keep `PaymentsEscrow` funded.

## Value Movement

- `offerAgreement` forwards an agreement offer to a collector, tracks its max next claim, and reconciles escrow.
- `beforeCollection` can perform a just-in-time top-up if escrow is too small for the current collection.
- `afterCollection` reconciles the agreement after payment collection changes claim accounting.
- `reconcileAgreement` refreshes one agreement's max claim from the collector.
- `reconcileProvider` deposits deficits, thaws excess, withdraws matured thaws, and removes low-value stale tracking.

## Role Checks

- `AGREEMENT_MANAGER_ROLE` offers and cancels agreements.
- `OPERATOR_ROLE` can force-remove agreements and tune escrow mode parameters.
- `GOVERNOR_ROLE` controls core roles and issuance allocator setup.
- `PAUSE_ROLE` can pause and emergency-clear a broken eligibility oracle.
- Anyone can call reconciliation while unpaused.

## Accounting Invariants

- Per provider pair: `sumMaxNextClaim` should reflect the collector's current max claim for tracked agreements.
- Global: `totalEscrowDeficit` should equal the sum of underfunded provider-pair escrow deficits.
- `escrowSnap` should eventually match live `PaymentsEscrow` balance after reconciliation.
- Just-in-time top-up should deposit enough to cover `tokensToCollect`.
- Thaw logic should avoid resetting active thaw timers while still restoring required liquid escrow.

## Existing Defenses Found

- Escrow mode degrades when available funds cannot support full proactive escrow.
- Reconciliation syncs live escrow snapshots before making balance-sensitive decisions.
- Dust thaws are gated to reduce griefing by third-party `depositTo`.
- Untracked provider pairs can be drained without recreating tracking state.
- Tests cover many thaw, residual, basis-degradation, and stale-snapshot edge cases.

## Candidate Edge Found

`beforeCollection` deposits only when `deficit < GRAPH_TOKEN.balanceOf(address(this))`; if the manager has exactly the deficit amount, it skips the deposit even though it appears able to cover the collection.

## Next Step

Model and later run a full local Foundry test for the exact-deficit just-in-time top-up boundary.
