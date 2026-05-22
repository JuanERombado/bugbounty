# Threat Modeler Prompt

Threat-model this in-scope asset for local-only research.

Context:

- Target: The Graph Immunefi bounty.
- Testing must be local repo analysis, local tests, or local forks only.
- Do not include phishing, social engineering, DoS, traffic-heavy scanning, public mainnet testing, or public testnet testing.
- Accepted impacts are direct significant user-fund loss from protocol contracts, private information theft, non-basic economic attacks causing significant direct user-fund loss, and participant impersonation causing unwanted actions.

Output:

1. Assets at risk.
2. Trusted roles and permissions.
3. External dependencies.
4. State transitions worth testing.
5. Accounting invariants.
6. Cross-contract or cross-chain assumptions.
7. Out-of-scope traps.
8. Top 5 local-only test directions.

Input:

```text
[paste scope entry, contract summary, and relevant code map lines]
```
