# Duplicate-Risk Check

## Lead

- Lead ID: RAM1
- Asset: `RecurringAgreementManager.beforeCollection`
- Status: `completed`
- One-sentence fingerprint: exact-deficit just-in-time escrow top-up may be skipped because `deficit < balance` excludes `deficit == balance`.
- Suspected accepted impact: payment/collection disruption if a valid collection cannot be funded despite exact available balance.

## Root-Cause Terms

- Contract: `RecurringAgreementManager`
- Functions: `beforeCollection`, `PAYMENTS_ESCROW.deposit`
- State variables: `escrowSnap`, `totalEscrowDeficit`, provider-pair escrow balance
- Errors/events: `EscrowFunded`
- Comments or docs wording: `JIT top-up`, `deposit only when escrow balance cannot cover this collection`
- Invariant: if manager free balance is enough to cover the deficit, escrow should be topped up before collection.

## Search Phrases

- `"RecurringAgreementManager" "beforeCollection" "deficit <"`
- `"beforeCollection" "JIT top-up" "deficit"`
- `"Exact-deficit" "JIT" "RecurringAgreementManager"`
- `"tokensToCollect" "escrowBalance" "deficit"`
- `"RecurringAgreementManager" "EscrowFunded"`
- `"PaymentsEscrow" "deposit" "beforeCollection"`
- `"getMaxNextClaim" "JIT top-up"`

## Sources Checked

- [x] Bounty page and resources
- [x] Scope and out-of-scope rules
- [x] Audits
- [x] GitHub issues
- [ ] Pull requests
- [x] Commit history
- [ ] Release notes
- [x] Docs
- [x] Existing tests
- [ ] Forum or governance posts
- [ ] Public bug writeups

## Findings

| Source | Match Type | Notes | Link or File |
| --- | --- | --- | --- |
| Existing local tests | similar | There is a no-deficit boundary test for `tokensToCollect == escrowBalance`, but not the exact-deficit boundary. | `external/thegraph-contracts/packages/issuance/test/unit/agreement-manager/edgeCases.t.sol` |
| Local git history | similar | Only the current visible commit was available for this file path; grep across git history found the current `deficit < GRAPH_TOKEN.balanceOf(address(this))` guard and related JIT tests. | `external/thegraph-contracts/packages/issuance/contracts/agreement/RecurringAgreementManager.sol` |
| GitHub issues API | none | Unauthenticated issue search for exact RAM/beforeCollection/deficit phrases returned zero issues. | `https://api.github.com/search/issues` |
| GitHub code API | blocked | GitHub code search API requires authentication, so exact remote code search could not be completed through the API. | `https://api.github.com/search/code` |
| Issuance audit PDF | exact / known issue | Trust audit `TRST-M-2` describes the JIT failure path and explicitly says that if RAM lacks free balance and the `deficit >= balanceOf()` guard fails, `beforeCollection` returns without action and the following escrow collect reverts. RAM1's exact-deficit case is a subset of this known condition. | `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf` |
| Local docs | similar | RAM docs describe JIT as a safety net and Trust Model docs say receivers depend on RAM funding logic outside Full mode. | `external/thegraph-contracts/packages/issuance/contracts/agreement/RecurringAgreementManager.md`; `external/thegraph-contracts/docs/PaymentsTrustModel.md` |

## Duplicate Risk

- Rating: `high`
- Reason: local audit `TRST-M-2` covers the same JIT failure class and includes the `deficit >= balanceOf()` guard condition that RAM1 relies on.
- What would make this non-duplicate: a materially new variant after the `TRST-M-2` mitigation, such as a different call path, different state transition, or bypass of the documented mitigation/reconciliation assumptions.

## Decision

- [ ] Continue to local PoC
- [ ] Reframe as a variant or bypass
- [x] Reject as known or likely duplicate
- [ ] Park as learning note

## Next Step

Do not continue RAM1 as currently framed; either reframe it as a post-TRST-M-2 bypass with new evidence, or move to the next payments path such as `SubgraphService`.
