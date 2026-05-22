# Billing BC3 Test Plan

## Question

Can arbitrary callers use `removeOnL2` / `removeFromL1` to remove another user's L2 billing balance?

## Source-Review Result

Rejected as currently framed.

`removeOnL2` is public on L1, but it encodes `msg.sender` as `_from`; on L2, `removeFromL1` can only be called by the Arbitrum L2 alias of the configured L1 BillingConnector.

## Evidence

- L1 connector encodes `IBilling.removeFromL1.selector, msg.sender, _to, _amount`.
- L2 Billing requires `msg.sender == AddressAliasHelper.applyL1ToL2Alias(l1BillingConnector)`.
- L2 Billing debits `userBalances[_from]`, not an arbitrary supplied owner chosen by a third-party caller.

## Remaining Risk

If the L2 retryable ticket fails, the L1 transaction may still have looked successful to the caller, but that is a retryable-delivery question rather than an arbitrary-removal bug.

## Next Step

Move to BC2: model underfunded or failed retryable tickets and decide whether the behavior is expected bridge semantics or a reportable user-fund risk.
