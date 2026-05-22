# L1Staking H5 Test Plan

## Hypothesis

Migration checks may miss a state where active allocation capacity becomes unsafe after partial stake migration, delegation changes, or slashing.

## Why This Is Next

Capacity is a high-value invariant: active allocations should remain covered by secure indexer stake plus usable delegated capacity.

## Local Test Shape

1. Set delegation ratio low enough to make capacity easy to reason about.
2. Stake an indexer and add delegation.
3. Create an active allocation near the maximum allowed capacity.
4. Partially migrate indexer stake to L2.
5. Try delegation removal, slashing, and allocation close paths around the migrated state.
6. Assert that the contract either blocks unsafe migration or safely reports zero new capacity until the state is restored.

## Expected Safe Result

The contract blocks migration that would immediately violate active allocation capacity, and later overallocated states are handled by returning zero capacity until stake, delegation, or allocations are restored.

## Vulnerable Result

The contract allows a migration or sequence that makes active allocation accounting unsafe in a way that causes direct fund loss or incorrect rewards.

## First Local Question

After a safe partial migration, can a delegator undelegate enough to make the indexer overallocated, and does the protocol handle that overallocated state safely?

## Test Result: Delegation Removal Branch

- Test added: `reports zero capacity after delegation removal makes a partially migrated indexer overallocated`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/staking/l2Transfer.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/staking/l2Transfer.test.ts --grep "reports zero capacity"`
- Result: `1 passing`
- Finding status: rejected for this branch.

## Test Result: Slashing Branch

- Test added: `reports zero capacity after slashing makes a partially migrated indexer overallocated`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/staking/l2Transfer.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/staking/l2Transfer.test.ts --grep "reports zero capacity after slashing"`
- Result: `1 passing`
- Finding status: rejected for this branch.

## Test Result: Allocation Close Branch

- Test added: `restores capacity after closing an allocation from a partially migrated overallocated state`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/staking/l2Transfer.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/staking/l2Transfer.test.ts --grep "restores capacity"`
- Result: `1 passing`
- Finding status: rejected for this branch.

## What We Learned

After a safe partial migration, removing enough delegation or slashing enough stake can make the indexer overallocated, but the contract safely reports zero available capacity and blocks another unsafe L2 stake transfer with `! allocation capacity`.

Closing the active allocation clears `tokensAllocated` and restores positive capacity, which matches the expected recovery path.

## Final Local Assessment

H5 is rejected for the tested branches because delegation removal, slashing, and allocation close all preserve the expected capacity behavior.

## Next Step

Move to H4 only if the transfer tool is in scope; otherwise move to the next high-value asset, `BridgeEscrow` or gateway bridge accounting.
