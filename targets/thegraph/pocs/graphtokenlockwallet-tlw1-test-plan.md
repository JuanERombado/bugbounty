# GraphTokenLockWallet TLW1 Test Plan

## Question

Can uneven schedule math make `release` treat surplus as scheduled tokens?

## Why This Is First

Release math is direct custody accounting, and the contract uses integer division in both time periods and token amounts.

## Local Model

Use a simple arithmetic harness that mirrors `availableAmount`, `releasableAmount`, and `release`.

## Expected Safe Behavior

`releasedAmount` should never exceed `managedAmount`.

## Candidate-Bug Behavior

If `releasedAmount` can exceed `managedAmount`, later outstanding or surplus accounting can underflow or misclassify funds.

## Next Step

Run the harness and decide whether the issue is only self-inflicted surplus release or worth porting into Hardhat.

## Command

```powershell
node targets/thegraph/pocs/graphtokenlockwallet-tlw1-harness.js
cd external/thegraph-contracts/packages/token-distribution
pnpm exec hardhat test test/tokenLock.test.ts --grep "edge schedules"
```

## Result

Confirmed locally, likely low severity.

The Hardhat test confirms that exact-`endTime` release with uneven period duration can emit `TokensReleased` for `managedAmount + surplusAmount`, set `releasedAmount` above `managedAmount`, and make `totalOutstandingAmount()` revert.

## Next Step

Check whether this can trap funds or affect any real in-scope deployed schedule; otherwise keep it as a low-severity learning find and move to TLW3.
