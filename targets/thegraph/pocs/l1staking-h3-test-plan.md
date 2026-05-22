# L1Staking H3 Test Plan

## Hypothesis

After an indexer partially migrates stake to L2, later rewards or query rebates can restake to the L1 indexer and create confusing or unsafe mixed L1/L2 stake state.

## Why This Is Next

Unlike H1, this can be tested entirely through normal protocol state transitions without relying on privileged pause state or bridge retryable behavior.

## Local Test Shape

1. Stake an indexer on L1.
2. Create an allocation that can earn query rebates or indexing rewards.
3. Partially transfer indexer stake to L2.
4. Trigger reward or rebate collection that restakes to the L1 indexer.
5. Check whether the new L1 stake can be safely migrated only to the original L2 beneficiary.
6. Check whether allocation capacity, rewards destination, and minimum stake invariants still hold.

## Expected Safe Result

Any post-migration L1 rewards become normal L1 stake and can only be migrated to the original fixed L2 beneficiary while preserving capacity and minimum-stake rules.

## Vulnerable Result

Rewards become stuck, can be migrated to the wrong beneficiary, or allow capacity/accounting state that violates the intended migration invariants.

## First Local Question

Can an indexer who already partially migrated receive new restaked L1 rewards and then migrate those rewards cleanly to the same L2 beneficiary?

## Result

Rejected by targeted local tests.

Command run from `external/thegraph-contracts/packages/contracts-test`:

```powershell
pnpm exec hardhat test --network hardhat tests/unit/staking/l2Transfer.test.ts --grep "allows restaked L1"
```

Observed result:

```text
2 passing
```

The tests covered query-fee rebates and indexing rewards after partial migration.

## Local Assessment

- New L1-restaked rewards after partial migration cannot be migrated to a different L2 beneficiary.
- Those rewards can be migrated to the original fixed L2 beneficiary.
- After migration, the L1 stake returns to the expected post-partial-migration amount.

This does not support an Immunefi report.
