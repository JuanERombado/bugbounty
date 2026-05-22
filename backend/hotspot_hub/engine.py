"""Hotspot Hub scan orchestrator."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from .models import Finding, Hotspot, HotspotReport, TargetInfo, utc_now_iso
from .scanners.base import Scanner
from .scanners.complexity import IGNORED_DIRS, SUPPORTED_SUFFIXES, ComplexityScanner
from .scanners.semgrep import SemgrepScanner
from .scanners.slither import SlitherScanner


SEVERITY_WEIGHT = {
    "info": 1,
    "low": 3,
    "medium": 8,
    "high": 16,
    "critical": 30,
}


class HotspotEngine:
    def __init__(self, scanners: list[Scanner] | None = None) -> None:
        self.scanners = scanners or [ComplexityScanner(), SemgrepScanner(), SlitherScanner()]

    def scan(self, target_dir: Path) -> HotspotReport:
        target_dir = target_dir.resolve()
        if not target_dir.exists() or not target_dir.is_dir():
            raise ValueError(f"Target directory does not exist: {target_dir}")

        scanner_runs = []
        all_findings: list[Finding] = []
        hotspot_by_path: dict[str, Hotspot] = {}

        for scanner in self.scanners:
            output = scanner.scan(target_dir)
            scanner_runs.append(output.run)
            all_findings.extend(output.findings)
            for hotspot in output.hotspots:
                hotspot_by_path[hotspot.path] = hotspot

        merged_hotspots = self._merge_findings_into_hotspots(hotspot_by_path, all_findings)
        file_count = self._count_supported_files(target_dir)
        return HotspotReport(
            target=TargetInfo(root=str(target_dir), generated_at=utc_now_iso(), file_count=file_count),
            hotspots=merged_hotspots,
            findings=all_findings,
            scanner_runs=scanner_runs,
        )

    def _merge_findings_into_hotspots(
        self,
        hotspot_by_path: dict[str, Hotspot],
        findings: list[Finding],
    ) -> list[Hotspot]:
        findings_by_path: dict[str, list[Finding]] = defaultdict(list)
        for finding in findings:
            findings_by_path[finding.location.path].append(finding)

        all_paths = set(hotspot_by_path) | set(findings_by_path)
        merged: list[Hotspot] = []
        for path in all_paths:
            base = hotspot_by_path.get(path)
            path_findings = findings_by_path.get(path, [])
            finding_score = sum(SEVERITY_WEIGHT[finding.severity] for finding in path_findings)
            score = round((base.score if base else 0) + finding_score, 2)
            reasons = list(base.reasons if base else [])
            if path_findings:
                reasons.append(f"{len(path_findings)} static-analysis finding(s)")
            merged.append(
                Hotspot(
                    path=path,
                    score=score,
                    reasons=reasons[:6],
                    metrics=list(base.metrics if base else []),
                    findings=path_findings,
                    symbols=list(base.symbols if base else []),
                    tags=list(base.tags if base else []),
                )
            )

        return sorted(merged, key=lambda item: item.score, reverse=True)

    def _count_supported_files(self, target_dir: Path) -> int:
        count = 0
        for path in target_dir.rglob("*"):
            if path.is_file() and path.suffix in SUPPORTED_SUFFIXES and not any(part in IGNORED_DIRS for part in path.parts):
                count += 1
        return count
