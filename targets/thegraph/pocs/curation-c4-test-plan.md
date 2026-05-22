# Curation C4 Test Plan

## Hypothesis

A curator might receive worse output than quoted if another curator changes the pool before execution.

## Local Test Shape

1. Initialize a curation pool.
2. Quote signal output for a planned mint.
3. Have another curator mint first and change the pool.
4. Try the planned mint using the stale quoted signal as `_signalOutMin`.
5. Assert the transaction reverts with `Slippage protection`.

## Expected Safe Result

The stale quote is rejected because the updated pool would mint less signal than the user's minimum.

## Vulnerable Result

The stale quote succeeds and the user receives less signal than expected.

## Test Result

- Test added: `rejects a stale mint quote after another curator changes the pool`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/curation/curation.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/curation/curation.test.ts --grep "rejects a stale mint quote"`
- Result: `1 passing`
- Finding status: rejected.

## What We Learned

The mint path does not silently accept a worse-than-quoted output after the pool changes; it reverts through slippage protection.

## Next Step

Either inspect the `Staking.collect` call path for C2 or move to `RewardsManager`, the next ranked accounting target.
