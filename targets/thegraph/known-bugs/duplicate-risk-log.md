# Duplicate-Risk Log

## RAM1

- Date checked: 2026-05-21
- Lead: exact-deficit JIT top-up skipped in `RecurringAgreementManager.beforeCollection`.
- Decision: reject as known / likely duplicate.
- Risk: high.
- Main source: Trust audit `TRST-M-2`.
- Reason: audit covers the broader JIT failure class and explicitly references the `deficit >= balanceOf()` guard condition.
- Workbench file: `targets/thegraph/reports/ram1-duplicate-risk.md`.
- Next action: only revisit as a post-audit bypass with materially new evidence.
