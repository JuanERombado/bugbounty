"""Generate hypotheses from hotspot reports via optional model providers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

from .model_providers.canned import CannedProvider
from .model_providers.ollama import OllamaProvider
from .model_providers.openai_compatible import OpenAICompatibleProvider


ProviderName = Literal["canned", "ollama", "openai"]


def generate_hypotheses(provider_name: ProviderName, hotspot_report: Path, out_path: Path, max_items: int = 5) -> dict:
    report = json.loads(hotspot_report.read_text(encoding="utf-8"))
    provider = _provider(provider_name)
    items = provider.generate(report, max_items)
    payload = {
        "provider": provider.name,
        "source_report": str(hotspot_report),
        "hypotheses": items,
        "report_ready": False,
        "safety_note": "Hypotheses are untrusted until local PoC or invariant evidence proves them.",
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def _provider(provider_name: ProviderName):
    if provider_name == "canned":
        return CannedProvider()
    if provider_name == "ollama":
        return OllamaProvider()
    if provider_name == "openai":
        return OpenAICompatibleProvider()
    raise ValueError(f"Unsupported provider: {provider_name}")
