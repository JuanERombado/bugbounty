# SubgraphService Payment-Flow Hypotheses

## Gate Result

- Duplicate-risk gate: passed for SubgraphService-specific indexing-fee hypotheses.
- Known no-tread areas: RAM JIT fallback, RecurringCollector callback gas/returndata, malformed ERC165, EIP-7702 payer-code, stale escrow snapshots.
- Main filter: do not chase behavior already covered by local tests unless a new value-loss or authorization break appears.
- Relevant design note: `MaxSecondsPerCollectionCap.md` says capped collection is intended to avoid stuck agreements and that every collection goes through `_tokensToCollect`.

## H1: Zero Payment Destination For Indexing Fees

- Status: `rejected-safe-default`
- Potential severity: informational.
- Idea: `SubgraphService.collect` forwards `paymentsDestination[indexer]` into indexing-fee collection, but the indexer may never set it.
- Why it matters: indexing rewards explicitly handle zero destination by restaking, but indexing-fee destination handling happens deeper in RecurringCollector/GraphPayments.
- Local result: `GraphPayments.collect` stakes the receiver share to the service provider when `receiverDestination == address(0)`.
- Decision: do not pursue unless a later integration test shows the staking destination differs from the intended receiver.

## H2: Entity-Based Fee Term Can Exceed RCA Rate Cap

- Status: `candidate`
- Potential severity: medium if a service provider can force repeated collection reverts or bypass payer expectations; likely low if RecurringCollector caps and slippage fully cover it.
- Idea: `_validateTermsAgainstRCA` checks `tokensPerSecond <= maxOngoingTokensPerSecond` but does not include `tokensPerEntityPerSecond`.
- Why it matters: a large `entities` value can make SubgraphService request far more than the RCA nominal rate before RecurringCollector narrows payout.
- Local test idea: create terms with low base rate and high entity rate, collect with large entities, and assert whether payout is capped, reverted, or slippage-controlled.
- Easiest next step: inspect RecurringCollector `collect` cap math before writing a test.

## H3: Overflow-As-DoS In `_tokensToCollect`

- Status: `test-written-pending-foundry`
- Potential severity: likely low-to-medium because it can block an agreement's collection path, but appears to require payer-signed/indexer-accepted extreme terms.
- Idea: `collectionSeconds * (tokensPerSecond + tokensPerEntityPerSecond * entities)` can revert on overflow before RecurringCollector can cap the value.
- Why it matters: if payer-approved terms plus indexer-chosen collection metadata can repeatedly overflow, accrued fees may become hard to collect.
- Local test added: `test_SubgraphService_CollectIndexingFees_Reverts_WhenEntityFeeRequestOverflowsBeforeCap` in `collect.t.sol`.
- Local simulator added: `scripts/simulate-subgraphservice-entity-fee-overflow.js`.
- Current assessment: keep alive, but do not draft a report until Foundry confirms and we determine whether safer inputs can recover collection.
- Easiest next step: install Foundry or run the test in an environment with `forge`, then decide whether this is an accepted-dangerous-terms issue or just unrealistic signed input.

## H4: Stale Allocation Resize Leaves Active Fee Agreement On Zero-Token Allocation

- Status: `candidate`
- Potential severity: medium if an agreement can keep collecting after the allocation has no meaningful stake; likely intended if RecurringCollector or disputes handle this.
- Idea: tests confirm stale/over-allocated allocation paths resize to zero and keep the agreement active.
- Why it matters: the agreement stays active while allocation tokens are zero, which may affect economic assumptions around service quality, dispute incentives, or fee collection.
- Local test idea: force resize-to-zero, wait collection interval, collect indexing fees, and assert whether this is allowed and whether any dispute/security invariant is violated.
- Easiest next step: inspect comments and tests around `closeStaleAllocation` and dispute eligibility.

## H5: Rebind After Deadline Has No Fresh Payer Authorization

- Status: `watchlist`
- Potential severity: high only if a payer's old agreement can be moved to a materially different economic context without their consent; currently likely intended and covered by tests.
- Idea: a same-hash agreement can rebind to a new allocation after the original acceptance deadline because RecurringCollector takes an idempotent path.
- Why it matters: payer authorization is bound to agreement terms and service provider, while allocation identity can change.
- Local test idea: try rebinding across different subgraph deployment, wrong indexer, closed allocation, and allocation with existing active agreement to confirm all guardrails hold.
- Easiest next step: deprioritize unless another hypothesis shows value movement changes after rebind.

## Recommended Pick

Continue with H3 because it checks whether SubgraphService can overflow before RecurringCollector applies the payer's cap.
