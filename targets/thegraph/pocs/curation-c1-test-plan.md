# Curation C1 Test Plan

## Hypothesis

Multiple curators plus collected fees might leave unclaimable GRT or signal dust after everyone exits.

## Local Test Shape

1. Mint GRT to a second curator and approve `Curation`.
2. Have two curators mint signal into the same deployment pool.
3. Configure the local staking mock and collect query-fee rewards into the pool.
4. Have each curator burn their full signal.
5. Assert final pool tokens and pool signal are zero.

## Expected Safe Result

All pool value is claimable and the final burn clears pool tokens and signal.

## Vulnerable Result

Pool tokens or signal remain after all curators burn their full balances.

## Test Result

- Test added: `clears pool tokens and signal when multiple curators exit after fees are collected`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/curation/curation.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/curation/curation.test.ts --grep "clears pool tokens"`
- Result: `1 passing`
- Finding status: rejected.

## What We Learned

Two curators can mint, receive collected-fee upside, fully exit, and leave no pool tokens or signal behind.

## Next Step

Test stale quote/slippage behavior after another curator changes the pool.
