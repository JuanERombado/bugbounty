"""Normalized data models for local hotspot analysis."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal


Severity = Literal["info", "low", "medium", "high", "critical"]


@dataclass(frozen=True)
class CodeLocation:
    path: str
    start_line: int = 1
    end_line: int | None = None
    symbol: str | None = None


@dataclass(frozen=True)
class Finding:
    scanner: str
    rule_id: str
    title: str
    severity: Severity
    location: CodeLocation
    message: str
    confidence: str = "unknown"
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class MetricSignal:
    name: str
    value: int | float
    weight: int | float
    reason: str


@dataclass(frozen=True)
class Hotspot:
    path: str
    score: float
    reasons: list[str]
    metrics: list[MetricSignal] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    symbols: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ScannerRun:
    scanner: str
    command: list[str]
    status: Literal["ok", "skipped", "failed"]
    summary: str
    elapsed_seconds: float


@dataclass(frozen=True)
class TargetInfo:
    root: str
    generated_at: str
    file_count: int


@dataclass(frozen=True)
class HotspotReport:
    target: TargetInfo
    hotspots: list[Hotspot]
    findings: list[Finding]
    scanner_runs: list[ScannerRun]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def relative_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()
