# Known Bugs / No-Tread Map

This folder tracks public audit findings, documented risks, existing tests, and duplicate-risk discoveries.

Use it before deeper PoC work.

## Rule

If a lead overlaps a known issue, stop unless you can describe a materially new variant, bypass, affected version, or impact path.

## Files

- `duplicate-risk-log.md`: decisions from duplicate-risk gates.
- `payments-known-issues.md`: payment, escrow, collector, and agreement-manager no-tread areas.
- `audits-index.md`: audit sources checked for known issues.
- `no-tread-patterns.md`: reusable root-cause patterns that tend to be crowded or already covered.

## Entry Format

```text
ID:
Source:
Asset:
Root cause:
Affected functions:
Impact class:
Status:
Why not to pursue:
Possible valid variant:
Search terms:
```
