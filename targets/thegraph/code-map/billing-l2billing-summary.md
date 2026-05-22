# L2 Billing Summary

## Plain-English Purpose

`Billing` is the L2 contract that holds user billing balances, receives bridged GRT, lets users withdraw, and lets approved collectors pull spent balances.

## Source Used

- Verified Arbiscan source for `0x1B07D3344188908Fb6DEcEac381f3eE63C48477a`.
- Source reference: `https://arbiscan.io/address/0x1B07D3344188908Fb6DEcEac381f3eE63C48477a`.

## Value Movement

- `onTokenTransfer` credits a user balance when the L2 gateway receives bridged GRT from the configured L1 BillingConnector.
- `remove` debits the caller's balance and transfers GRT to `_to`.
- `removeFromL1` debits `_from` and transfers GRT to `_to`, but only when called through the L1 connector alias.
- `pull` and `pullMany` let approved collectors debit user balances and send collected GRT to a destination.
- `rescueTokens` lets the governor rescue ERC20 tokens from the contract.

## Role Checks

- Only the governor can set collectors, the L2 token gateway, and the L1 BillingConnector.
- Only the configured L2 token gateway can call `onTokenTransfer`.
- `onTokenTransfer` also requires the L1 sender to equal the configured L1 BillingConnector.
- Only the L2 alias of the configured L1 BillingConnector can call `removeFromL1`.
- Only collectors can call `pull` and `pullMany`.

## Accounting Invariants

- `userBalances[user]` should increase only when tokens actually arrive or are pulled from a local depositor.
- Withdrawals should reduce the exact user's balance before sending tokens.
- Collector pulls should debit at most the user's available balance.
- Failed L1 removal due to insufficient balance should not debit or transfer tokens.
- The L1 connector address must be stored unaliased, because the check applies Arbitrum's alias helper at call time.

## BC3 Source-Review Result

BC3 is weakened by the source review: `removeFromL1` is not open to arbitrary callers because it requires `msg.sender == AddressAliasHelper.applyL1ToL2Alias(l1BillingConnector)`.

The remaining question is not "can anyone call removeFromL1," but "can retryable-ticket parameters or refund handling cause a user-facing loss or stuck state."

## Next Step

Move to BC2 and model retryable-ticket failure/underfunding expectations.
