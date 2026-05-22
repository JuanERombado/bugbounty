# Test Plan: SubgraphService Entity Fee Overflow

## Goal

Check whether a valid indexing agreement can become uncollectable because SubgraphService overflows before RecurringCollector caps payout.

## Why This Matters

RecurringCollector caps payouts, but SubgraphService computes the requested amount first.

## Local-Only Setup

Use the existing indexing-agreement Foundry helpers and do not interact with any deployment.

## Steps

1. Accept a normal indexing agreement.
2. Update the agreement to set `tokensPerSecond = 0` and a very large `tokensPerEntityPerSecond`.
3. Make the agreement collectable by advancing time.
4. Collect with a very large `entities` value.
5. Observe whether `_tokensToCollect` overflows before RecurringCollector can cap the payout.
6. If it overflows, reduce values until the smallest reproducible valid agreement is found.
7. If it cannot overflow under valid RCA/RCAU constraints, reject the hypothesis.

## Expected Safe Outcome

The protocol rejects dangerous terms before acceptance/update or safely caps collection without a pre-cap overflow.

## Suspicious Outcome

A payer-signed or update-signed agreement can be accepted, then normal collection permanently reverts because pre-cap arithmetic overflows.

## Suggested Foundry Test Name

`test_SubgraphService_CollectIndexingFees_Reverts_WhenEntityFeeRequestOverflowsBeforeCap`

## Current Status

The starter regression test has been added to `external/thegraph-contracts/packages/subgraph-service/test/unit/subgraphService/indexing-agreement/collect.t.sol`.

The arithmetic simulator `scripts/simulate-subgraphservice-entity-fee-overflow.js` confirms that SubgraphService can overflow before RecurringCollector's cap would apply.

The regression test also tries a zero-entity collection after the overflow attempt to check whether basic liveness can recover.

## Duplicate-Risk Check

- No local known-bug entry found for `tokensPerEntityPerSecond`, `_tokensToCollect` overflow, or entity-fee overflow.
- A relevant design note says the cap fix is intended to avoid stuck agreements, which makes this worth testing as a possible regression.
- This is not related to the RAM duplicate path.

## Severity Caution

This is probably not critical because extreme terms must be signed/accepted, but it may still matter if accepted terms can make honest collection unrecoverable.

## Next Step

Run the Foundry test once `forge` is available, then classify whether this is permanent payment blockage, recoverable zero-value liveness only, or unrealistic signed input.
