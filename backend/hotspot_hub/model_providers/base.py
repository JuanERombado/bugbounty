"""Base protocol for hypothesis-generation providers."""

from __future__ import annotations

from typing import Protocol


class HypothesisProvider(Protocol):
    name: str

    def generate(self, hotspot_report: dict, max_items: int = 5) -> list[dict]:
        """Return deterministic, JSON-serializable hypothesis candidates."""
