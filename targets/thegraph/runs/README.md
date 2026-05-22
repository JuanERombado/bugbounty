# The Graph Validation Runs

Each folder here is one local-only validation run.

Expected artifacts:

- `hypothesis-queue.json`: the candidate ideas being tested.
- `foundry-result.json`: command, stdout, stderr, and pass/fail status.
- `judgment.json`: conservative triage result.

Passing a generated scaffold does not mean a bug exists.

Only a real contract harness with reproducible failing behavior can become report evidence.
