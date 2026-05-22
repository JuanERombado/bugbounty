"""Slither scanner adapter for Solidity targets."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

from ..models import CodeLocation, Finding, ScannerRun, Severity, relative_path
from ..subprocess_tools import command_exists, run_command
from .base import Scanner, ScannerOutput


IMPACT_TO_SEVERITY: dict[str, Severity] = {
    "optimization": "info",
    "informational": "info",
    "low": "low",
    "medium": "medium",
    "high": "high",
}


class SlitherScanner(Scanner):
    name = "slither"

    def scan(self, target_dir: Path) -> ScannerOutput:
        command_preview = ["slither", ".", "--json", "<tempfile>", "--disable-color"]
        if not command_exists("slither", target_dir):
            return ScannerOutput(
                run=ScannerRun(
                    scanner=self.name,
                    command=command_preview,
                    status="skipped",
                    summary="Slither is not installed.",
                    elapsed_seconds=0,
                )
            )

        with tempfile.TemporaryDirectory(prefix="hotspot-hub-slither-") as temp_dir:
            output_path = Path(temp_dir) / "slither.json"
            command = ["slither", ".", "--json", str(output_path), "--disable-color"]
            result = run_command(command, cwd=str(target_dir), timeout_seconds=300)
            if result.returncode != 0 and not output_path.exists():
                return ScannerOutput(
                    run=ScannerRun(
                        scanner=self.name,
                        command=command,
                        status="failed",
                        summary=(result.stderr or result.stdout).strip()[:500] or "Slither failed.",
                        elapsed_seconds=result.elapsed_seconds,
                    )
                )

            try:
                payload = json.loads(output_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                return ScannerOutput(
                    run=ScannerRun(
                        scanner=self.name,
                        command=command,
                        status="failed",
                        summary=f"Could not parse Slither JSON: {exc}",
                        elapsed_seconds=result.elapsed_seconds,
                    )
                )

        detectors = payload.get("results", {}).get("detectors", [])
        findings = [
            finding
            for detector in detectors
            if (finding := self._normalize(detector, target_dir)) is not None
        ]
        return ScannerOutput(
            run=ScannerRun(
                scanner=self.name,
                command=command_preview,
                status="ok",
                summary=f"Slither returned {len(findings)} detector finding(s).",
                elapsed_seconds=result.elapsed_seconds,
            ),
            findings=findings,
        )

    def _normalize(self, detector: dict[str, Any], target_dir: Path) -> Finding | None:
        location = self._primary_location(detector, target_dir)
        if self._is_dependency_location(location.path):
            return None
        impact = str(detector.get("impact", "informational")).lower()
        severity = IMPACT_TO_SEVERITY.get(impact, "info")
        if severity == "info":
            return None
        check = str(detector.get("check", "slither.unknown"))
        return Finding(
            scanner=self.name,
            rule_id=f"slither.{check}",
            title=check.replace("-", " ").title(),
            severity=severity,
            location=location,
            message=str(detector.get("description", "")).strip(),
            confidence=str(detector.get("confidence", "unknown")).lower(),
            raw={
                "impact": detector.get("impact"),
                "confidence": detector.get("confidence"),
                "check": detector.get("check"),
                "markdown": detector.get("markdown"),
            },
        )

    def _primary_location(self, detector: dict[str, Any], target_dir: Path) -> CodeLocation:
        element = self._first_element_with_mapping(detector.get("elements", []))
        mapping = element.get("source_mapping", {}) if element else {}
        filename = (
            mapping.get("filename_relative")
            or mapping.get("filename_short")
            or mapping.get("filename_absolute")
            or detector.get("first_markdown_element")
            or "unknown"
        )
        lines = mapping.get("lines") or [1]
        start_line = int(lines[0]) if lines else 1
        end_line = int(lines[-1]) if len(lines) > 1 else start_line
        path = relative_path(target_dir / str(filename), target_dir)
        return CodeLocation(
            path=path,
            start_line=start_line,
            end_line=end_line,
            symbol=str(element.get("name")) if element and element.get("name") else None,
        )

    def _first_element_with_mapping(self, elements: list[dict[str, Any]]) -> dict[str, Any] | None:
        for element in elements:
            if element.get("source_mapping"):
                return element
        return elements[0] if elements else None

    def _is_dependency_location(self, path: str) -> bool:
        normalized = path.replace("\\", "/")
        return normalized.startswith("../") or "/node_modules/" in normalized or normalized.startswith("node_modules/")
