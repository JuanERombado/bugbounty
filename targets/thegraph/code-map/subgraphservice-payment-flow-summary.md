# SubgraphService Indexing-Fee Payment Flow

## Scope

This map covers the local-only SubgraphService indexing-fee path, not live deployments.

## Plain-English Flow

1. An indexer or authorized operator calls `SubgraphService.collect(indexer, IndexingFee, data)`.
2. `SubgraphService` checks that the indexer has a valid provision and is registered before dispatching the payment type.
3. For indexing fees, `data` is decoded into an `agreementId` and agreement-specific collection metadata.
4. `SubgraphService` passes the request to `IndexingAgreement.collect` with the indexer's configured `paymentsDestination`.
5. `IndexingAgreement.collect` loads the local agreement plus the RecurringCollector agreement state.
6. The agreement's allocation must still exist, be open, and belong to the agreement's service provider.
7. The caller-provided `indexer` must match the allocation owner.
8. RecurringCollector decides whether the agreement is currently collectable and how many seconds can be collected.
9. SubgraphService decodes V1 metadata: `entities`, `poi`, `poiBlockNumber`, `metadata`, and `maxSlippage`.
10. Expected tokens are computed as `collectionSeconds * (tokensPerSecond + tokensPerEntityPerSecond * entities)`.
11. SubgraphService calls RecurringCollector, which is expected to cap actual payout against RCA limits and slippage.
12. The emitted event records the POI data, entities, expected collection context, and actual tokens collected.

## Value Movement

- Payer funds are pulled through RecurringCollector and the Graph Payments flow.
- The data service cut is `indexingFeesCut`.
- The receiver is `paymentsDestination[indexer]`, which is set by the indexer.
- For indexing fees, `GraphPayments.collect` treats a zero receiver destination as a safe default by staking the receiver's share to the service provider.
- For indexing rewards, a zero payment destination restakes to provision in the allocation handler.

## Role Checks

- Collection requires `enforceService(indexer, VALID_PROVISION | REGISTERED)`.
- Agreement acceptance requires the allocation to belong to `rca.serviceProvider`.
- Agreement updates require the indexer to be the agreement service provider.
- Indexer cancellation is an exit path and does not require valid provision or registration.
- Payer cancellation requires the payer or a RecurringCollector-authorized caller.

## Delegation And Allocation Links

- One allocation can have only one active indexing agreement.
- One accepted agreement can intentionally be rebound to a different open allocation for the same subgraph deployment.
- Rebinding clears the old allocation-to-agreement pointer and assigns the new one.
- Closing the old allocation after a rebind should not cancel the agreement.

## Accounting Invariants To Protect

- An allocation should never collect for an agreement owned by another indexer.
- An inactive, canceled, invalid, or uncollectable agreement should not collect.
- The requested token amount should not overflow or bypass RecurringCollector caps.
- A payment destination should not cause value to be burned, stranded, or sent to the wrong party unless explicitly intended.
- Allocation close, resize, and stale-allocation paths should not silently strand accrued fees.

## Current Lead

`tokensPerEntityPerSecond` is not checked against the RCA rate cap, so SubgraphService can compute an overflowing requested amount before RecurringCollector applies its safe cap.

## Duplicate-Risk Notes

- Avoid RAM/RecurringCollector callback gas, malformed ERC165, EIP-7702 payer-code, stale escrow snapshot, and JIT top-up leads already tracked in `targets/thegraph/known-bugs/payments-known-issues.md`.
- Rebinding across allocations is heavily tested and appears intentional, so only pursue it if a concrete accounting invariant breaks.

## Suggested Next Step

Move to entity-based fee math: confirm whether large `tokensPerEntityPerSecond * entities` values can overflow before RecurringCollector caps payout.
