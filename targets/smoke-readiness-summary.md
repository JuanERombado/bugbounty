# Smoke Readiness Summary

Run date: 2026-05-22

## Environment Sanity

- Command: `python -m backend.hotspot_hub.cli --help`
- Status: passed
- Evidence: CLI imported and listed `scan`, `prompt`, `tools`, `target`, `validate`, `hypotheses`, `worker`, and `llm`.
- Command: `forge --version`
- Status: repo-local Foundry passed after prepending `.tools\foundry\bin` to PATH.
- Evidence: `forge Version: 1.7.1`.
- Note: plain shell PATH did not include `forge`, so future smoke runs should use the repo-local Foundry path or update the user PATH.

## Seeded Fixture

- Command: `python -m backend.hotspot_hub.cli validate fixture-slice --fixture vulnerable-vault`
- Status: reproduced
- Fixture reproduced: yes
- Evidence path: `targets/fixtures/runs/vulnerable-vault-fixture-slice/judgment.json`
- Vulnerable result: `targets/fixtures/runs/vulnerable-vault-fixture-slice/vulnerable-result.json`
- Fixed result: `targets/fixtures/runs/vulnerable-vault-fixture-slice/fixed-result.json`
- Confirmation: vulnerable run returned nonzero and fixed run returned zero.
- Report ready: false

## Deterministic Hypotheses

- Command: `python -m backend.hotspot_hub.cli hypotheses generate --provider canned --hotspot-report queues/examples/hotspot-report.example.json --out targets/thegraph/hypotheses/generated.json`
- Status: passed
- Provider: canned
- Count: 1
- Evidence path: `targets/thegraph/hypotheses/generated.json`
- Report ready: false

## Local LLM Ping

- Command: `python -m backend.hotspot_hub.cli llm ping`
- Status: passed after adapter compatibility fix
- Result: local endpoint exposed `qwen/qwen3.5-9b` and returned reasoning-model output.
- Pipeline impact: non-blocking because canned hypotheses work without a model provider.

## Real Foundry Compile Smoke

- Command: `python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id SMOKE-001`
- Status: clean
- Interpretation: compile/import smoke passed only; this is not evidence that the contract has no bug.
- Run path: `targets/thegraph/runs/real-2026-05-22T180919-subgraphservice-smoke-001/`
- Generated harness path: `targets/thegraph/pocs/generated/real-2026-05-22T180919-subgraphservice-smoke-001/`
- Report ready: false

## Stop/Go Decision

- Go: fixture-slice reproduced the seeded bug and canned hypotheses generated correctly.
- Next blocker: wire one real target contract with proper mocks/setup and replace the smoke assertion with a real invariant.
- Next build phase: wire one real target contract with proper mocks/setup and replace the smoke assertion with a real invariant.
