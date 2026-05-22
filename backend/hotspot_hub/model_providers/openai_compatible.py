"""OpenAI-compatible hypothesis provider."""

from __future__ import annotations

import json
import os
import urllib.request


class OpenAICompatibleProvider:
    name = "openai"

    def __init__(self, base_url: str | None = None, model: str | None = None, api_key: str | None = None) -> None:
        self.base_url = base_url or os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
        self.model = model or os.environ.get("OPENAI_MODEL", "gpt-5.4-mini")
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")

    def generate(self, hotspot_report: dict, max_items: int = 5) -> list[dict]:
        hotspots = [
            {"path": item.get("path"), "score": item.get("score"), "tags": item.get("tags", []), "reasons": item.get("reasons", [])}
            for item in hotspot_report.get("hotspots", [])[:max_items]
        ]
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "Return only valid JSON. Do not suggest live testing."},
                {
                    "role": "user",
                    "content": (
                        "Generate local-only smart-contract bug hypotheses as JSON array. "
                        "Each item needs id,title,hotspot_path,hypothesis,local_test_idea,rejection_rule.\n"
                        + json.dumps(hotspots, indent=2)
                    ),
                },
            ],
            "temperature": 0.2,
        }
        req = urllib.request.Request(
            f"{self.base_url.rstrip('/')}/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=180) as response:
            payload = json.loads(response.read().decode("utf-8"))
        raw = payload["choices"][0]["message"]["content"]
        items = json.loads(raw)
        for index, item in enumerate(items, start=1):
            item.setdefault("id", f"OPENAI-{index:03d}")
            item["source"] = self.name
            item["report_ready"] = False
        return items
