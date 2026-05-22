# BillingConnector Summary

## Plain-English Purpose

`BillingConnector` is an L1 helper that moves user GRT into the L2 Billing contract and sends L1-to-L2 messages for L2 balance removals.

## Source Used

- Verified source extracted from Etherscan for `0x8017B9AF3F199CC6b08A48DA3859410F20bbea72`.
- Local copy: `targets/thegraph/code-map/billingconnector-source/contracts/BillingConnector.sol`.

## Value Movement

- `addToL2` pulls GRT from `msg.sender` into the connector, approves the L1 token gateway, then calls `outboundTransfer` to bridge the same amount to `l2Billing`.
- `addToL2WithPermit` first proves the caller is the token owner, then uses `permit` or existing allowance before calling the same bridge path.
- `removeOnL2` does not move L1 GRT; it sends a retryable ticket asking L2 Billing to remove `_amount` from `msg.sender` and send it to `_to`.
- `rescueTokens` lets the governor transfer ERC20 tokens held by the connector.

## Role Checks

- Only the governor can change `l1TokenGateway`, `l2Billing`, `inbox`, or call `rescueTokens`.
- Ownership transfer is two-step: governor nominates a pending governor, then the pending governor accepts.
- `addToL2` is public but can only move the caller's approved tokens.
- `addToL2WithPermit` requires `_user == msg.sender`, so a third party cannot use someone else's permit through this function.
- `removeOnL2` is public and intentionally sends an L2 action on behalf of `msg.sender`.

## Bridge And Accounting Invariants

- A successful `addToL2` should never leave user GRT in the connector.
- The amount pulled from the user should equal the amount approved to the gateway and bridged to L2.
- The L2 credit destination is encoded as callhook data, while the token bridge recipient is always `l2Billing`.
- A removal request should always encode `msg.sender` as the L2 balance owner.
- Governance setters must not accept zero addresses.
- The connector should not retain stale gateway allowance after a successful bridge.

## First Things To Hunt

- Non-standard ERC20 behavior because `transferFrom` and `approve` return values are not checked.
- Retryable-ticket failure or underfunding that could emit success-looking events without L2 execution.
- `removeOnL2` authorization assumptions between L1 `msg.sender` and L2 Billing's `removeFromL1`.
- Governor rescue of GRT if bridge transfer fails after token pull.
- Destination/refund edge cases caused by using `_to` as the retryable ticket refund address.

## Next Step

Pick the easiest local-only hypothesis: test whether a token that returns `false` from `transferFrom` or `approve` can make `addToL2` continue anyway.
