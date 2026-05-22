# Billing BC4 Test Plan

## Question

Can GRT become stranded in `BillingConnector` if the gateway reverts after `transferFrom`?

## Why It Matters

The connector pulls user tokens before calling the gateway, so we need to know whether a later failure leaves funds behind.

## Expected Safe Behavior

If the gateway reverts, the whole transaction reverts and the earlier token transfer and approval roll back.

## Local Model

The harness snapshots token balances and allowances before `addToL2`, then restores them if the gateway throws.

## Command

```powershell
node targets/thegraph/pocs/billing-bc4-harness.js
```

## Result

Rejected as framed.

With normal ERC20 and EVM rollback semantics, a reverting gateway does not strand GRT in the connector.

## Next Step

Check BC5, the permit fallback behavior, because it is the last BillingConnector-specific hypothesis.
