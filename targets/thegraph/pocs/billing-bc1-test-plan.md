# Billing BC1 Test Plan

## Question

Does `BillingConnector.addToL2` continue when the token's `transferFrom` or `approve` returns `false`?

## Why This Is First

This is the smallest local-only check for a direct value-movement invariant.

## Local-Only Setup

- Contract under test: `targets/thegraph/code-map/billingconnector-source/contracts/BillingConnector.sol`
- Mock token: returns `false` from `transferFrom` or `approve` without reverting.
- Mock gateway: records whether `outboundTransfer` was called and with what amount.

## Expected Safe Behavior

If token transfer or approval fails, `addToL2` should revert before calling the gateway or emitting a success-looking event.

## Candidate-Bug Behavior

If the token returns `false` and the connector continues, the gateway can be called even though token movement or approval failed.

## Important Scope Check

Before escalating, confirm whether the actual Graph Token can ever return `false` instead of reverting.

## Command

```powershell
node targets/thegraph/pocs/billing-bc1-harness.js
```

## Result

Model confirms the connector's call sequence continues after a false-returning `transferFrom` or `approve`.

Rejected for The Graph because the real `GraphToken` inherits OpenZeppelin ERC20, whose `transferFrom` and `approve` return `true` after success and revert on failure.

## Next Step

Inspect the L2 Billing side of `removeFromL1`, because that is the actual cross-chain authorization boundary.
