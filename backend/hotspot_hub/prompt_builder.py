"""Build focused LLM prompts from selected hotspots."""

from __future__ import annotations

from pathlib import Path

from .models import Hotspot


MAX_CODE_CHARS = 18_000


def build_hotspot_prompt(target_root: Path, hotspot: Hotspot) -> dict[str, str]:
    source_path = target_root / hotspot.path
    code = source_path.read_text(encoding="utf-8", errors="ignore")[:MAX_CODE_CHARS]
    findings = "\n".join(
        f"- {finding.severity.upper()} {finding.rule_id} at line {finding.location.start_line}: {finding.message}"
        for finding in hotspot.findings
    ) or "- none"
    return {
        "system": (
            "You are a smart contract security reviewer. Analyze only the provided local code and alerts. "
            "Do not suggest live-system testing. Focus on reproducible local PoC ideas."
        ),
        "user": f"""Target file: {hotspot.path}
Hotspot score: {hotspot.score}
Reasons: {", ".join(hotspot.reasons)}
Static findings:
{findings}

Tasks:
1. Explain the security-relevant logic in plain English.
2. List realistic bug hypotheses ranked by impact and testability.
3. For each hypothesis, propose a local Foundry/Hardhat test idea.
4. Reject weak or duplicate-looking ideas explicitly.

Code:
```text
{code}
```""",
    }
