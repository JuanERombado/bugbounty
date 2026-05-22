# Immunefi Report Drafter Prompt

Draft an Immunefi-style report from a confirmed local PoC.

Do not exaggerate. If evidence is missing, say so.
If any readiness check fails, stop and output "NOT READY" with the missing evidence.

Required checks:

- The asset is listed in scope.
- The impact matches an accepted impact.
- The issue is not a known audit issue.
- The PoC is reproducible locally.
- No live-system testing was performed.
- The reproduction steps include every dependency, config, command, and expected output needed to rerun the PoC.
- The report is not a placeholder, scanner dump, or AI-generated claim without demonstrated impact.

Output:

1. Title
2. Summary
3. In-scope asset
4. Accepted impact
5. Affected code
6. Root cause
7. Local reproduction steps
8. PoC
9. Expected result
10. Actual result
11. Impact
12. Suggested fix
13. Scope and rules checklist

Input:

```text
[paste confirmed hypothesis, test output, code snippets, and scope notes]
```
