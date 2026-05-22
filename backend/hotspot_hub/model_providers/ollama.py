"""Ollama hypothesis provider."""

from __future__ import annotations

import json
import os
import urllib.request


class OllamaProvider:
    name = "ollama"

    def __init__(self, base_url: str | None = None, model: str | None = None) -> None:
        self.base_url = base_url or os.environ.get("OLLAMA_BASE_URL")
        self.model = model or os.environ.get("OLLAMA_MODEL", "qwen3.5:9b")
        if not self.base_url:
            raise RuntimeError("OLLAMA_BASE_URL is not set")

    def generate(self, hotspot_report: dict, max_items: int = 5) -> list[dict]:
        prompt = _prompt(hotspot_report, max_items)
        body = {"model": self.model, "prompt": prompt, "stream": False, "format": "json"}
        req = urllib.request.Request(
            f"{self.base_url.rstrip('/')}/api/generate",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=180) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return _parse_items(payload.get("response", "[]"), self.name)


def _prompt(hotspot_report: dict, max_items: int) -> str:
    hotspots = [
        {"path": item.get("path"), "score": item.get("score"), "tags": item.get("tags", []), "reasons": item.get("reasons", [])}
        for item in hotspot_report.get("hotspots", [])[:max_items]
    ]
    return (
        "Generate local-only smart-contract bug hypotheses as JSON array. "
        "Each item needs id,title,hotspot_path,hypothesis,local_test_idea,rejection_rule. "
        "No live testing. Hotspots:\n"
        + json.dumps(hotspots, indent=2)
    )


def _parse_items(raw: str, source: str) -> list[dict]:
    items = json.loads(raw)
    for index, item in enumerate(items, start=1):
        item.setdefault("id", f"OLLAMA-{index:03d}")
        item["source"] = source
        item["report_ready"] = False
    return items
