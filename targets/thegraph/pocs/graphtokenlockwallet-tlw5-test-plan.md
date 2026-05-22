# GraphTokenLockWallet TLW5 Test Plan

## Question

Does beneficiary acceptance freeze the wallet manager?

## Why It Matters

The manager controls which protocol destinations receive token allowance and which fallback calls the beneficiary can forward.

## Result

Confirmed behavior: after `acceptLock()`, the owner can still call `setManager()`.

After the manager is changed, future `approveProtocol()` approvals and fallback authorization use the new manager.

## Hardhat Command

```powershell
cd external/thegraph-contracts/packages/token-distribution
pnpm exec hardhat test test/tokenLockWallet.test.ts --grep "can change manager after beneficiary accepts lock"
```

## Candidate Severity

Likely low or intended-admin behavior unless acceptance is documented or understood to freeze all owner-controlled trust assumptions.

## Next Step

Run all GraphTokenLockWallet focused tests together, then move to the next high-value asset.
