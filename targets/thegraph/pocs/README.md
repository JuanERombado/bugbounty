# PoCs

Use this folder for local-only proof-of-concept work.

Recommended flow:

1. Start with a hypothesis in `targets/thegraph/hypotheses/`.
2. Create the smallest local test that proves or rejects it.
3. Prefer mocks before local forks.
4. Log the exact command and result.
5. Move to report drafting only after the test proves an accepted impact.

Never test against public mainnet or public testnet deployments.
