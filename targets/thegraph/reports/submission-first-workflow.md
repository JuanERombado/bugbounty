# Submission-First Workflow

Start with the report we need Immunefi triage to accept, then work backward.

## Final Artifact

A submission-ready report must prove all of this:

- The affected asset is explicitly in scope.
- The selected impact is explicitly accepted by the bounty.
- The bug is not a known audit issue or listed exclusion.
- Duplicate risk has been checked against public sources and existing tests.
- The PoC is complete, runnable, and local-only.
- The reproduction steps are clear enough for triage to run without guessing.
- The impact is explained in plain English without exaggeration.
- No live system, public mainnet, or public testnet was attacked.

## Backward Chain

1. Report: can we write a precise title, summary, impact, root cause, and fix?
2. Evidence: do we have code links, test output, configs, commands, and environment notes?
3. PoC: does one local test prove the bug and the impact?
4. Duplicate risk: have we checked public sources, audits, tests, issues, PRs, commits, docs, and forum posts?
5. Hypothesis: is the idea a small claim that can be confirmed or rejected?
6. Threat model: does the idea touch funds, roles, state transitions, or cross-chain assumptions?
7. Contract map: do we know which functions, modifiers, and storage are involved?
8. Asset ranking: is this asset worth high-critical research time?
9. Scope: is the asset and impact eligible under Immunefi and target rules?

## Stop Rules

- Stop if the asset is not in scope.
- Stop if the impact does not map to a paid severity.
- Stop if the required exploit step is prohibited.
- Stop if the issue is already known and not a genuine bypass.
- Stop or reframe if duplicate risk is high and there is no clear new variant.
- Stop if the PoC cannot be made local and reproducible.

## Report Skeleton

Use this order:

1. Title
2. Summary
3. In-scope asset
4. Accepted impact
5. Affected code
6. Root cause
7. Local reproduction steps
8. PoC code
9. Expected result
10. Actual result
11. Impact
12. Suggested fix
13. Scope, rules, known-issue, and duplicate-risk checklist

One-sentence rule: every research task exists to fill or reject one report section.
