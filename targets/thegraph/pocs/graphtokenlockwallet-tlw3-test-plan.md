# GraphTokenLockWallet TLW3 Test Plan

## Question

Do removed token destinations keep existing wallet allowances?

## Why It Matters

`approveProtocol` approves all current manager destinations, but `revokeProtocol` only revokes destinations currently returned by the manager.

## Command

```powershell
node targets/thegraph/pocs/graphtokenlockwallet-tlw3-harness.js
```

## Result

Confirmed locally in the model and Hardhat.

If a destination is removed from the manager before a wallet calls `revokeProtocol`, that removed destination may keep its old allowance.

The stronger local test uses `TokenPullerMock` to show that a removed destination with a callable pull path can still transfer wallet tokens after removal.

## Hardhat Command

```powershell
cd external/thegraph-contracts/packages/token-distribution
pnpm exec hardhat test test/tokenLockWallet.test.ts --grep "keeps allowance"
pnpm exec hardhat test test/tokenLockWallet.test.ts --grep "removed destinations can still pull"
```

## Candidate Severity

Potentially higher than TLW1 if a real removed destination can still pull funds from wallets after governance intended to deauthorize it.

This is not submission-ready until we connect the local primitive to a real in-scope destination, deployment history, or deauthorization scenario.

## Next Step

Check real manager destination history and transfer-tool/staking pull paths to see whether stale allowance can affect actual in-scope wallets.
