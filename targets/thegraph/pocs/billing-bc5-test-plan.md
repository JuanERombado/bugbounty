# Billing BC5 Test Plan

## Question

Can `addToL2WithPermit` move tokens after an invalid permit?

## Why It Matters

Users may assume an invalid or expired permit stops the call, but the source intentionally falls back to existing allowance.

## Expected Safe Behavior

The fallback may proceed only when the caller is the token owner and allowance already exists.

## Command

```powershell
node targets/thegraph/pocs/billing-bc5-harness.js
```

## Result

Rejected as a candidate.

The invalid-permit fallback is real, but `_user == msg.sender` prevents third-party use and the behavior is explicitly documented in the source.

## Next Step

Close the BillingConnector pass and choose the next ranked target.
