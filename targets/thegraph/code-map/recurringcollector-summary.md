# RecurringCollector Summary

## Plain-English Purpose

`RecurringCollector` turns a payer-approved recurring payment agreement into bounded collections from `PaymentsEscrow`.

## Value Movement

- `accept` stores signed or pre-offered agreement terms; it does not move tokens.
- `collect` computes the allowed payment amount, updates `lastCollectionAt`, then asks `PaymentsEscrow` to pay.
- `update` replaces agreement terms after payer authorization; it does not reset `lastCollectionAt`.
- `cancel` marks the agreement canceled; payer cancellation can still allow one final collection for elapsed time.
- `getMaxNextClaim` estimates the largest next collection so agreement managers can reserve enough escrow.

## Role Checks

- Only the agreement `dataService` can accept, update, cancel, or collect.
- The payer must authorize new agreements and updates by signature or stored offer.
- Collection also requires the service provider to have tokens available with that data service.
- The collector contract treats itself as trusted only for delegated internal authorization flows.
- Pause guards can stop mutating entry points.

## Accounting Invariants

- A collection cannot exceed `rate * cappedElapsedSeconds + initialBonus`.
- `minSecondsPerCollection` is enforced even for zero-token collections.
- `maxSecondsPerCollection` caps one collection's claim; it is not a deadline.
- `lastCollectionAt` must move forward only when a valid collection occurs.
- `getMaxNextClaim` must overestimate, or at least not underestimate, what a later valid collection can pull.

## Existing Defenses Found

- Unauthorized callers cannot collect for a data service.
- A data service with no provider stake cannot siphon funds.
- Over-large requests are capped, with optional slippage protection.
- Zero-token collections cannot bypass the minimum collection window.
- Pending update max-claim envelope tests cover under-reservation risk.
- Callback returndata is bounded to reduce return-data griefing.

## First Things To Hunt

- Agreement-manager escrow reservation around `getMaxNextClaim`.
- Term updates that retroactively change rate or max window.
- Payer cancellation and final-collection edge cases.
- Callback conditions that change after acceptance.
- Pause behavior across collector, escrow, and agreement-manager flows.

## Next Step

Map `RecurringAgreementManager`, because it uses `getMaxNextClaim` to decide whether an agreement is safely funded.
