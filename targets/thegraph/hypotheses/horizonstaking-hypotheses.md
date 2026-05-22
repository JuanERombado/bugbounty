# HorizonStaking Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`, `confirmed-low`.

## HZ1: Delegation Share Rounding Can Trap Small Residual Delegations

- Status: covered-existing-tests
- Asset: HorizonStaking delegation accounting.
- Hypothesis: after pool value changes through slashing or added tokens, a partial undelegation can leave a delegator with shares whose token value is below `MIN_DELEGATION`, forcing a revert.
- Why it might matter: delegators may be unable to partially exit or may need unintuitive full-exit behavior.
- Impact if true: possible user fund friction or griefing, likely low unless funds become stuck.
- Minimal local test idea: create a provision, delegate, alter pool value, then fuzz partial undelegations around `MIN_DELEGATION`.
- Result: existing tests cover partial undelegation below `MIN_DELEGATION`, invalid pools after full slashing, and pool recovery through `addToDelegationPool`.
- Evidence files: `external/thegraph-contracts/packages/horizon/test/unit/staking/delegation/undelegate.t.sol`, `external/thegraph-contracts/packages/horizon/test/unit/staking/delegation/withdraw.t.sol`, and `external/thegraph-contracts/packages/horizon/test/unit/staking/delegation/addToPool.t.sol`.

## HZ2: Slashing During Thawing Can Create Rounding Dust Or Invalidate Pending Withdrawals

- Status: covered-existing-tests
- Asset: HorizonStaking slashing plus thaw request accounting.
- Hypothesis: slashing while provider or delegation tokens are thawing can round `tokensThawing` down or invalidate pending thaw requests, losing more value than intended.
- Why it might matter: slashing is a high-value state transition and explicitly mutates thaw pools.
- Impact if true: excess loss, stuck thaw requests, or accounting mismatch.
- Minimal local test idea: create provider/delegator thaw requests, slash different fractions, then compare post-withdraw balances and pool accounting.
- Result: existing Foundry tests already cover provider thaw rounding, delegation thaw rounding, and full slash reset behavior.
- Evidence files: `external/thegraph-contracts/packages/horizon/test/unit/staking/slash/slash.t.sol`, `external/thegraph-contracts/packages/horizon/test/unit/staking/provision/thaw.t.sol`, and `external/thegraph-contracts/packages/horizon/test/unit/staking/delegation/withdraw.t.sol`.

## HZ3: Thaw Request Ordering Can Delay Already-Expired Requests After Parameter Changes

- Status: confirmed-low
- Asset: HorizonStaking thaw request linked lists.
- Hypothesis: if thawing periods are shortened, a later request can expire before an earlier request, but fulfillment stops at the first unexpired request.
- Why it might matter: expired funds may remain temporarily inaccessible because the list is creation-ordered, not expiry-ordered.
- Impact if true: withdrawal delay; likely low unless it can be extended or weaponized.
- Scope caution: code comments already acknowledge this behavior.
- Minimal local test idea: create two thaw requests with different thawing periods, shorten parameters, then try to fulfill the later expired request.
- Result: JS harness confirms the ordering behavior; a Solidity test was added but could not be run because `forge` is unavailable in this environment.
- Candidate severity: likely low because the delay clears when the older request expires and parameter changes require service provider/verifier acceptance.
- Evidence files: `targets/thegraph/pocs/horizonstaking-hz3-harness.js` and `external/thegraph-contracts/packages/horizon/test/unit/staking/provision/thaw.t.sol`.

## HZ4: Legacy SubgraphService Paths May Diverge From New Verifier-Specific Paths

- Status: covered-existing-tests
- Asset: HorizonStaking legacy compatibility.
- Hypothesis: the special `SUBGRAPH_DATA_SERVICE_ADDRESS` paths use legacy operator and delegation storage, which may behave differently from the new verifier-specific pools.
- Why it might matter: migration compatibility surfaces often hide state transition bugs.
- Impact if true: authorization bypass, wrong pool accounting, or unexpected withdrawals.
- Minimal local test idea: compare the same operator/delegation action through legacy and non-legacy verifier paths.
- Result: existing tests cover legacy delegation, undelegation, withdrawal, and locked operator behavior.
- Evidence files: `external/thegraph-contracts/packages/horizon/test/unit/staking/delegation/delegate.t.sol`, `external/thegraph-contracts/packages/horizon/test/unit/staking/delegation/undelegate.t.sol`, `external/thegraph-contracts/packages/horizon/test/unit/staking/delegation/withdraw.t.sol`, and `external/thegraph-contracts/packages/horizon/test/unit/staking/operator/locked.t.sol`.

## HZ5: Force Withdraw Legacy Delegation Can Be Used Out Of Sequence

- Status: covered-existing-tests
- Asset: HorizonStaking legacy withdrawal.
- Hypothesis: `forceWithdrawDelegated` lets any caller withdraw a legacy delegator's locked tokens to the delegator, which may bypass expected caller sequencing.
- Why it might matter: permissionless helper functions can become griefing tools when downstream state assumes user timing.
- Impact if true: likely low because funds go to the delegator, not the caller.
- Minimal local test idea: set up legacy locked delegation state and call force withdraw from an unrelated account.
- Result: existing tests cover unrelated caller and delegator-triggered force withdrawal; funds are paid to the delegator.
- Evidence file: `external/thegraph-contracts/packages/horizon/test/unit/staking/delegation/forceWithdrawDelegated.t.sol`.

## Picked First Test

HZ2 was checked first through existing coverage; HZ3 was confirmed as a low-severity delay behavior.

## Next Step

Close the HorizonStaking first pass and move to a different high-value surface, likely `SubgraphService` payments/collection or `AllocationExchange`.
