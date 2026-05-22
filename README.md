# Bug Bounty Workbench

AI-assisted, local-only workflow for responsible bug bounty research.

First target: [The Graph Immunefi program](https://immunefi.com/bug-bounty/thegraph/information/#top).

## Guardrails

- Do not attack live systems.
- Do not test against public mainnet or public testnet deployments.
- Use local repo analysis, local tests, and local forks only.
- Do not run traffic-heavy scanners.
- Do not build phishing, social engineering, DoS, or exploit automation.
- Produce Immunefi-style report drafts only after a finding is confirmed with a reproducible local PoC.

## Folder Map

- `targets/thegraph/scope/`: bounty scope schema and target scope JSON.
- `targets/thegraph/assets/`: ranked asset maps and investigation queues.
- `targets/thegraph/audits/`: audit links, known-issue notes, and audit review notes.
- `targets/thegraph/known-bugs/`: no-tread map for public audit findings, duplicate-risk decisions, and known issue classes.
- `targets/thegraph/code-map/`: local code summaries generated from cloned repos.
- `targets/thegraph/hypotheses/`: candidate bug hypotheses and triage notes.
- `targets/thegraph/pocs/`: local-only PoC plans and test harnesses.
- `targets/thegraph/reports/`: report drafts for confirmed issues only.
- `scripts/`: small repeatable helpers.
- `prompts/`: copy/paste AI prompt templates.
- `notes/`: personal notes and scratchpads.

## Workflow

The workflow is report-first: every step exists to fill or reject a final Immunefi submission.

1. Define the final report: read `targets/thegraph/reports/submission-first-workflow.md`.
2. Gate scope and impact: confirm the asset and accepted impact in `targets/thegraph/scope/thegraph.scope.json`.
3. Gate exclusions: reject ideas that need prohibited activity or out-of-scope impact.
4. Gate known issues: check audits and known-issue sources before PoC work.
5. Rank assets: run `python scripts/rank_assets.py targets/thegraph/scope/thegraph.scope.json`.
6. Map code: run `python scripts/map_contracts.py external/thegraph-contracts --scope targets/thegraph/scope/thegraph.scope.json --out targets/thegraph/code-map/contracts-map.md`.
7. Explain one contract: use `prompts/contract-explainer.md`.
8. Threat-model one asset: use `prompts/threat-modeler.md`.
9. Write one hypothesis: use `prompts/bug-hypothesis-generator.md`.
10. Gate duplicate risk: use `prompts/duplicate-risk-gate.md`, `targets/thegraph/reports/duplicate-risk-template.md`, and `targets/thegraph/known-bugs/`.
11. Plan one local PoC: use `prompts/poc-test-planner.md`.
12. Build evidence: use `prompts/evidence-builder.md`.
13. Check readiness: run `python scripts/check_submission_readiness.py targets/thegraph/reports/finding-dossier.example.json`.
14. Draft report: use `prompts/immunefi-report-drafter.md` only after the readiness check passes on a real dossier.

## First Commands

```powershell
cd "C:\Users\jromb\VibeCoded Projects\bugbounty\bug-bounty-workbench"
python scripts/rank_assets.py targets/thegraph/scope/thegraph.scope.json
python scripts/map_contracts.py external/thegraph-contracts --scope targets/thegraph/scope/thegraph.scope.json --out targets/thegraph/code-map/contracts-map.md
python scripts/check_submission_readiness.py targets/thegraph/reports/finding-dossier.example.json
```

## GUI

Start the local visualization app:

```powershell
python -m backend.hotspot_hub.server --host 127.0.0.1 --port 4173
```

Then open `http://localhost:4173`.

The GUI can initialize a new Immunefi target, show the process map, pipeline, duplicate-risk gate, severity playbooks, All Stars-inspired workflow patterns, the ranked asset queue, and local-only analyzer commands.

CLI fallback for target initialization:

```powershell
python -m backend.hotspot_hub.cli target init "https://immunefi.com/bug-bounty/thegraph/information/#top"
```

## Hotspot Hub Backend

Run the reusable local scanner backend:

```powershell
python -m backend.hotspot_hub.cli scan "external/thegraph-contracts" --out "targets/thegraph/code-map/hotspot-report.json"
```

Then build a focused LLM prompt for one selected hotspot:

```powershell
python -m backend.hotspot_hub.cli prompt "targets/thegraph/code-map/hotspot-report.json" "packages/subgraph-service/contracts/libraries/IndexingAgreement.sol"
```

Tooling disk-space plan: `knowledge/tooling-size-plan.md`.

## Exploit-Validation Slice

Generate three invariant ideas, create a Foundry scaffold, run `forge test`, and store the result:

```powershell
python -m backend.hotspot_hub.cli validate foundry-slice --target thegraph --contract-name SubgraphService --contract-path external/thegraph-contracts/packages/subgraph-service/contracts/SubgraphService.sol
```

Artifacts are written to:

- `targets/thegraph/runs/<run-id>/`
- `targets/thegraph/pocs/generated/<run-id>/`

A passing generated scaffold is not report evidence; it only proves the local validation loop works.

## Local Research Worker

Run bounded local jobs without manually approving each hypothesis step:

```powershell
python -m backend.hotspot_hub.cli worker run queues/thegraph-smoke.worker.json
```

Worker results are written under `targets/<target>/runs/<run-id>/`.

The worker is for local evidence production only; use local or frontier LLMs to review compact artifacts after deterministic tools run.

Generate a queue from a hotspot report:

```powershell
python -m backend.hotspot_hub.cli worker generate targets/thegraph/code-map/hotspot-report.json --out queues/thegraph-hotspots.worker.json --max-hotspots 5
```

Then run it:

```powershell
python -m backend.hotspot_hub.cli worker run queues/thegraph-hotspots.worker.json
```

## Add A New Bounty

```powershell
python scripts/new_target.py "Example Protocol" --program-url "https://example.com/bug-bounty"
```

Then fill the new scope JSON, run the ranking script against it, and use the same prompts and local PoC workflow.

## Current Priority

Start with staking, rewards, curation, disputes, bridge/cross-chain logic, accounting/state transitions, and permission/access-control logic.

The first ranked attack map is in `targets/thegraph/assets/ranked-assets.md`.
