# Gemini Handoff

This repo is a local-only bug bounty workbench for Immunefi-style Web3 research.

## North Star

The workflow is report-first: every lead must eventually map to an in-scope asset, accepted paid impact, duplicate-risk decision, local PoC, and Immunefi-style report draft.

## Hard Guardrails

- Do not attack live systems.
- Do not test against public mainnet or public testnet deployments.
- Use local repo analysis, local tests, and local forks only.
- Do not run traffic-heavy scanners.
- Do not build phishing, social engineering, DoS, or exploit automation.
- Draft reports only for confirmed issues with reproducible local evidence.

## Current Target

- Target: The Graph Immunefi program.
- Scope source: `targets/thegraph/scope/thegraph.scope.json`.
- First ranked attack map: `targets/thegraph/assets/ranked-assets.md`.
- Known-issue and duplicate-risk area: `targets/thegraph/known-bugs/`.
- Current learning emphasis: staking, rewards, curation, disputes, bridge/cross-chain logic, accounting/state transitions, and permission/access-control logic.

## App Architecture

- `app/`: browser dashboard for the workflow.
- `backend/hotspot_hub/`: local Python backend and scanner orchestration.
- `scripts/`: simple repeatable target/code mapping helpers.
- `prompts/`: reusable LLM prompt templates.
- `targets/`: target-specific scope, maps, hypotheses, PoC plans, and report artifacts.
- `knowledge/`: reusable bug bounty/tooling knowledge base.

## Dashboard

Run from repo root:

```powershell
python -m backend.hotspot_hub.server --host 127.0.0.1 --port 4173
```

If 4173 is already in use, use another port:

```powershell
python -m backend.hotspot_hub.server --host 127.0.0.1 --port 4174
```

The dashboard has a New Project page that accepts an Immunefi URL and initializes `targets/<slug>/` without overwriting an existing scope file.

## Target Initialization

GUI endpoint:

```text
POST /api/projects/initialize
```

CLI fallback:

```powershell
python -m backend.hotspot_hub.cli target init "https://immunefi.com/bug-bounty/thegraph/information/#top"
```

Current behavior:

- Fetches one public Immunefi program page.
- Creates target folders.
- Writes `scope/<slug>.initializer.latest.json`.
- Writes `scope/<slug>.scope.json` only if it does not already exist.
- Marks generated scope as `needs_manual_scope_review`.

Next improvement:

- Extract structured assets, accepted impacts, exclusions, audits, and resource links into editable GUI sections.

## Local Scanner Backend

Run a hotspot scan:

```powershell
python -m backend.hotspot_hub.cli scan "external/thegraph-contracts" --out "targets/thegraph/code-map/hotspot-report.json"
```

Build a focused LLM prompt from one hotspot:

```powershell
python -m backend.hotspot_hub.cli prompt "targets/thegraph/code-map/hotspot-report.json" "packages/subgraph-service/contracts/libraries/IndexingAgreement.sol"
```

Inspect installed tools:

```powershell
python -m backend.hotspot_hub.cli tools status
```

Installed locally on this machine, but intentionally not committed:

- Foundry under `.tools/foundry`.
- Slither under `.tools/slither`.
- Semgrep under `.tools/semgrep`.

See `knowledge/tooling-size-plan.md`.

## Current Research State

Important prior result:

- `RAM1` was stopped by duplicate-risk review because it overlapped Trust audit `TRST-M-2`.
- Duplicate-risk gates are first-class workflow steps now, not afterthoughts.

Recent focus:

- Payment flows around `SubgraphService`, `PaymentsEscrow`, `RecurringCollector`, and `RecurringAgreementManager`.
- `targets/thegraph/code-map/subgraphservice-payment-flow-summary.md`.
- `targets/thegraph/hypotheses/subgraphservice-payment-flow-hypotheses.md`.

Do not treat existing hypotheses as findings.

## Recommended Next Steps

1. Improve the New Project initializer to parse Immunefi pages into structured editable scope sections.
2. Add a dashboard Tool Layer page for Foundry, Slither, Semgrep, and future code-slicing tools.
3. Add `gfunc` or equivalent function-level Solidity slicing for targeted LLM prompts.
4. Continue The Graph locally from the SubgraphService payment-flow lane.
5. For every new lead, run scope, impact, exclusion, known-issue, and duplicate-risk gates before PoC work.

## Verification Commands

```powershell
python -m compileall -q backend
python scripts/rank_assets.py targets/thegraph/scope/thegraph.scope.json
python scripts/check_submission_readiness.py targets/thegraph/reports/finding-dossier.example.json
```

Expected readiness checker behavior:

- Example dossiers may fail until they contain real confirmed evidence.
- Failure is useful when it prevents premature or duplicate submissions.

## Git Hygiene

Do not commit:

- `external/`
- `.tools/`
- local build caches
- node modules
- raw saved HTML pages in `notes/*.html`

The committed repo should contain the workbench code, prompts, summaries, target metadata, and reproducible local workflow artifacts.
