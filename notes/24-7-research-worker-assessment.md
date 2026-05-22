# 24/7 Research Worker Assessment

The spare-desktop idea is worth pursuing, but only as a local, evidence-producing research worker with strict scope, time, and safety constraints.

## Honest Assessment

A 24/7 worker can help with:

- Running long local fuzz campaigns.
- Replaying invariant tests overnight.
- Backtesting the workflow against known public bugs.
- Ranking hotspots and producing concise morning summaries.
- Trying many local hypothesis variants without burning interactive attention.

It probably will not help if it is built as:

- An autonomous exploit hunter pointed at live systems.
- A broad scanner that produces thousands of weak alerts.
- A model-only agent that reads whole repos and guesses.
- A report generator without reproducible local proof.

## Best Version Of The Idea

Use the worker as an overnight local research queue:

1. Pull latest workbench config from GitHub.
2. Load one target scope file.
3. Select one approved local-only task.
4. Run bounded tooling such as Foundry tests, Echidna, Slither, Semgrep, or custom invariant checks.
5. Store artifacts under `runs/<date>/<target>/<task>/`.
6. Summarize only new evidence, failing tests, crashes, coverage gaps, and duplicate-risk hints.
7. Notify the main machine only when a result crosses a configured evidence threshold.

## Hardware View

An old desktop may be enough for:

- Static analysis.
- Small Foundry/Hardhat test loops.
- Lightweight Python orchestration.
- Overnight bounded fuzzing.

A newer Mac mini or small workstation helps if:

- Fuzzing runs are CPU-bound for many hours.
- Target repos need large dependency installs.
- You want multiple campaigns in parallel.
- You want quieter, lower-power 24/7 operation.

Start with the spare desktop before buying hardware.

## Important Design Rule

The worker should not decide that something is reportable.

It should produce evidence packages that a human and interactive AI review later.

## Worker Task Types

- Backtest a known vulnerability class against a local target.
- Run one invariant suite for a fixed time budget.
- Mutate one Foundry test around one hypothesis.
- Compare implementation behavior to documented invariants.
- Search for duplicate-risk evidence in local audits, issues, tests, and docs.
- Generate a short morning digest.

## Evidence Threshold For Notifications

Notify only when at least one is true:

- A local test fails in a way tied to an accepted impact.
- A fuzz run finds a reproducible minimal counterexample.
- A static finding overlaps a high-value asset and a paid impact.
- A duplicate-risk search finds a strong reason to stop a lead.
- A new invariant cannot be proven or rejected after the time budget.

## Recommended Next Build Step

Add a `worker/` module that can run one bounded job from a JSON queue and write a normalized result artifact.

Do not add autonomous target crawling or live testing.
