"""Scanner adapter contracts."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from ..models import Finding, Hotspot, ScannerRun


@dataclass(frozen=True)
class ScannerOutput:
    run: ScannerRun
    findings: list[Finding] = field(default_factory=list)
    hotspots: list[Hotspot] = field(default_factory=list)


class Scanner:
    name = "scanner"

    def scan(self, target_dir: Path) -> ScannerOutput:
        raise NotImplementedError
