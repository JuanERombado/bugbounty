# L1Staking Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`.

## H1: L1 State And L2 Credit Can Diverge If The Retryable Or Callhook Fails

- Status: rejected
- Asset: L1Staking / L1GraphTokenGateway
- Hypothesis: stake or delegation can be removed from L1 accounting even if the L2 receive/callhook does not ultimately credit the intended L2 staking account.
- Why it might matter: the gateway comment says callhook failure can lock bridged tokens if the callhook never succeeds.
- Impact if true: potential direct loss or permanent lock of migrated stake/delegation.
- Scope fit: likely high-value if it affects in-scope contracts and can be shown locally without relying on third-party bridge failure as the only cause.
- Out-of-scope risk: could be considered known bridge/callhook liveness risk or third-party Arbitrum behavior.
- Minimal local test idea: simulate a valid L1 transfer where L1 state and escrow update, then force L2 staking callhook failure and verify whether funds can be recovered or credited.
- Evidence that rejects it: the retryable can always be retried with the same valid callhook, or failed callhook cannot happen for valid in-scope messages.
- Result so far: targeted L2 test confirms a valid L1 staking migration message reverts if L2 staking is partial-paused, and the L2 mint/credit rolls back locally.
- Current assessment: not a finding yet because the observed failure is caused by privileged protocol pause state and may be normal retryable-ticket behavior rather than a bug in The Graph contracts.
- Next question: can any non-privileged or ordinary in-scope state make the L1Staking-generated callhook permanently fail?
- Final local assessment: no non-privileged permanent-failure path was identified from the reviewed code; L1Staking generates fixed valid message codes/ABI, indexer-stake receive has no user-controlled rejection condition, and delegation receive returns too-small/zero-share transfers to the delegator instead of reverting.
- Rejection reason: the only demonstrated valid-message rejection depends on privileged partial pause state, which is not enough for an Immunefi finding under the current rules and evidence.

## H2: Delegation Pool Rounding Can Burn Shares For Less Than Expected L2 Credit

- Status: rejected
- Asset: L1Staking
- Hypothesis: `delegation.shares * pool.tokens / pool.shares` can round down during `transferDelegationToL2`, leaving meaningful value behind or creating dust that cannot be recovered.
- Why it might matter: delegation transfer burns all shares and sends only the floored token amount.
- Impact if true: delegators could lose value during migration.
- Scope fit: potential accounting issue, but likely low unless the loss can become material.
- Out-of-scope risk: tiny rounding dust may not meet paid impact.
- Minimal local test idea: create skewed pool token/share ratios through delegation rewards, transfer all delegation to L2, and assert pool and delegator value conservation.
- Evidence that rejects it: any residual dust stays in the pool for remaining delegators and cannot become material user fund loss.
- Result: targeted local test passed; after one delegator migrates, remaining pool accounting is conserved, and after the final delegator migrates the pool reaches zero tokens and zero shares.

## H3: Partial Indexer Migration Plus Later Rewards Can Create Unexpected L1 Stake State

- Status: rejected
- Asset: L1Staking / RewardsManager
- Hypothesis: after an indexer partially migrates to L2, later rewards or query rebates can restake to the L1 indexer and create a confusing mixed L1/L2 stake position.
- Why it might matter: migration accounting assumes a fixed L2 beneficiary after first transfer.
- Impact if true: possibly stuck stake, incorrect capacity, or unexpected reward accounting.
- Scope fit: could matter if it causes direct fund loss or incorrect participant action.
- Out-of-scope risk: mixed L1/L2 operation may be intended.
- Minimal local test idea: partially transfer stake, leave an allocation, close/collect rewards, and verify whether newly restaked L1 rewards can be migrated safely.
- Evidence that rejects it: subsequent transfers to the same L2 beneficiary handle the new stake cleanly.
- Result: targeted local tests passed for both query-fee rebates and indexing rewards after partial migration.
- Rejection reason: restaked L1 rewards can only move to the original fixed L2 beneficiary, and moving them to that beneficiary restores the expected L1 stake state.

## H4: Locked Transfer Tool Trust Boundary Can Misroute Stake Or Delegation

- Status: new
- Asset: L1Staking / GraphTokenLockWallet tooling
- Hypothesis: `transferLockedStakeToL2` and `transferLockedDelegationToL2` fully trust the transfer tool's `l2WalletAddress` mapping, so a tool mapping bug could send migrated funds to the wrong L2 beneficiary.
- Why it might matter: vesting wallets may not be normal EOAs and rely on this mapping.
- Impact if true: user funds could be credited to the wrong L2 account.
- Scope fit: only in scope if the transfer tool and affected wallet path are in scope and the bug is not privileged/governance-only.
- Out-of-scope risk: if it requires governor setting a malicious transfer tool, it is likely out of scope.
- Minimal local test idea: model stale or changed mapping behavior in the transfer tool and verify whether L1Staking has any independent protection.
- Evidence that rejects it: only trusted/governance-controlled setup can cause the bad mapping.

## H5: Migration Checks May Miss A State Where Active Allocation Capacity Becomes Unsafe

- Status: rejected
- Asset: L1Staking
- Hypothesis: `_transferStakeToL2` checks current capacity, but another state transition around delegation, slashing, or allocation close could still leave active allocations undercollateralized after migration.
- Why it might matter: active allocations should remain covered by stake plus usable delegated capacity.
- Impact if true: accounting or slashing assumptions could break around migrated stake.
- Scope fit: possible high if it causes direct user fund loss or incorrect rewards.
- Out-of-scope risk: slash-only or parameter-governance scenarios may be excluded.
- Minimal local test idea: fuzz local sequences of delegate, allocate, partial transfer, undelegate, slash, and close allocation against a capacity invariant.
- Evidence that rejects it: overallocated states are expected and safely handled by capacity returning zero until restored.
- Result so far: targeted local test passed for post-migration delegation removal; `getIndexerCapacity` returns zero after overallocation and a further unsafe L2 stake transfer reverts with `! allocation capacity`.
- Additional result: targeted local test passed for post-migration slashing; privileged slashing can create an overallocated state, but capacity stays zero and another unsafe L2 stake transfer is blocked.
- Final tested result: closing the active allocation from a partially migrated overallocated state clears `tokensAllocated` and restores positive capacity.
- Rejection reason: the tested state transitions preserve the expected safety behavior; no direct loss, excess migration, or incorrect capacity was reproduced.

## Picked First Test

H2 was tested first because it only needed the existing staking/delegation test harness and a value-conservation assertion around `transferDelegationToL2`, without needing a realistic Arbitrum retryable lifecycle.

Next best hypothesis: H5, because allocation-capacity invariants around partial migration, delegation changes, and slashing are still high-value state-machine territory.
