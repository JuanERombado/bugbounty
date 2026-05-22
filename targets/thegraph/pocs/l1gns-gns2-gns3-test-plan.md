# L1GNS GNS2/GNS3 Test Plan

## Question

What happens if L1GNS finalizes a subgraph or curator transfer but the L2 retryable never completes?

## Why This Matters

This is the real cross-chain risk: L1 state is changed before L2 completion is guaranteed.

## Local Model

The harness models owner migration and curator migration where the L1 send succeeds but L2 execution never occurs.

## Command

```powershell
node targets/thegraph/pocs/l1gns-gns2-gns3-harness.js
```

## Result

Rejected as standalone candidates.

The model confirms L1 state is finalized before L2 completion, but the source comments explicitly warn about retryable redemption risk and this appears to be expected Arbitrum bridge behavior.

## What Would Make This Reportable

A reportable path would need show that an honest user can lose funds or ownership despite using valid parameters, or that another actor can force expiry/failure.

## Next Step

Move to GNS4 and test whether rounding dust in owner/curator split can accumulate or strand value.
