# BridgeEscrow And L1GraphTokenGateway Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`.

## B1: Deposit Can Move GRT Into Escrow Without Creating A Valid L2 Ticket

- Status: rejected
- Asset: L1GraphTokenGateway / BridgeEscrow
- Hypothesis: a failure after `token.transferFrom(from, escrow, amount)` could leave GRT in escrow without a usable L2 retryable ticket.
- Why it might matter: direct user funds could become stuck in escrow.
- Impact if true: potential direct loss or permanent lock of bridged user funds.
- Minimal local test idea: make the mocked Inbox/retryable creation fail after token transfer and assert the whole transaction reverts atomically.
- Evidence that rejects it: EVM revert rolls back both the token transfer and gateway state.
- Result: targeted local test passed; when the configured inbox cannot create a retryable ticket, `outboundTransfer` reverts and both sender and escrow GRT balances remain unchanged.
- Rejection reason: the token transfer and retryable creation are atomic inside the same transaction.

## B2: Router Data Can Spoof `from` Or Attach Callhook Data

- Status: rejected
- Asset: L1GraphTokenGateway
- Hypothesis: the router path decodes `from` from calldata, so malformed or malicious router data could move tokens from an unintended approved address or attach callhook data.
- Why it might matter: this touches impersonation and unwanted user actions.
- Impact if true: user funds could be bridged or callhooks executed without the intended user action.
- Out-of-scope risk: if it requires a malicious Arbitrum router, it may be considered third-party or privileged.
- Minimal local test idea: call as router with non-empty callhook data and confirm the gateway rejects it because the router cannot be allowlisted.
- Evidence that rejects it: router callhook data always reverts with `CALL_HOOK_DATA_NOT_ALLOWED`.
- Result: targeted local test passed; router-style calldata with non-empty callhook bytes reverts and sender/escrow balances remain unchanged.
- Rejection reason: the callhook allowlist check keys off `msg.sender`, and the configured router is not allowlisted.

## B3: Mint Allowance Boundary Can Be Double-Counted Around Updates

- Status: rejected
- Asset: L1GraphTokenGateway
- Hypothesis: `updateL2MintAllowance` or manual allowance parameters could double-count block ranges and allow more L1 GRT to be minted than intended.
- Why it might matter: bridge minting is a high-value accounting boundary.
- Impact if true: inflation or excess withdrawals from L2-to-L1 messages.
- Out-of-scope risk: purely bad governor input is privileged and likely excluded.
- Minimal local test idea: simulate allowance updates across block boundaries and try to finalize withdrawals just above the computed allowance.
- Evidence that rejects it: total minted remains bounded by `accumulatedL2MintAllowanceAtBlock`.
- Result: targeted local test passed; after one withdrawal consumes mint allowance, a second withdrawal above the newly remaining allowance reverts with `INVALID_L2_MINT_AMOUNT`.
- Rejection reason: `totalMintedFromL2` is counted against accumulated allowance and prevents reuse.

## B4: Partial Escrow Plus Mint Shortfall Can Transfer More Than Intended

- Status: rejected
- Asset: L1GraphTokenGateway / BridgeEscrow
- Hypothesis: when escrow has some GRT and the gateway mints only the shortfall, accounting might release more total value than allowed.
- Why it might matter: mixed escrowed and newly minted balances are a classic bridge accounting edge.
- Impact if true: direct fund loss or unauthorized token inflation.
- Minimal local test idea: deposit a small amount, set mint allowance for the shortfall, withdraw escrow plus shortfall, and assert balances and `totalMintedFromL2`.
- Evidence that rejects it: only the shortfall is minted and total recipient balance equals the requested withdrawal.
- Result: existing and added local tests confirm only the shortfall is minted, escrow is consumed, and excess follow-up withdrawal attempts are blocked.
- Rejection reason: mixed escrow-plus-mint accounting preserves the expected balance and mint counters.

## B5: Escrow Approval Can Remain Live For A Retired Gateway

- Status: new
- Asset: BridgeEscrow
- Hypothesis: if a gateway is replaced without revoking the old allowance, the old spender can still drain escrow.
- Why it might matter: unlimited allowances are powerful and easy to forget during upgrades.
- Impact if true: direct loss of escrowed GRT.
- Out-of-scope risk: this may be operational/governance configuration rather than a code bug.
- Minimal local test idea: approve two spenders, revoke only one, and show the other keeps access.
- Evidence that rejects it: expected governor-controlled allowance behavior; not a contract vulnerability by itself.

## Picked First Test

B1 was tested first because it asks the most important bridge question in the simplest way: if retryable creation fails, does the escrow transfer roll back too?

Next best test: B3/B4, because mint allowance and partial escrow withdrawal accounting are the highest-value bridge accounting boundaries left in this pass.
