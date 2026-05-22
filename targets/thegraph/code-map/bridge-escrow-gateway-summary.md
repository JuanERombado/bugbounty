# BridgeEscrow And L1GraphTokenGateway Summary

## Plain-English Purpose

`BridgeEscrow` holds L1 GRT for the Arbitrum bridge, and `L1GraphTokenGateway` moves GRT into escrow for L1-to-L2 deposits or releases/mints GRT for L2-to-L1 withdrawals.

## Value Movement

- L1-to-L2 deposit: `outboundTransfer` pulls GRT from the L1 sender into `BridgeEscrow`, then asks Arbitrum Inbox to create the L2 retryable message.
- L2-to-L1 withdrawal: `finalizeInboundTransfer` releases GRT from `BridgeEscrow` to the L1 recipient.
- If a withdrawal amount exceeds escrow balance, the gateway mints the shortfall to escrow before transferring to the recipient.
- `BridgeEscrow` itself does not decide recipients; it only gives approved spenders unlimited GRT allowance.

## Role Checks

- `BridgeEscrow.approveAll` and `BridgeEscrow.revokeAll` are governor-only.
- `L1GraphTokenGateway` setup functions are governor-only.
- `finalizeInboundTransfer` only accepts calls from the Arbitrum bridge when the active outbox reports the configured L2 gateway as sender.
- Callhook data is only allowed when `msg.sender` is on the gateway callhook allowlist.
- The router cannot be callhook-allowlisted.

## Bridge Accounting

- Deposits increase escrow balance.
- Withdrawals decrease escrow balance.
- If withdrawals exceed escrow, minting is capped by `accumulatedL2MintAllowanceAtBlock(block.number) - totalMintedFromL2`.
- `totalMintedFromL2` only increases when the L1 gateway mints due to insufficient escrow.

## Important Invariants

- Only the configured gateway should be able to spend from `BridgeEscrow`.
- L2-originated withdrawals must only be accepted from the configured L2 gateway through the Arbitrum bridge/outbox path.
- Minted L1 GRT must never exceed the configured L2 mint allowance.
- Failed deposits should not leave the user with GRT moved to escrow but no retryable ticket.
- Non-allowlisted users and the router should not be able to attach arbitrary callhook data.

## First Things To Hunt

- Atomicity between escrow transfer and retryable ticket creation.
- Mint allowance boundary conditions across block updates.
- Router/from parsing and callhook allowlist bypasses.
- Escrow allowance changes and spender assumptions.
- Withdrawal behavior when escrow has partial balance and minting covers only the shortfall.
