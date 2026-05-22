# BillingConnector Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`.

## BC1: False-Returning Token Calls Can Make `addToL2` Continue Without Real Token Movement

- Status: rejected
- Asset: BillingConnector
- Hypothesis: because `_addToL2` does not check the boolean return values of `graphToken.transferFrom` or `graphToken.approve`, a false-returning token could make the function continue after a failed transfer or approval.
- Why it might matter: the contract could emit `TokensSentToL2` or call the gateway even though the connector did not actually receive or approve tokens.
- Impact if true: accounting mismatch or misleading bridge action.
- Scope caution: The real Graph Token behavior must be checked before treating this as a bounty candidate.
- Minimal local test idea: deploy a mock token that returns `false` without moving balances, call `addToL2`, and verify whether the gateway call still happens.
- Evidence that rejects it: the actual `GraphToken` inherits OpenZeppelin ERC20, whose `transferFrom` and `approve` return `true` after successful state changes and revert on failure.
- Result: the local model confirmed the generic integration smell, but the real target token does not appear to expose the false-returning behavior needed for impact.
- Rejection reason: this is useful learning, but not currently a The Graph bounty candidate.

## BC2: Retryable Ticket Underfunding Can Create A Local Success But Failed L2 Effect

- Status: rejected
- Asset: BillingConnector
- Hypothesis: `addToL2` or `removeOnL2` may succeed on L1 while the L2 retryable ticket later fails, leaving user expectations or accounting out of sync.
- Why it might matter: bridge connectors often split "L1 transaction succeeded" from "L2 effect actually happened."
- Impact if true: lost access to billing funds or failed withdrawals.
- Scope caution: failed retryables can be expected Arbitrum behavior unless the contract promises stronger guarantees.
- Minimal local test idea: mock the gateway/inbox to accept underfunded parameters and verify whether the connector has any local recovery or clear failure signal.
- Current evidence: source review shows `removeOnL2` emits after retryable ticket creation, while L2 Billing can later emit `InsufficientBalanceForRemoval` without changing balances.
- Result: the local model confirms L1 request success is separate from L2 execution, but no unauthorized debit, wrong-recipient transfer, or permanent stuck-funds path appears.
- Rejection reason: this is normal retryable-ticket behavior unless paired with a concrete fund-loss condition.

## BC3: `removeOnL2` May Let A Caller Request L2 Removal Without L1 Proof Of L2 Balance

- Status: rejected
- Asset: BillingConnector / L2 Billing
- Hypothesis: any L1 caller can send a removal message, and safety depends entirely on L2 Billing checking that `msg.sender` owns enough L2 balance.
- Why it might matter: this is a cross-chain authorization boundary.
- Impact if true: unauthorized L2 balance removal.
- Scope caution: this probably belongs in the L2 Billing contract, not just the L1 connector.
- Minimal local test idea: inspect or model `IBilling.removeFromL1` behavior and confirm only the real L1 connector alias can call it and debit the encoded owner.
- Evidence that rejects it: verified L2 Billing source uses `onlyL1BillingConnector`, which requires the Arbitrum L2 alias of the configured L1 BillingConnector, and `removeOnL2` encodes L1 `msg.sender` as the debited `_from`.
- Result: arbitrary callers can request removal only for their own encoded sender identity; L2 authorization is anchored to the connector alias.
- Rejection reason: as framed, this is not an arbitrary-removal path.

## BC4: Governor Rescue Can Pull GRT If Tokens Become Stranded In The Connector

- Status: rejected
- Asset: BillingConnector
- Hypothesis: if a bridge call fails after GRT is transferred into the connector, governor `rescueTokens` can move those stranded GRT.
- Why it might matter: user funds could depend on governance action for recovery.
- Impact if true: temporary fund lock or privileged recovery path.
- Scope caution: this is likely intended emergency behavior unless an unprivileged path can strand funds.
- Minimal local test idea: mock the gateway to revert after `transferFrom` and confirm the whole transaction reverts, leaving no stranded GRT.
- Result: local transaction model confirms a reverting gateway rolls back the earlier token pull and approval.
- Rejection reason: with normal ERC20 and EVM rollback semantics, this path does not strand user GRT.

## BC5: Permit Fallback May Consume Existing Allowance When The Signature Fails

- Status: rejected
- Asset: BillingConnector
- Hypothesis: if `permit` fails but allowance already exists, `addToL2WithPermit` proceeds without a valid signature.
- Why it might matter: users may assume a bad or expired permit prevents movement.
- Impact if true: surprising token movement with prior allowance.
- Scope caution: this behavior is explicitly commented and `_user == msg.sender`, so it is likely intended and low severity.
- Minimal local test idea: set allowance, pass an invalid permit, and verify the call succeeds only for the token owner.
- Result: local model confirms invalid permit can fall back to existing allowance, but only when `_user == msg.sender`.
- Rejection reason: behavior is documented, self-only, and not a third-party token movement path.

## Picked First Test

BC1 was checked first because it needed only local mocks and tested a direct value-movement invariant.

## Next Step

BillingConnector pass result: all five starter hypotheses are rejected or documented behavior, with local-only evidence.

Next best target: `L1GNS`, because it is adjacent in the ranked map and has publication, curation, and cross-chain transition behavior.
