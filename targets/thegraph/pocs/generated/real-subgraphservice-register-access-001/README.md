# Real Foundry Harness

Target: `thegraph`

Contract: `SubgraphService`

Hypothesis: `REGISTER-ACCESS-001`

This harness imports the real contract path and runs `forge test`.

Statuses are conservative:

- `compile_failed`: imports/remappings/mocks need work.
- `harness_needs_mocks`: constructor or setup is not wired.
- `clean`: generated compile smoke passed.

Generated tests alone are never report-ready.
