# Foundry Starter Harness

This is a local-only starter harness for turning hypotheses into tests.

## Setup

Install Foundry, then from this folder run:

```powershell
forge test -vv
```

## Usage

1. Copy the relevant contract or create a minimal mock in `src/`.
2. Add one hypothesis test in `test/`.
3. Keep the test focused on setup, action, and assertion.
4. Do not broadcast transactions.
5. Do not test against public deployments.

The included test is intentionally simple; replace it once you have a real local hypothesis.
