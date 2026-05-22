# L1GNS Summary

## Plain-English Purpose

`L1GNS` is the L1 Graph Name System contract plus migration helpers for sending subgraphs and curator balances to L2.

## Value Movement

- `sendSubgraphToL2` burns the subgraph's L1 curation signal, sends the owner's proportional GRT to L2, and leaves the rest as withdrawable L1 GRT for other curators.
- `sendCuratorBalanceToBeneficiaryOnL2` sends a non-owner curator's remaining withdrawable L1 balance to an L2 beneficiary.
- `_sendTokensAndMessageToL2GNS` approves the L1 gateway and sends GRT plus callhook data to the L2 GNS.
- Normal `GNS` flows still include publishing, minting signal, burning signal, deprecating subgraphs, withdrawing from deprecated subgraphs, and charging owner tax on upgrades.

## Role Checks

- Only the current subgraph owner can call `sendSubgraphToL2`.
- Only curators with remaining signal can call `sendCuratorBalanceToBeneficiaryOnL2`.
- Both L2 transfer functions are blocked while partial pause is active.
- `sendSubgraphToL2` rejects a second transfer with `ALREADY_DONE`.
- L2 `onTokenTransfer` only accepts calls from the configured L2 token gateway and only when the bridged L1 sender is the counterpart L1 GNS.

## Accounting Invariants

- Owner L2 tokens should equal `ownerNSignal * curationTokens / totalSignal`.
- Non-owner L1 withdrawable GRT should equal `curationTokens - ownerTokensForL2`.
- After a subgraph is sent to L2, owner signal is zeroed, the subgraph is disabled, and the NFT is burned.
- Curator balance transfers should reduce that curator's L1 signal and reduce `withdrawableGRT` by the exact amount sent to L2.
- If an L2 curator balance message arrives before the L2 subgraph transfer is finished, L2 returns tokens to the beneficiary instead of minting signal.

## First Things To Hunt

- Retryable-ticket expiration after L1 state is finalized.
- Division-by-zero or zero-signal paths in `sendSubgraphToL2`.
- Rounding dust in owner/non-owner split during L1-to-L2 transfer.
- Ordering problems between L2 subgraph receipt, finish, curator balance receipt, and deprecation.
- Owner-tax and curation-tax edge cases during version updates before migration.

## Next Step

Start with GNS1: test what happens when the owner tries to send an active but uncurated subgraph to L2.
