# L1Staking Plain-English Summary

Reviewed files:

- `external/thegraph-contracts/packages/contracts/contracts/staking/L1Staking.sol`
- `external/thegraph-contracts/packages/contracts/contracts/staking/Staking.sol`
- `external/thegraph-contracts/packages/contracts/contracts/staking/StakingExtension.sol`
- `external/thegraph-contracts/packages/contracts/contracts/staking/StakingStorage.sol`
- `external/thegraph-contracts/packages/contracts/contracts/staking/libs/Stakes.sol`
- `external/thegraph-contracts/packages/contracts/contracts/gateway/L1GraphTokenGateway.sol`

## What It Does

`L1Staking` is the Ethereum L1 version of The Graph staking contract, with extra migration functions that send indexer stake and delegator stake to the L2 staking contract through the L1 Graph Token Gateway.

## Main Actors

- Indexer: stakes GRT, allocates stake to subgraphs, earns rewards, and can transfer stake to L2.
- Delegator: delegates GRT to an indexer and can transfer delegation to L2 after the indexer has transferred stake.
- Operator: can allocate or close for an indexer, but cannot call L1-to-L2 stake transfer because that uses `msg.sender` as the indexer.
- Governor: sets protocol parameters, gateway/counterpart addresses, extension implementation, slasher, and transfer tool.
- Slasher: can slash indexer stake through `StakingExtension`.
- L1GraphTokenGateway: escrows GRT and creates the retryable L2 message.
- L1GraphTokenLockTransferTool: supplies L2 wallet mapping and ETH for vesting lock wallet migrations.

## Value Movement

- `stake()` / `stakeTo()` pulls GRT from the caller into the staking contract and increases `tokensStaked`.
- `unstake()` moves available indexer stake into a locked state until the thawing period passes.
- `withdraw()` sends withdrawable indexer stake back to the indexer.
- `delegate()` pulls GRT from a delegator, burns delegation tax, mints delegation pool shares, and increases pool tokens.
- `undelegate()` burns delegation shares and locks the corresponding tokens until the unbonding period passes.
- `withdrawDelegated()` either returns unlocked delegated tokens or re-delegates them to another indexer.
- `collect()` pulls query fees, burns protocol tax, pays curation fees, calculates rebates, adds delegator rewards to the pool, and sends or restakes indexer rewards.
- `transferStakeToL2()` subtracts stake from the L1 indexer balance and sends GRT plus a callhook message through the gateway.
- `transferDelegationToL2()` removes all of a delegator's shares for an indexer, subtracts their pro-rata pool tokens, and sends GRT plus a callhook message through the gateway.

## Role Checks

- Governance setters use `onlyGovernor`.
- Stake transfer to L2 can only be initiated by the indexer because the external function passes `msg.sender` as `_indexer`.
- Delegation transfer to L2 can only be initiated by the delegator because the external function passes `msg.sender` as `_delegator`.
- Allocation can be done by indexer or authorized operator through `_isAuth`.
- Closing allocations can be done by indexer/operator, or by anyone only after max allocation epochs and only for non-zero allocations.
- Slashing requires an allowed slasher.
- Locked transfer helpers trust `L1GraphTokenLockTransferTool` for L2 wallet mapping and ETH funding.

## Delegation Model

- Each indexer has a delegation pool with `tokens` and `shares`.
- Delegating mints shares proportional to existing pool value.
- Undelegating burns shares and locks the corresponding tokens.
- Transferring delegation to L2 burns all of the delegator's shares for that indexer and bridges the pro-rata token amount.
- Delegator rewards increase pool tokens, so shares can become worth more tokens over time.

## L1-To-L2 Transfer Paths

- `transferStakeToL2`: normal indexer pays ETH directly for retryable ticket gas.
- `transferLockedStakeToL2`: vesting wallet path gets beneficiary and ETH from the transfer tool.
- `transferDelegationToL2`: normal delegator pays ETH directly for retryable ticket gas.
- `transferLockedDelegationToL2`: vesting wallet path gets beneficiary and ETH from the transfer tool.
- `unlockDelegationToTransferredIndexer`: if an indexer fully moved to L2, delegators who already undelegated can unlock early and withdraw immediately.

## Important Accounting Invariants

- Indexer `tokensStaked` should only decrease when stake is withdrawn, slashed, or transferred to L2.
- `tokensStaked - tokensLocked` must stay at zero or above minimum indexer stake.
- An indexer cannot transfer all stake to L2 while allocations are open.
- A partial stake transfer must leave enough stake plus delegated capacity to cover active allocations.
- Delegation pool `tokens` and `shares` must decrease together when delegation moves to L2.
- A delegator cannot transfer L2 delegation while they have tokens locked for undelegation.
- The first L2 stake transfer fixes the indexer's L2 beneficiary forever.
- L1 state changes for L2 transfers should correspond to successful token escrow and a valid L2 receive message.

## Existing Test Coverage Observed

The repo already has a dedicated `contracts-test/tests/unit/staking/l2Transfer.test.ts` suite covering many direct checks: pause behavior, minimum stake constraints, locked stake rejection, zero beneficiary rejection, open-allocation rejection, capacity checks, ETH amount equality, repeated same-beneficiary transfers, different-beneficiary rejection, locked transfer tool behavior, early delegated unlock, delegation transfer, duplicate delegation transfer prevention, and locked delegation transfer behavior.

## Highest-Value Review Gap

The most interesting remaining area is not a simple missing require; it is whether L1 staking/delegation state can be reduced while the L2 bridge/callhook path fails, expires, or credits a different state than L1 assumed.
