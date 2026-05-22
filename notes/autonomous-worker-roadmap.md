# Autonomous Worker Roadmap

The workbench should stop asking the user for every next step.

## Correct Thesis

AI should generate or rank hypotheses, but only executable local evidence should decide what survives.

## Runtime Tiers

1. Deterministic local tools: ranking, Semgrep, Slither, Foundry, Echidna, Medusa, grep, and duplicate-risk searches.
2. Local LLM: cheap hypothesis expansion, summarization, and morning digests.
3. Frontier LLM: expensive review only for compact evidence packages, test failures, and report-quality reasoning.
4. Human: final scope, impact, duplicate, ethics, and submission decisions.

## Continuous Loop

```text
scope -> asset queue -> hotspot -> hypothesis -> local test/fuzz job -> artifact -> judge -> keep/kill/escalate
```

## Worker Rules

- Run only inside the local workspace.
- Never attack live systems.
- Use bounded timeouts and small queues.
- Store every result under `targets/<target>/runs/`.
- Notify only when a reproducible failure or strong duplicate-risk signal appears.
- Treat model output as a proposal, not evidence.

## V1 Implemented

The CLI now has a bounded queue runner:

```powershell
python -m backend.hotspot_hub.cli worker run queues/thegraph-smoke.worker.json
```

This executes local commands from JSON, captures stdout/stderr/exit code, and writes a `worker-summary.json`.

## Next Build Milestones

1. Add a queue generator that converts ranked hotspots into safe worker jobs.
2. Add a local LLM adapter for Ollama or LM Studio using compact prompt templates.
3. Add a result classifier that marks jobs as `dead`, `needs_mutation`, `promising`, or `escalate_frontier`.
4. Add a dashboard page for worker queues, running jobs, artifacts, and evidence thresholds.
5. Backtest the worker against known vulnerable training contracts before trusting it on live bounty targets.

## Practical Goal

The user should spend premium Codex/Gemini time improving the machine and reviewing high-signal evidence, not manually advancing every hypothesis branch.
