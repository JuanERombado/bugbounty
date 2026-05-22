# RewardsManager R2 Test Plan

## Hypothesis

When both subgraph denial and indexer ineligibility apply, rewards might be reclaimed to the wrong address.

## Local Test Shape

1. Configure reclaim addresses for `SUBGRAPH_DENIED` and `INDEXER_INELIGIBLE`.
2. Make the indexer ineligible through the local mock eligibility oracle.
3. Deny the subgraph.
4. Close a pre-denial allocation.
5. Assert rewards go to the `SUBGRAPH_DENIED` reclaim address and not the ineligible-indexer address.

## Expected Safe Result

`SUBGRAPH_DENIED` takes priority when it has a configured reclaim address.

## Test Result

- Existing test used: `should reclaim to SUBGRAPH_DENIED when both conditions true and SUBGRAPH_DENIED address configured (pre-denial allocation)`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/rewards/rewards-reclaim.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/rewards/rewards-reclaim.test.ts --grep "SUBGRAPH_DENIED when both conditions true"`
- Result: `1 passing`
- Finding status: rejected.

## What We Learned

Dual-denial reclaim routing is explicit and tested: subgraph denial wins over indexer ineligibility when the subgraph-denied reclaim address is configured.

## Next Step

Test or inspect R4 next, because issuance allocator switching is the highest-value RewardsManager accounting boundary left.
