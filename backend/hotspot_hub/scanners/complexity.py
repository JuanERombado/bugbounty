"""Dependency-free file and Solidity function complexity scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import CodeLocation, Finding, Hotspot, MetricSignal, ScannerRun, relative_path
from .base import Scanner, ScannerOutput


IGNORED_DIRS = {
    ".git",
    "node_modules",
    "artifacts",
    "cache",
    "out",
    "dist",
    "build",
    ".venv",
    "venv",
}

SUPPORTED_SUFFIXES = {".sol", ".vy", ".rs", ".go", ".js", ".jsx", ".ts", ".tsx", ".py"}

FUNCTION_RE = re.compile(r"\b(function|modifier)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")
CONTRACT_RE = re.compile(r"\b(contract|library|interface)\s+([A-Za-z_][A-Za-z0-9_]*)")
BLOCK_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
LINE_COMMENT_RE = re.compile(r"//.*")
BRANCH_RE = re.compile(r"\b(if|else if|for|while|require|assert|revert|try|catch)\b")
VALUE_FLOW_RE = re.compile(r"\b(transfer|transferFrom|send|call|delegatecall|approve|mint|burn|stake|withdraw|collect|slash)\b", re.I)
AUTH_RE = re.compile(r"\b(onlyOwner|owner|governor|admin|role|authorize|permission|operator|delegate)\b", re.I)


class ComplexityScanner(Scanner):
    name = "complexity"

    def scan(self, target_dir: Path) -> ScannerOutput:
        started = time.perf_counter()
        hotspots: list[Hotspot] = []
        findings: list[Finding] = []
        file_count = 0

        for path in self._iter_files(target_dir):
            file_count += 1
            text = path.read_text(encoding="utf-8", errors="ignore")
            hotspot = self._score_file(path, target_dir, text)
            if hotspot.score > 0:
                hotspots.append(hotspot)
            findings.extend(self._heuristic_findings(path, target_dir, text))

        elapsed = time.perf_counter() - started
        run = ScannerRun(
            scanner=self.name,
            command=["internal", "complexity"],
            status="ok",
            summary=f"Scanned {file_count} source files with dependency-free heuristics.",
            elapsed_seconds=elapsed,
        )
        return ScannerOutput(run=run, findings=findings, hotspots=hotspots)

    def _iter_files(self, target_dir: Path) -> list[Path]:
        files: list[Path] = []
        for path in target_dir.rglob("*"):
            if not path.is_file() or path.suffix not in SUPPORTED_SUFFIXES:
                continue
            if any(part in IGNORED_DIRS for part in path.parts):
                continue
            files.append(path)
        return sorted(files)

    def _score_file(self, path: Path, target_dir: Path, text: str) -> Hotspot:
        rel = relative_path(path, target_dir)
        code = self._strip_comments(text)
        line_count = text.count("\n") + 1
        branches = len(BRANCH_RE.findall(code))
        value_flows = len(VALUE_FLOW_RE.findall(code))
        auth_terms = len(AUTH_RE.findall(code))
        functions = [match.group(2) for match in FUNCTION_RE.finditer(code)]
        contracts = [match.group(2) for match in CONTRACT_RE.finditer(code)]

        metrics = [
            MetricSignal("lines", line_count, min(line_count / 120, 10), "Large files hide state interactions."),
            MetricSignal("branches", branches, branches * 1.5, "Branches increase logic paths."),
            MetricSignal("value_flows", value_flows, value_flows * 3, "Value movement is bounty-relevant."),
            MetricSignal("auth_terms", auth_terms, auth_terms * 2, "Access control deserves review."),
            MetricSignal("functions", len(functions), len(functions), "More entry points means more attack surface."),
        ]
        score = round(sum(signal.weight for signal in metrics), 2)
        reasons = [signal.reason for signal in metrics if signal.weight >= 3]
        tags = self._tags(rel, text)

        return Hotspot(
            path=rel,
            score=score,
            reasons=reasons[:5],
            metrics=metrics,
            symbols=(contracts + functions)[:30],
            tags=tags,
        )

    def _strip_comments(self, text: str) -> str:
        text = BLOCK_COMMENT_RE.sub("", text)
        return LINE_COMMENT_RE.sub("", text)

    def _heuristic_findings(self, path: Path, target_dir: Path, text: str) -> list[Finding]:
        rel = relative_path(path, target_dir)
        findings: list[Finding] = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            if ".call{" in line or ".call(" in line:
                findings.append(
                    Finding(
                        scanner=self.name,
                        rule_id="heuristic.low-level-call",
                        title="Low-level call requires manual review",
                        severity="medium",
                        location=CodeLocation(rel, line_number),
                        message="Low-level calls can bypass typed interfaces and complicate reentrancy/error handling.",
                        confidence="medium",
                        raw={"line": line.strip()},
                    )
                )
            if "tx.origin" in line:
                findings.append(
                    Finding(
                        scanner=self.name,
                        rule_id="heuristic.tx-origin",
                        title="tx.origin usage",
                        severity="high",
                        location=CodeLocation(rel, line_number),
                        message="tx.origin is usually unsafe for authorization.",
                        confidence="high",
                        raw={"line": line.strip()},
                    )
                )
        return findings

    def _tags(self, rel: str, text: str) -> list[str]:
        haystack = f"{rel} {text[:3000]}".lower()
        tags = []
        for term in ["staking", "rewards", "curation", "dispute", "bridge", "escrow", "payment", "governance"]:
            if term in haystack:
                tags.append(term)
        return tags
