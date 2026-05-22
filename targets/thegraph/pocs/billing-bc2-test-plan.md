# Billing BC2 Test Plan

## Question

Can a BillingConnector call succeed on L1 while the intended L2 Billing effect does not happen?

## Why It Matters

Bridge flows often have two success moments: L1 message creation and later L2 execution.

## Source-Review Notes

- `addToL2` calls the L1 token gateway, which creates the bridged token transfer and callhook delivery to L2 Billing.
- `removeOnL2` calls `Inbox.createRetryableTicket` and emits `RemovalRequestSentToL2` after ticket creation.
- L2 Billing's `removeFromL1` intentionally succeeds with `InsufficientBalanceForRemoval` instead of reverting when the user lacks enough balance.
- The connector only requires `_maxSubmissionCost != 0` on `removeOnL2`; deeper fee validation is left to Arbitrum's inbox.

## Expected Bridge Behavior

An L1 transaction can successfully create a retryable ticket even though the later L2 execution may fail or need manual retry.

## Candidate-Bug Behavior

It becomes reportable only if the contract causes user funds to be permanently stuck, miscredited, or silently transferred to the wrong party beyond normal retryable-ticket semantics.

## Minimal Local Model

Mock the inbox so it accepts a retryable ticket but records no L2 state change, then verify the connector emits a request event without any local proof of L2 execution.

## Current Status

Rejected as a standalone candidate.

The local model confirms L1 request success is separate from L2 execution, but that is expected retryable-ticket behavior and does not by itself show unauthorized debit, wrong-recipient transfer, or permanent stuck funds.

## Command

```powershell
node targets/thegraph/pocs/billing-bc2-harness.js
```

## Next Step

Move to BC4 and check whether a reverting gateway can strand GRT in the connector.
