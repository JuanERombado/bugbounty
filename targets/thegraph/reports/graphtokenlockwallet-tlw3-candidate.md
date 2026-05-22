# Candidate Report: Removed Token Destinations Retain Wallet Spending Power

Status: not submission-ready.

## Summary

`GraphTokenLockWallet.approveProtocol()` grants unlimited GRT allowance to every token destination currently listed by `GraphTokenLockManager`, but `revokeProtocol()` only clears destinations still listed at revoke time.

## Local Impact

If a destination is removed from the manager before a wallet revokes protocol access, the removed destination can retain `MaxUint256` allowance from that wallet.

A local test-only destination with a callable `transferFrom` path can still pull tokens from the wallet after removal.

## Affected Code

- `GraphTokenLockWallet.approveProtocol()`
- `GraphTokenLockWallet.revokeProtocol()`
- `GraphTokenLockManager.removeTokenDestination()`

## Local Reproduction

```powershell
cd external/thegraph-contracts/packages/token-distribution
pnpm exec hardhat test test/tokenLockWallet.test.ts --grep "removed destinations can still pull"
```

## Evidence

- Added local mock: `external/thegraph-contracts/packages/token-distribution/contracts/tests/TokenPullerMock.sol`
- Added local test: `external/thegraph-contracts/packages/token-distribution/test/tokenLockWallet.test.ts`

## Missing Before Submission

- Identify a real in-scope destination that was removed, deprecated, upgradeable, compromised, or otherwise intended to be deauthorized.
- Show that the real destination exposes a callable path that can spend the stale wallet allowance.
- Estimate affected wallet funds and whether beneficiary action is required.

## Current Severity Guess

Unknown; likely informational/low without a real destination path, potentially higher if a removed destination can still pull locked funds contrary to governance intent.

## Next Step

Map real token destinations and authorized transfer/staking tool addresses, then check whether any removed or deprecated destination has a callable pull path.
