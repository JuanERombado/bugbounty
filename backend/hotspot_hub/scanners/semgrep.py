"""Semgrep scanner adapter."""

from __future__ import annotations

import json
from pathlib import Path

from ..models import CodeLocation, Finding, ScannerRun, relative_path
from ..subprocess_tools import command_exists, run_command
from .base import Scanner, ScannerOutput


class SemgrepScanner(Scanner):
    name = "semgrep"

    def scan(self, target_dir: Path) -> ScannerOutput:
        command = ["semgrep", "scan", "--config", "auto", "--json", "--quiet", "."]
        if not command_exists("semgrep", target_dir):
            return ScannerOutput(
                run=ScannerRun(
                    scanner=self.name,
                    command=command,
                    status="skipped",
                    summary="Semgrep is not installed.",
                    elapsed_seconds=0,
                )
            )

        result = run_command(command, cwd=str(target_dir), timeout_seconds=240)
        if result.returncode not in {0, 1}:
            return ScannerOutput(
                run=ScannerRun(
                    scanner=self.name,
                    command=command,
                    status="failed",
                    summary=result.stderr.strip()[:500] or "Semgrep failed.",
                    elapsed_seconds=result.elapsed_seconds,
                )
            )

        payload = json.loads(result.stdout or "{}")
        findings = [self._normalize(item, target_dir) for item in payload.get("results", [])]
        return ScannerOutput(
            run=ScannerRun(
                scanner=self.name,
                command=command,
                status="ok",
                summary=f"Semgrep returned {len(findings)} findings.",
                elapsed_seconds=result.elapsed_seconds,
            ),
            findings=findings,
        )

    def _normalize(self, item: dict, target_dir: Path) -> Finding:
        extra = item.get("extra", {})
        severity = str(extra.get("severity", "INFO")).lower()
        if severity not in {"info", "low", "medium", "high", "critical"}:
            severity = "info"
        path = relative_path(target_dir / item.get("path", ""), target_dir)
        return Finding(
            scanner=self.name,
            rule_id=str(item.get("check_id", "semgrep.unknown")),
            title=str(extra.get("metadata", {}).get("shortlink") or item.get("check_id", "Semgrep finding")),
            severity=severity,  # type: ignore[arg-type]
            location=CodeLocation(
                path=path,
                start_line=int(item.get("start", {}).get("line", 1)),
                end_line=int(item.get("end", {}).get("line", item.get("start", {}).get("line", 1))),
            ),
            message=str(extra.get("message", "")),
            confidence=str(extra.get("metadata", {}).get("confidence", "unknown")),
            raw=item,
        )
