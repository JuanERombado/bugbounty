# RAM1 Test Plan: Exact-Deficit JIT Top-Up

## Goal

Prove whether `RecurringAgreementManager.beforeCollection` skips a needed top-up when the manager has exactly the missing escrow amount.

## Setup

1. Create or reuse a managed recurring agreement.
2. Set the escrow account balance to `X`.
3. Set the manager's free GRT balance to `Y`.
4. Call `beforeCollection(agreementId, X + Y)` as the collector.

## Expected Safe Behavior

The manager deposits exactly `Y`, so escrow balance becomes `X + Y`.

## Suspected Current Behavior

The manager deposits nothing because `deficit < managerBalance` is false when `deficit == managerBalance`.

## Why This Matters

The following `PaymentsEscrow.collect` may fail even though the manager held exactly enough GRT to fund the payment.

## Current Verification

The local JavaScript model confirms the branch boundary, but the full Solidity test is still pending because `forge` is not installed in this environment.

## Command

```powershell
node targets/thegraph/pocs/recurringagreementmanager-ram1-harness.js
```

## Next Step

Add a Foundry test under `packages/issuance/test/unit/agreement-manager/afterCollection.t.sol` or a new focused test file, then run it when Foundry is available.
