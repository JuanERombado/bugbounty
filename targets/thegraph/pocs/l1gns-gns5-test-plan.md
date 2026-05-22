# L1GNS GNS5 Test Plan

## Question

What happens when a curator balance arrives on L2 before the L2 subgraph transfer is finished?

## Why It Matters

The beneficiary may receive liquid GRT instead of L2 curation signal depending on message ordering.

## Existing Evidence

Existing `l2GNS.test.ts` tests cover these cases:

- if the subgraph does not exist, tokens are returned to the beneficiary;
- if the subgraph is L2-native, tokens are returned to the beneficiary;
- if the L1 subgraph transfer was received but not finished, tokens are returned to the beneficiary;
- if the subgraph was deprecated after transfer, tokens are returned to the beneficiary;
- if the transfer is finished and active, curator signal is minted.

## Result

Rejected as a candidate.

The ordering behavior is intentional, tested, and avoids trapping the curator balance in the L2 GNS.

## Next Step

Close the L1GNS pass and move to `GraphTokenLockWallet`.
