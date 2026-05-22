# Bug Hypothesis Generator Prompt

Generate beginner-friendly bug hypotheses for this in-scope asset.

Hard limits:

- No live-system attack steps.
- No mainnet or public testnet testing.
- No DoS, phishing, social engineering, or traffic-heavy scanning.
- Every hypothesis must map to an accepted Immunefi impact or be labeled "probably not in scope".
- Known audit issues must be checked before escalation.

For each hypothesis, provide:

- Hypothesis:
- Why it might happen:
- Impact if true:
- Scope fit:
- Out-of-scope risk:
- Minimal local test idea:
- What evidence would reject it:

Input:

```text
[paste ranked asset, contract summary, and relevant functions]
```
