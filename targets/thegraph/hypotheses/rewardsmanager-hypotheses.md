# RewardsManager Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`.

## R1: Minimum Signal Changes Can Retroactively Reclaim Or Grant Rewards Unexpectedly

- Status: rejected
- Asset: RewardsManager
- Hypothesis: changing `minimumSubgraphSignal` can retroactively reclaim or grant rewards for prior periods in a way that harms participants.
- Why it might matter: the contract comments explicitly warn that threshold changes apply to pending rewards since the last update.
- Impact if true: rewards could be misdirected or withheld.
- Out-of-scope risk: threshold changes are authorized governance/oracle actions and may be intended behavior.
- Minimal local test idea: accrue rewards while eligible, raise threshold before update, and verify whether pending rewards are reclaimed rather than distributed.
- Evidence that rejects it: behavior is documented, permissioned, and existing tests cover below-minimum reward exclusion.
- Result: existing local tests passed for below-minimum exclusion, threshold-change no-underflow cases, reclaim routing, and reward dropping when no reclaim address is configured.
- Rejection reason: the retroactive threshold effect is explicitly documented in `RewardsManager.sol` with an operational mitigation, so this is not currently a hidden vulnerability.

## R2: Reclaim Priority Can Send Rewards To The Wrong Address When Multiple Conditions Apply

- Status: rejected
- Asset: RewardsManager
- Hypothesis: if a subgraph is denied and an indexer is ineligible at the same time, rewards may route to an unintended reclaim address.
- Why it might matter: reclaim routing is value movement.
- Impact if true: protocol rewards could be minted to the wrong recipient.
- Minimal local test idea: configure both reclaim addresses, make both conditions true, and assert the intended priority.
- Evidence that rejects it: explicit priority chooses subgraph denial first when it has a configured address.
- Result: existing local test passed; when both conditions are true and `SUBGRAPH_DENIED` is configured, rewards go to the subgraph-denied reclaim address and not the indexer-ineligible address.
- Rejection reason: reclaim priority is explicit and covered by the test suite.

## R3: Reclaim Address Changes Redirect Old Rewards Retroactively

- Status: rejected
- Asset: RewardsManager
- Hypothesis: changing a reclaim address can redirect rewards accrued before the change.
- Why it might matter: retroactive value routing can surprise participants.
- Out-of-scope risk: contract comments explicitly document this as intended.
- Minimal local test idea: accrue reclaimable rewards, change reclaim address, close allocation, and confirm rewards go to the new address.
- Evidence that rejects it: documented governor-only behavior.
- Result: local test confirmed accrued pre-denial rewards are sent to the current reclaim address after a reclaim-address change.
- Rejection reason: the behavior is real, but it is explicitly documented, governor-only, and therefore not a hidden vulnerability by itself.

## R4: Issuance Allocator Changes Can Double Count Or Drop Rewards

- Status: rejected
- Asset: RewardsManager / issuance allocator
- Hypothesis: switching between local issuance and allocator issuance can miss the snapshot and double count or drop rewards.
- Why it might matter: this is a direct inflation/reward accounting boundary.
- Minimal local test idea: accrue under local issuance, switch allocator, accrue more, and compare total minted/reclaimable rewards to expected block-by-block issuance.
- Evidence that rejects it: `setIssuanceAllocator` and `beforeIssuanceAllocationChange` call `updateAccRewardsPerSignal`.
- Result: existing local tests passed for allocator-rate accrual and local-to-allocator-to-local switching.
- Rejection reason: reward accounting is snapshotted before allocator changes, and phase-by-phase accrual matches the expected rates.

## R5: L2 Issuance Updates Can Exceed L1 Bridge Mint Allowance If Not Coordinated

- Status: rejected
- Asset: RewardsManager / L1GraphTokenGateway
- Hypothesis: L2 issuance changes without matching L1 mint allowance updates can break withdrawals or mint accounting.
- Why it might matter: reward issuance and bridge mint allowance must stay coordinated.
- Out-of-scope risk: likely operational/governance coordination unless a contract allows excess minting.
- Minimal local test idea: compare L2 issuance increase with L1 gateway mint allowance limits in the local bridge harness.
- Evidence that rejects it: L1 gateway enforces mint allowance and reverts over-mint attempts.
- Result: existing local bridge tests passed for minting up to allowance, rejecting over-allowance minting, and preventing consumed allowance reuse.
- Rejection reason: the L1 gateway enforces the mint allowance locally, so a coordination mistake may break withdrawals but does not by itself allow excess L1 minting.

## Picked First Test

R2 was checked first because reclaim priority is direct value routing and can be tested without live systems.

R4 was checked second because issuance allocator switching is the most direct reward-inflation/accounting boundary.

R1 was checked third because minimum-signal threshold changes can affect pending rewards and teaches an important "documented governance behavior vs bug" distinction.

R3 was checked fourth because reclaim address changes are another explicitly retroactive value-routing behavior.

R5 was checked fifth because it connects RewardsManager issuance with bridge mint-allowance enforcement across L1/L2 accounting.

RewardsManager pass result: all five starter hypotheses are rejected or documented behavior, with local evidence.

Next best target: `DisputeManager`, because disputes are high-value state transitions involving slashing, rewards, and challenge windows.
