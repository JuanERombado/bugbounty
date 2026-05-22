"""CLI entry point for the Hotspot Hub backend."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .engine import HotspotEngine
from .prompt_builder import build_hotspot_prompt
from .target_initializer import initialize_target
from .tool_status import collect_tool_status


def scan_command(args: argparse.Namespace) -> int:
    report = HotspotEngine().scan(args.target)
    payload = report.to_dict()
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"Wrote {args.out} with {len(report.hotspots)} hotspots")
    else:
        print(json.dumps(payload, indent=2))
    return 0


def prompt_command(args: argparse.Namespace) -> int:
    payload = json.loads(args.report.read_text(encoding="utf-8"))
    hotspot = next((item for item in payload["hotspots"] if item["path"] == args.path), None)
    if not hotspot:
        raise SystemExit(f"Hotspot not found in report: {args.path}")

    from .models import CodeLocation, Finding, Hotspot, MetricSignal

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
        for item in hotspot.get("findings", [])
    ]
    metrics = [MetricSignal(**item) for item in hotspot.get("metrics", [])]
    model = Hotspot(
        path=hotspot["path"],
        score=hotspot["score"],
        reasons=hotspot.get("reasons", []),
        metrics=metrics,
        findings=findings,
        symbols=hotspot.get("symbols", []),
        tags=hotspot.get("tags", []),
    )
    prompt = build_hotspot_prompt(Path(payload["target"]["root"]), model)
    print(json.dumps(prompt, indent=2))
    return 0


def tools_status_command(args: argparse.Namespace) -> int:
    payload = collect_tool_status(args.cwd)
    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        print(text)
    return 0


def target_init_command(args: argparse.Namespace) -> int:
    payload = initialize_target(args.program_url, Path.cwd(), args.name)
    print(json.dumps(payload, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local Hotspot Hub backend")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan = subparsers.add_parser("scan", help="Scan a target directory and emit normalized JSON")
    scan.add_argument("target", type=Path)
    scan.add_argument("--out", type=Path)
    scan.set_defaults(func=scan_command)

    prompt = subparsers.add_parser("prompt", help="Build a focused LLM prompt for one hotspot")
    prompt.add_argument("report", type=Path)
    prompt.add_argument("path", help="Hotspot path from the report JSON")
    prompt.set_defaults(func=prompt_command)

    tools = subparsers.add_parser("tools", help="Inspect local scanner/tool readiness")
    tools_subparsers = tools.add_subparsers(dest="tools_command", required=True)

    status = tools_subparsers.add_parser("status", help="Emit installed/missing tools and disk usage as JSON")
    status.add_argument("--cwd", type=Path, default=Path.cwd(), help="Workspace root used for local .tools discovery")
    status.add_argument("--out", type=Path, help="Optional JSON output path")
    status.set_defaults(func=tools_status_command)

    target = subparsers.add_parser("target", help="Create or update local target foundations")
    target_subparsers = target.add_subparsers(dest="target_command", required=True)

    init = target_subparsers.add_parser("init", help="Initialize a target from an Immunefi program URL")
    init.add_argument("program_url", help="Immunefi program URL")
    init.add_argument("--name", help="Optional display name for the target")
    init.set_defaults(func=target_init_command)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
