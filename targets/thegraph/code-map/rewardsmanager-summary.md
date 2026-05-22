# RewardsManager Summary

## Plain-English Purpose

`RewardsManager` tracks how newly issued GRT rewards should be allocated to subgraphs, indexers, and reclaim addresses.

## Value Movement

- `takeRewards` mints rewards to the authorized rewards issuer, currently the subgraph service/staking path.
- Denied, ineligible, below-minimum, no-signal, and no-allocation rewards can be reclaimed to configured addresses.
- If no reclaim address is configured, denied or unclaimable rewards are dropped instead of minted.
- `issuancePerBlock` or an external issuance allocator controls the reward rate.

## Role Checks

- Only the governor can set issuance, subgraph service, eligibility oracle, issuance allocator, reclaim addresses, and `revertOnIneligible`.
- The subgraph availability oracle or governor can set `minimumSubgraphSignal`.
- Only the subgraph availability oracle can deny or undeny subgraphs.
- Only the configured rewards issuer can call `takeRewards` and `reclaimRewards`.

## Accounting Invariants

- Rewards per signal should only increase.
- Rewards per allocated token should not increase when a subgraph is denied, below minimum signal, or has no allocations.
- Reclaimed rewards should not also be mintable to an indexer.
- Changing issuance or allocator should first snapshot accumulated rewards under the old rate.
- Existing reward gaps should remain claimable when temporary exclusion conditions clear.

## First Things To Hunt

- Retroactive threshold changes around `minimumSubgraphSignal`.
- Denial and eligibility priority when multiple reclaim reasons apply.
- Reclaim address changes applying retroactively.
- Issuance allocator changes and snapshot timing.
- L2 issuance changes requiring L1 gateway mint allowance updates.
