# GraphTokenLockWallet TLW2 Test Plan

## Question

Does the TLW1 over-release make outstanding/surplus accounting revert?

## Result

Confirmed locally as a consequence of TLW1.

After exact-`endTime` over-release, `releasedAmount > managedAmount`, so `totalOutstandingAmount()` reverts with `SafeMath: subtraction overflow`.

## Command

```powershell
cd external/thegraph-contracts/packages/token-distribution
pnpm exec hardhat test test/tokenLock.test.ts --grep "edge schedules"
```

## Next Step

Decide whether any real deployed wallet has uneven schedule parameters and surplus tokens; then assess whether this is only low severity.
