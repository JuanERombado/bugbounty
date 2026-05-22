# Test Plan: SubgraphService Zero Payment Destination

## Goal

Confirm whether indexing-fee proceeds are handled safely when an indexer has not set `paymentsDestination`.

## Why This Test First

It is a small value-routing question with a clear pass/fail result.

## Local-Only Setup

Use the existing Foundry indexing-agreement test helpers under `external/thegraph-contracts/packages/subgraph-service/test/unit/subgraphService/indexing-agreement`.

## Steps

1. Create a normal indexer and accepted indexing agreement.
2. Do not call `subgraphService.setPaymentsDestination(indexerState.addr)`.
3. Ensure the payer has escrow and the agreement is collectable.
4. Collect `IGraphPayments.PaymentTypes.IndexingFee`.
5. Assert whether indexer proceeds go to a documented default, remain safely accounted, or are sent to `address(0)`.
6. If zero destination reverts, confirm whether that creates a realistic lock or only a setup error.

## Expected Safe Outcomes

- Zero destination maps to a documented safe default.
- The collect call reverts before any value movement.
- Funds remain recoverable and correctly accounted.

## Suspicious Outcomes

- Indexing-fee proceeds are burned or stranded.
- Collection succeeds but value cannot be recovered by the intended indexer.
- A payer can be charged while the service provider receives nothing due to unset destination.

## Suggested Foundry Test Name

`test_SubgraphService_CollectIndexingFees_ZeroPaymentDestination_IsSafe`

## Next Step

Inspect RecurringCollector and GraphPayments destination logic, then write the test in `collect.t.sol`.
