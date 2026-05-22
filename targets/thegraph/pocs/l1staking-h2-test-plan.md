# L1Staking H2 Test Plan

## Hypothesis

`transferDelegationToL2` might burn all of a delegator's shares while sending a rounded-down token amount, creating unrecoverable value loss or accounting dust.

## Why This Is First

It is easy to test locally because the repo already has `contracts-test/tests/unit/staking/l2Transfer.test.ts` with setup for staking, delegation, and L2 transfer mocks.

## Local Test Shape

1. Stake an indexer.
2. Delegate from at least two delegators so the pool has multiple share owners.
3. Add delegation rewards or otherwise skew `pool.tokens / pool.shares`.
4. Transfer one delegator's full delegation to L2.
5. Assert conservation:
   - the transferred token amount equals the delegator's pre-transfer pro-rata claim rounded as expected,
   - pool shares decrease by exactly that delegator's shares,
   - pool tokens decrease by exactly the transferred amount,
   - remaining delegators' pro-rata value is not reduced unexpectedly,
   - no meaningful dust is trapped when the last delegator transfers.

## Expected Safe Result

Rounding is either negligible, remains claimable by remaining delegators, or is impossible to amplify into meaningful loss.

## Vulnerable Result

A delegator can lose meaningful value during migration, or dust accumulates in a way that no remaining delegator can recover.

## Rejection Criteria

Reject this hypothesis if losses are bounded to tiny integer dust and cannot plausibly meet The Graph's accepted high or critical impacts.

## Result

Rejected by targeted local test.

Command run from `external/thegraph-contracts/packages/contracts-test`:

```powershell
pnpm exec hardhat test --network hardhat tests/unit/staking/l2Transfer.test.ts --grep "preserves delegation pool accounting"
```

Observed result:

```text
1 passing
```

The added test showed that a rounded pro-rata delegation transfer preserves pool accounting for the remaining delegator, and the pool reaches zero tokens and zero shares after the final delegator migrates.

## Files To Use

- `external/thegraph-contracts/packages/contracts-test/tests/unit/staking/l2Transfer.test.ts`
- `external/thegraph-contracts/packages/contracts/contracts/staking/L1Staking.sol`
- `external/thegraph-contracts/packages/contracts/contracts/staking/StakingExtension.sol`
