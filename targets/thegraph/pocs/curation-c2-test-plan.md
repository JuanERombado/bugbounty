# Curation C2 Test Plan

## Hypothesis

`Curation.collect` could overstate pool tokens if the staking path calls it without transferring the matching GRT.

## Local Test Shape

1. Use the real `Staking.collect` path, not a fake direct call.
2. Create a curated subgraph deployment and an allocation.
3. Collect query fees with a non-zero curation percentage.
4. Assert the curation pool token increase equals the actual GRT balance increase in `Curation`.

## Expected Safe Result

The staking path transfers GRT to `Curation` before calling `collect`, so accounting and actual token balance move together.

## Vulnerable Result

Pool tokens increase without the `Curation` contract receiving the same amount of GRT.

## Test Result

- Invariant added: curation pool token increase must equal actual `Curation` GRT balance increase.
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/staking/allocation.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/staking/allocation.test.ts --grep "with 20% curationFees, 0% protocolTax and 0% queryFeeCut"`
- Result: `7 passing`
- Finding status: rejected for the real staking path.

## What We Learned

The production staking path calls `TokenUtils.pushTokens` before `curation.collect`, so curation accounting and actual GRT balances move together.

## Next Step

Move to `RewardsManager`, focusing on reward issuance, allocation close rewards, and L1/L2 mint allowance assumptions.
