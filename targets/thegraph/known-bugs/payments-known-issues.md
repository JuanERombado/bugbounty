# Payments Known Issues

## TRST-M-2 / RAM1 Overlap

- ID: `TRST-M-2`
- Source: `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf`
- Asset: `RecurringAgreementManager`
- Root cause: JIT fallback/top-up path can fail when escrow is short and RAM cannot top up.
- Affected functions: `beforeCollection`, `PaymentsEscrow.collect`, JIT escrow/reconciliation path.
- Impact class: payment availability / collection failure.
- Status: fixed in audit; RAM1 treated as high duplicate-risk.
- Why not to pursue: RAM1's exact-deficit condition is a subset of the audit's `deficit >= balanceOf()` condition.
- Possible valid variant: a post-fix bypass through a new call path, updated mitigation assumption, or different collector/service flow.
- Search terms: `TRST-M-2`, `beforeCollection`, `JIT top-up`, `deficit >= balanceOf`, `RecurringAgreementManager`.

## TRST-H-3

- ID: `TRST-H-3`
- Source: `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf`
- Asset: `RecurringAgreementManager`
- Root cause: stale escrow snapshot can cause a perpetual revert loop.
- Affected functions: escrow snapshot and reconciliation paths.
- Impact class: payment/reconciliation availability.
- Status: fixed in audit.
- Why not to pursue: known high-severity audit issue.
- Possible valid variant: only if current code reintroduces stale snapshot drift through a new state path.
- Search terms: `stale escrow snapshot`, `escrowSnap`, `totalEscrowDeficit`, `reconcileProviderEscrow`.

## TRST-M-1

- ID: `TRST-M-1`
- Source: `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf`
- Asset: `RecurringAgreementManager`, `PaymentsEscrow`
- Root cause: micro-thaw griefing via permissionless `depositTo` and reconciliation.
- Affected functions: `depositTo`, `reconcileAgreement`, thaw adjustment logic.
- Impact class: griefing / delayed excess withdrawal.
- Status: mitigated or acknowledged by residual/thaw threshold design.
- Why not to pursue: known medium audit issue.
- Possible valid variant: threshold bypass causing meaningful locked funds or repeated thaw disruption.
- Search terms: `micro-thaw`, `depositTo`, `minThawFraction`, `minResidualEscrowFactor`.

## TRST-M-3

- ID: `TRST-M-3`
- Source: `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf`
- Asset: `RecurringAgreementManager`
- Root cause: new agreement offers can degrade escrow mode from Full to OnDemand globally.
- Affected functions: `offerAgreement`, `offerAgreementUpdate`, `_escrowMinMax`.
- Impact class: payment reliability / operator-driven escrow mode degradation.
- Status: acknowledged and documented.
- Why not to pursue: known audit issue and documented operator caution.
- Possible valid variant: untrusted actor can force degradation or create direct fund loss.
- Search terms: `instant escrow mode degradation`, `Full to OnDemand`, `sumMaxNextClaim`, `totalEscrowDeficit`.

## TRST-M-4

- ID: `TRST-M-4`
- Source: `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf`
- Asset: `RecurringCollector`
- Root cause: return-data bombing via payer callbacks.
- Affected functions: `_preCollectCallbacks`, `_postCollectCallback`.
- Impact class: gas griefing / payment availability.
- Status: fixed in audit.
- Why not to pursue: known medium audit issue.
- Possible valid variant: a callback path still copies unbounded returndata or bypasses gas checks.
- Search terms: `returndata bombing`, `payer callbacks`, `beforeCollection`, `afterCollection`.

## TRST-H-1

- ID: `TRST-H-1`
- Source: `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf`
- Asset: `RecurringCollector`
- Root cause: payer callback gas siphoning through the 63/64 gas rule.
- Affected functions: collection callbacks.
- Impact class: collection bypass / payment availability.
- Status: fixed in audit.
- Why not to pursue: known high audit issue.
- Possible valid variant: a remaining callback path can still starve payment execution.
- Search terms: `63/64`, `gas siphoning`, `collection callbacks`.

## TRST-H-2

- ID: `TRST-H-2`
- Source: `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf`
- Asset: `RecurringCollector`
- Root cause: invalid `supportsInterface()` returndata escapes try/catch.
- Affected functions: interface support checks.
- Impact class: collection bypass / agreement acceptance disruption.
- Status: fixed in audit.
- Why not to pursue: known high audit issue.
- Possible valid variant: malformed interface detection still escapes or blocks in current code.
- Search terms: `supportsInterface`, `malformed ERC165`, `invalid returndata`.

## TRST-H-4

- ID: `TRST-H-4`
- Source: `external/thegraph-contracts/packages/issuance/audits/2026-05-09_Graph_PR1334_v05.pdf`
- Asset: payer/callback flow.
- Root cause: EOA payer can acquire code via EIP-7702 and block collection.
- Affected functions: payer callback assumptions.
- Impact class: collection bypass / payment availability.
- Status: fixed in audit.
- Why not to pursue: known high audit issue.
- Possible valid variant: EIP-7702 or code-changing payer behavior bypasses current assumptions.
- Search terms: `EIP-7702`, `EOA payer`, `callback gas griefing`, `payer code change`.
