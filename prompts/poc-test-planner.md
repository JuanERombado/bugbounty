# PoC Test Planner Prompt

Turn this hypothesis into a local Foundry or Hardhat test plan.

Rules:

- Local execution only.
- Use mocks for external systems unless a local fork is explicitly required.
- Do not require external downloads in the final report PoC.
- Prefer one clear failing assertion over a large scenario.
- Include setup, action, assertion, and rejection criteria.

Output:

- Test name:
- Framework:
- Contracts/mocks needed:
- Setup:
- Action:
- Expected vulnerable result:
- Expected safe result:
- Assertions:
- Data to log:
- Rejection criteria:
- Notes for Immunefi report if confirmed:

Hypothesis:

```text
[paste one hypothesis here]
```
