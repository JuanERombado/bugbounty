"""OpenAI-compatible local LLM adapter for LM Studio."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from .models import CodeLocation, Finding, Hotspot, MetricSignal
from .prompt_builder import build_hotspot_prompt


DEFAULT_BASE_URL = "http://127.0.0.1:1234/v1"
DEFAULT_MODEL = "qwen/qwen3.5-9b"
DEFAULT_TEMPERATURE = 0.2
DEFAULT_MAX_TOKENS = 1400
DEFAULT_PING_MAX_TOKENS = 256


def chat_completion(
    messages: list[dict[str, str]],
    base_url: str = DEFAULT_BASE_URL,
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    timeout_seconds: int = 300,
) -> dict[str, Any]:
    """Send a chat completion request to an OpenAI-compatible local server."""
    body = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Local LLM request failed: HTTP {exc.code} {exc.reason}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Local LLM request failed: {exc}") from exc
    return json.loads(raw)


def list_local_models(
    base_url: str = DEFAULT_BASE_URL,
    timeout_seconds: int = 30,
) -> list[str]:
    """Return model ids exposed by the local OpenAI-compatible server."""
    request = urllib.request.Request(f"{base_url.rstrip('/')}/models", method="GET")
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Local model list failed: HTTP {exc.code} {exc.reason}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Local model list failed: {exc}") from exc

    payload = json.loads(raw)
    return [item["id"] for item in payload.get("data", []) if "id" in item]


def ping_local_llm(
    base_url: str = DEFAULT_BASE_URL,
    model: str = DEFAULT_MODEL,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    """Run a small connectivity and response-shape check."""
    available_models = list_local_models(base_url, timeout_seconds)
    selected_model = model
    if selected_model not in available_models and available_models:
        selected_model = available_models[0]

    response = chat_completion(
        [
            {"role": "system", "content": "You are a concise local model health check."},
            {"role": "user", "content": "Reply with exactly: local model online"},
        ],
        base_url=base_url,
        model=selected_model,
        temperature=0.0,
        max_tokens=DEFAULT_PING_MAX_TOKENS,
        timeout_seconds=timeout_seconds,
    )
    normalized = normalize_response(response)
    normalized["available_models"] = available_models
    normalized["requested_model"] = model
    normalized["selected_model"] = selected_model
    normalized["server_reachable"] = True
    normalized["health_status"] = "online" if normalized["has_output"] else "reachable_no_output"
    normalized["ping_note"] = (
        "Some reasoning models return health-check text in reasoning_content before final content. "
        "For this workbench, server reachability plus any model output is enough for ping."
    )
    return normalized


def analyze_prompt_file(
    prompt_path: Path,
    out_path: Path | None = None,
    base_url: str = DEFAULT_BASE_URL,
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    timeout_seconds: int = 300,
) -> dict[str, Any]:
    """Analyze a JSON prompt file with `system` and `user` fields."""
    prompt = json.loads(prompt_path.read_text(encoding="utf-8"))
    result = analyze_prompt_payload(prompt, base_url, model, temperature, max_tokens, timeout_seconds)
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def analyze_hotspot(
    report_path: Path,
    hotspot_path: str,
    out_path: Path | None = None,
    base_url: str = DEFAULT_BASE_URL,
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    timeout_seconds: int = 300,
) -> dict[str, Any]:
    """Build a hotspot prompt and send it to the local LLM."""
    report = json.loads(report_path.read_text(encoding="utf-8"))
    hotspot = next((item for item in report["hotspots"] if item["path"] == hotspot_path), None)
    if hotspot is None:
        raise ValueError(f"Hotspot not found in report: {hotspot_path}")

    model_hotspot = _hotspot_from_payload(hotspot)
    prompt = build_hotspot_prompt(Path(report["target"]["root"]), model_hotspot)
    result = analyze_prompt_payload(prompt, base_url, model, temperature, max_tokens, timeout_seconds)
    result["hotspot"] = {
        "path": hotspot_path,
        "score": hotspot.get("score"),
        "reasons": hotspot.get("reasons", []),
        "tags": hotspot.get("tags", []),
    }
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def analyze_prompt_payload(
    prompt: dict[str, str],
    base_url: str,
    model: str,
    temperature: float,
    max_tokens: int,
    timeout_seconds: int,
) -> dict[str, Any]:
    response = chat_completion(
        [
            {"role": "system", "content": prompt["system"]},
            {"role": "user", "content": prompt["user"]},
        ],
        base_url=base_url,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout_seconds=timeout_seconds,
    )
    normalized = normalize_response(response)
    normalized["prompt_chars"] = len(prompt["system"]) + len(prompt["user"])
    return normalized


def normalize_response(response: dict[str, Any]) -> dict[str, Any]:
    choice = response.get("choices", [{}])[0]
    message = choice.get("message", {})
    content = message.get("content") or ""
    reasoning = message.get("reasoning_content") or ""
    has_content = bool(content.strip())
    has_reasoning = bool(reasoning.strip())
    return {
        "model": response.get("model"),
        "content": content,
        "reasoning_content": reasoning,
        "finish_reason": choice.get("finish_reason"),
        "usage": response.get("usage", {}),
        "raw_id": response.get("id"),
        "has_content": has_content,
        "has_reasoning_content": has_reasoning,
        "has_output": has_content or has_reasoning,
    }


def _hotspot_from_payload(payload: dict[str, Any]) -> Hotspot:
    findings = [
        Finding(
            scanner=item["scanner"],
            rule_id=item["rule_id"],
            title=item["title"],
            severity=item["severity"],
            location=CodeLocation(**item["location"]),
            message=item["message"],
            confidence=item.get("confidence", "unknown"),
            raw=item.get("raw", {}),
        )
        for item in payload.get("findings", [])
    ]
    metrics = [MetricSignal(**item) for item in payload.get("metrics", [])]
    return Hotspot(
        path=payload["path"],
        score=payload["score"],
        reasons=payload.get("reasons", []),
        metrics=metrics,
        findings=findings,
        symbols=payload.get("symbols", []),
        tags=payload.get("tags", []),
    )
