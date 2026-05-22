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

## Architecture

The workbench is a lean exploit-validation system:

1. Local scanners and code maps rank attack surface.
2. Canned or local model providers generate hypotheses.
3. Foundry fixtures and real harnesses decide whether a hypothesis survives.
4. Result judges mark evidence status conservatively.
5. Reports stay blocked until a reproducible local PoC and scope/impact gates exist.

AI output is untrusted until local tests prove it.

## Fixture Demo

Before using a real bounty target, prove the pipeline on a seeded vulnerable fixture:

```powershell
python -m backend.hotspot_hub.cli validate fixture-slice --fixture vulnerable-vault
```

Expected status: `reproduced`.

The vulnerable vault has a withdrawal-accounting bug and an access-control bug; the fixed vault in the same fixture must pass.

## Exploit-Validation Slice

Generate three invariant ideas, create a Foundry scaffold, run `forge test`, and store the result:

```powershell
python -m backend.hotspot_hub.cli validate foundry-slice --target thegraph --contract-name SubgraphService --contract-path external/thegraph-contracts/packages/subgraph-service/contracts/SubgraphService.sol
```

Artifacts are written to:

- `targets/thegraph/runs/<run-id>/`
- `targets/thegraph/pocs/generated/<run-id>/`

A passing generated scaffold is not report evidence; it only proves the local validation loop works.

The legacy generated Foundry command is now explicitly `scaffold_only`.

## Real Foundry Slice

Generate a real-contract compile smoke harness:

```powershell
python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id SMOKE-001
```

Run the first meaningful The Graph invariant slice:

```powershell
python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id OWNER-ACCESS-001 --run-id real-subgraphservice-owner-access-001
```

This local-only harness deploys `SubgraphService` through an `ERC1967Proxy`, uses a mock Graph controller, and checks that non-owners cannot change economic settings while the owner can.

First registration gate slice:

```powershell
python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id REGISTER-ACCESS-001 --run-id real-subgraphservice-register-access-001
```

This local-only harness adds mock Horizon staking and dispute-manager dependencies, then checks that an authorized indexer with a valid provision can register while unauthorized or unprovisioned registration attempts revert.

Possible statuses include `compile_failed`, `harness_needs_mocks`, `test_failed`, `invariant_failed_promising`, and `clean`.

Compile failures are harness work, not security findings.

## Model Providers

Hypothesis generation works without any model keys:

```powershell
python -m backend.hotspot_hub.cli hypotheses generate --provider canned --hotspot-report queues/examples/hotspot-report.example.json --out targets/thegraph/hypotheses/generated.json
```

Optional providers:

- `ollama`: enabled only when `OLLAMA_BASE_URL` is set.
- `openai`: enabled only when `OPENAI_API_KEY` is set.

Local or frontier models generate hypotheses only; Foundry/Echidna/Slither/local tools decide truth.

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

Check LM Studio connectivity:

```powershell
python -m backend.hotspot_hub.cli llm ping
```

The ping command lists loaded local models, uses the requested model when available, and accepts `reasoning_content` as valid health-check output for reasoning models that do not emit final `content` during short pings.

Generate a queue that sends hotspots to the local model:

```powershell
python -m backend.hotspot_hub.cli worker generate targets/thegraph/code-map/hotspot-report.json --out queues/thegraph-local-llm.worker.json --max-hotspots 5 --mode local-llm
```

## Add A New Bounty

```powershell
python scripts/new_target.py "Example Protocol" --program-url "https://example.com/bug-bounty"
```

Then fill the new scope JSON, run the ranking script against it, and use the same prompts and local PoC workflow.

## Current Priority

Start with staking, rewards, curation, disputes, bridge/cross-chain logic, accounting/state transitions, and permission/access-control logic.

The first ranked attack map is in `targets/thegraph/assets/ranked-assets.md`.
