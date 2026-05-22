# RecurringAgreementManager Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`, `candidate`, `covered-existing-tests`, `likely-intended`.

## RAM1: Exact-Deficit JIT Top-Up Is Skipped

- Status: rejected-known-issue-risk
- Asset: `RecurringAgreementManager.beforeCollection`.
- Hypothesis: if `tokensToCollect > escrowBalance` and the manager's free GRT balance equals the exact deficit, the top-up is skipped because the code uses `<` instead of `<=`.
- Why it might matter: a collection can fail even though the manager holds exactly enough tokens to cover the missing escrow.
- Source evidence: `if (deficit < GRAPH_TOKEN.balanceOf(address(this))) { deposit(deficit); }`.
- Local model: `recurringagreementmanager-ram1-harness.js`.
- Solidity test added: `external/thegraph-contracts/packages/issuance/test/unit/agreement-manager/edgeCases.t.sol`.
- Verification status: JavaScript branch harness passes; Foundry test is pending because `forge` is not installed.
- Duplicate-risk result: high. Trust audit `TRST-M-2` covers the broader JIT failure class and explicitly references the `deficit >= balanceOf()` guard condition.
- Impact estimate: likely availability/accounting disruption, not theft.
- Next check: do not continue RAM1 unless reframed as a post-TRST-M-2 bypass with materially new evidence.

## RAM2: Escrow Basis Degradation Can Affect Unrelated Providers

- Status: likely-intended
- Asset: `_escrowMinMax` and `offerAgreement`.
- Hypothesis: one large agreement can reduce spare balance and degrade escrow mode globally, causing unrelated provider pairs to thaw proactive deposits.
- Why it might matter: cross-pair accounting behavior can surprise operators or reduce payment reliability.
- Result: the repository docs explicitly warn operators about this behavior.
- Evidence file: `external/thegraph-contracts/packages/issuance/contracts/agreement/RecurringAgreementManager.md`.
- Next check: treat as system-design risk, not a bug, unless an untrusted actor can trigger it.

## RAM3: Stale Escrow Snapshot Inflates Available Spare

- Status: covered-existing-tests
- Asset: `escrowSnap`, `totalEscrowDeficit`, and `_reconcileProviderEscrow`.
- Hypothesis: stale escrow snapshots can make the manager think it has more spare balance than it really does.
- Why it might matter: this could cause failed deposits or wrong basis selection.
- Result: `_reconcileProviderEscrow` syncs the live escrow snapshot before decisions, and tests cover staleness recovery.
- Evidence file: `external/thegraph-contracts/packages/issuance/test/unit/agreement-manager/escrowSnapStaleness.t.sol`.
- Next check: none for v1.

## RAM4: Dust Deposits Can Start Tiny Thaws That Block Larger Thaws

- Status: covered-existing-tests
- Asset: third-party `depositTo` plus RAM thaw threshold.
- Hypothesis: an attacker can dust-fund a provider pair and force tiny thaw activity that blocks useful thaw increases.
- Why it might matter: excess funds could be trapped longer than expected.
- Result: RAM uses `minThawFraction` as a threshold to avoid micro-thaw griefing.
- Evidence file: `external/thegraph-contracts/packages/issuance/test/unit/agreement-manager/updateEscrow.t.sol`.
- Next check: none unless the threshold can be bypassed.

## RAM5: Pause Split Leaves Collector Active While Manager Is Paused

- Status: likely-intended
- Asset: `RecurringAgreementManager` pause versus `RecurringCollector` pause.
- Hypothesis: if RAM is paused but the collector is not, collections may still happen when escrow is already funded, while reconciliation is delayed.
- Why it might matter: accounting can drift until unpaused.
- Result: source docs explicitly describe this cross-contract pause behavior.
- Evidence file: `external/thegraph-contracts/packages/issuance/contracts/agreement/RecurringAgreementManager.sol`.
- Next check: only relevant if pause assumptions in bounty scope treat drift as an accepted impact.

## Next Step

Create a concrete local test plan for RAM1, because it is the only new candidate in this pass.
