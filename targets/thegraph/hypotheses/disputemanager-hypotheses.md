# DisputeManager Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`.

## D1: Duplicate Query Disputes Can Slash The Same Attestation More Than Once

- Status: rejected
- Asset: DisputeManager
- Hypothesis: because query dispute IDs include `fisherman`, two fishermen can dispute the same attestation and both accepted disputes may slash the same indexer.
- Why it might matter: repeated slashing for one underlying action could over-penalize an indexer and overpay fishermen.
- Out-of-scope risk: slashing-only impacts may be excluded or lower priority unless they cause broader direct fund loss.
- Minimal local test idea: create the same query dispute from two fishermen, accept both, and compare total stake loss to one expected slash.
- Result: local test passed; the duplicate dispute from `fisherman2` could be accepted after the first dispute, and the indexer was slashed again based on remaining stake.
- Rejection reason: OpenZeppelin's 2023 Dispute Manager audit explicitly documents that different fishermen can create query disputes against the same resolved attestation and places responsibility on the arbitrator.
- Reportability note: do not draft an Immunefi report; this is known/assumed behavior and the direct impact is slashing.

## D2: Related Conflict Dispute Resolution Can Leave A Pending Twin

- Status: rejected
- Asset: DisputeManager
- Hypothesis: accepting or drawing one linked conflict dispute might fail to finalize the related dispute in some ordering.
- Why it might matter: stale pending disputes can later trigger unexpected slashing or deposit movement.
- Minimal local test idea: create conflict disputes, accept or draw one side, then try to resolve the related side.
- Evidence that rejects it: existing tests cover basic accept/draw conflict resolution.
- Result: local tests passed; accepting either side accepts that side and rejects its twin, while drawing either side marks both as drawn.
- Rejection reason: related conflict disputes do not stay pending after the main dispute is resolved.

## D3: Drawn Conflict Disputes May Emit Only One Event While Resolving Two Disputes

- Status: rejected
- Asset: DisputeManager
- Hypothesis: drawing one conflict dispute changes the related dispute status without emitting a second draw event.
- Why it might matter: off-chain accounting or monitoring may miss a state transition.
- Out-of-scope risk: event-only/reporting issues are usually not high severity unless they cause fund movement.
- Minimal local test idea: draw one conflict dispute and assert both statuses and emitted events.
- Result: local test confirmed one `DisputeDrawn` event is emitted while both linked disputes become `Drawn`.
- Rejection reason: this is an event-observability quirk without extra fund movement, and therefore not a strong bounty candidate.

## D4: Stake Changes Between Dispute Creation And Acceptance Can Change Slash Economics

- Status: rejected
- Asset: DisputeManager / Staking
- Hypothesis: if indexer stake changes after dispute creation, acceptance slashes the current stake instead of stake at the disputed time.
- Why it might matter: slash amount can be lower or higher than expected.
- Out-of-scope risk: current-stake slashing may be intended by the old contract design.
- Minimal local test idea: create a dispute, change stake, accept the dispute, and compare slash amount.
- Result: local test passed; after increasing stake post-dispute creation, acceptance slashed a percentage of the larger current stake.
- Rejection reason: this matches the contract implementation, which stores no stake snapshot and calls `getIndexerStakedTokens` during acceptance.

## D5: Reject/Draw Deposit Accounting Can Be Replayed Through Related Disputes

- Status: rejected
- Asset: DisputeManager
- Hypothesis: conflict-dispute status updates may allow deposit return or burn paths to be reached twice.
- Why it might matter: deposit accounting is direct value movement.
- Minimal local test idea: resolve one conflict dispute, then attempt accept/reject/draw on the related dispute and assert reverts or no balance changes.
- Result: local tests passed; after accepting or drawing one side, all accept/reject/draw attempts on the related dispute revert because it is no longer pending.
- Rejection reason: the `onlyPendingDispute` guard prevents replaying finalization on the related dispute.

## Picked First Test

D1 comes first because it touches direct slashing and the existing tests explicitly allow duplicate query disputes by different fishermen.

D1 local PoC confirmed the duplicate-slash behavior, then audit review rejected it as a candidate finding.

D2 and D3 were checked together because linked conflict dispute state and event behavior share the same path.

DisputeManager pass result: no reportable issue yet; D1 was real but known/audit-documented, and the remaining starter hypotheses were rejected as candidates.

Next best target: `BillingConnector`, because it is the next ranked asset with accounting and access-control behavior.
