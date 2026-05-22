# Duplicate-Risk Gate

Use this before deeper PoC work.

## Goal

Estimate whether a lead is already publicly known, already fixed, covered by tests, documented as intended behavior, or likely to be rejected as a duplicate.

## Input

- Target name:
- Lead ID:
- One-sentence bug fingerprint:
- Asset:
- Functions and state variables:
- Suspected impact:
- Current evidence:

## Instructions

1. Restate the lead as a fingerprint: asset, root cause, broken invariant, and impact.
2. Generate 8 to 12 search phrases using exact function names, state variables, errors, comments, and impact wording.
3. Check these source groups: audits, GitHub issues, PRs, commits, release notes, docs, tests, forum/governance posts, and public bug writeups.
4. Separate exact matches from related-but-different findings.
5. Decide whether the lead is `low`, `medium`, or `high` duplicate risk.
6. If risk is medium or high, explain what new variant or bypass would be needed to continue.
7. Keep the output concise and practical.

## Output

```markdown
# Duplicate-Risk Result

## Fingerprint

## Search Phrases

## Sources Checked

## Matches Found

## Similar But Different

## Risk Rating

## Decision

## Next Step
```
