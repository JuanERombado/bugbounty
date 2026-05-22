"""CLI entry point for the Hotspot Hub backend."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .engine import HotspotEngine
from .foundry_harness_generator import generate_foundry_scaffold
from .hypothesis_queue import default_invariant_candidates, make_run_id, write_queue
from .local_llm import analyze_hotspot, analyze_prompt_file, ping_local_llm
from .prompt_builder import build_hotspot_prompt
from .queue_generator import generate_hotspot_worker_queue
from .result_judge import judge_foundry_result
from .target_initializer import initialize_target
from .test_runner import run_foundry_tests
from .tool_status import collect_tool_status
from .worker import run_worker_queue


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


def foundry_slice_command(args: argparse.Namespace) -> int:
    workspace = Path.cwd()
    run_id = args.run_id or make_run_id(args.contract_name)
    run_dir = workspace / "targets" / args.target / "runs" / run_id
    generated_dir = workspace / "targets" / args.target / "pocs" / "generated" / run_id
    candidates = default_invariant_candidates(args.contract_name, args.contract_path)

    queue_payload = write_queue(
        run_dir / "hypothesis-queue.json",
        run_id=run_id,
        target=args.target,
        contract_name=args.contract_name,
        contract_path=args.contract_path,
        candidates=candidates,
    )
    generated_files = generate_foundry_scaffold(generated_dir, queue_payload)
    run_payload = run_foundry_tests(generated_dir, run_dir / "foundry-result.json", args.timeout)
    judgment = judge_foundry_result(queue_payload, run_payload, run_dir / "judgment.json")

    summary = {
        "run_id": run_id,
        "status": judgment["status"],
        "generated_dir": str(generated_dir),
        "run_dir": str(run_dir),
        "generated_files": [str(path) for path in generated_files],
        "result_file": str(run_dir / "foundry-result.json"),
        "judgment_file": str(run_dir / "judgment.json"),
        "next_action": judgment["next_action"],
    }
    print(json.dumps(summary, indent=2))
    return 0


def worker_run_command(args: argparse.Namespace) -> int:
    summary = run_worker_queue(args.queue, Path.cwd(), args.out_dir, args.max_jobs)
    print(json.dumps(summary, indent=2))
    return 0


def worker_generate_command(args: argparse.Namespace) -> int:
    queue = generate_hotspot_worker_queue(
        args.report,
        args.out,
        args.target,
        args.max_hotspots,
        args.mode,
        args.timeout,
    )
    print(json.dumps({"out": str(args.out), "jobs": len(queue["jobs"]), "mode": queue["mode"]}, indent=2))
    return 0


def llm_ping_command(args: argparse.Namespace) -> int:
    result = ping_local_llm(args.base_url, args.model, args.timeout)
    print(json.dumps(result, indent=2))
    return 0


def llm_analyze_prompt_command(args: argparse.Namespace) -> int:
    result = analyze_prompt_file(
        args.prompt_json,
        args.out,
        args.base_url,
        args.model,
        args.temperature,
        args.max_tokens,
        args.timeout,
    )
    print(json.dumps(result, indent=2))
    return 0


def llm_analyze_hotspot_command(args: argparse.Namespace) -> int:
    result = analyze_hotspot(
        args.report,
        args.path,
        args.out,
        args.base_url,
        args.model,
        args.temperature,
        args.max_tokens,
        args.timeout,
    )
    print(json.dumps(result, indent=2))
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

    validate = subparsers.add_parser("validate", help="Run local hypothesis validation slices")
    validate_subparsers = validate.add_subparsers(dest="validate_command", required=True)

    foundry = validate_subparsers.add_parser("foundry-slice", help="Generate and run one Foundry validation scaffold")
    foundry.add_argument("--target", default="thegraph", help="Target slug under targets/")
    foundry.add_argument("--contract-name", required=True, help="Human-readable selected contract name")
    foundry.add_argument("--contract-path", required=True, help="Local or mapped path for the selected contract")
    foundry.add_argument("--run-id", help="Optional stable run id")
    foundry.add_argument("--timeout", type=int, default=180, help="Forge test timeout in seconds")
    foundry.set_defaults(func=foundry_slice_command)

    worker = subparsers.add_parser("worker", help="Run bounded local research jobs from a queue")
    worker_subparsers = worker.add_subparsers(dest="worker_command", required=True)

    worker_run = worker_subparsers.add_parser("run", help="Run a JSON worker queue")
    worker_run.add_argument("queue", type=Path, help="Path to worker queue JSON")
    worker_run.add_argument("--out-dir", type=Path, help="Optional output directory for run artifacts")
    worker_run.add_argument("--max-jobs", type=int, help="Optional maximum jobs to run from the queue")
    worker_run.set_defaults(func=worker_run_command)

    worker_generate = worker_subparsers.add_parser("generate", help="Generate a worker queue from a hotspot report")
    worker_generate.add_argument("report", type=Path, help="Hotspot report JSON")
    worker_generate.add_argument("--out", type=Path, required=True, help="Output worker queue JSON")
    worker_generate.add_argument("--target", default="thegraph", help="Target slug under targets/")
    worker_generate.add_argument("--max-hotspots", type=int, default=5, help="Maximum ranked hotspots to queue")
    worker_generate.add_argument(
        "--mode",
        choices=["prompt", "local-llm", "foundry-scaffold"],
        default="prompt",
        help="Queue prompt artifacts, local LLM analysis, or generated Foundry scaffold runs",
    )
    worker_generate.add_argument("--timeout", type=int, default=180, help="Timeout per generated job in seconds")
    worker_generate.set_defaults(func=worker_generate_command)

    llm = subparsers.add_parser("llm", help="Use a local OpenAI-compatible LLM server")
    llm_subparsers = llm.add_subparsers(dest="llm_command", required=True)

    llm_ping = llm_subparsers.add_parser("ping", help="Check local LLM connectivity")
    llm_ping.add_argument("--base-url", default="http://127.0.0.1:1234/v1")
    llm_ping.add_argument("--model", default="qwen/qwen3.5-9b")
    llm_ping.add_argument("--timeout", type=int, default=60)
    llm_ping.set_defaults(func=llm_ping_command)

    llm_prompt = llm_subparsers.add_parser("analyze-prompt", help="Send a saved prompt JSON to the local LLM")
    llm_prompt.add_argument("prompt_json", type=Path)
    llm_prompt.add_argument("--out", type=Path)
    llm_prompt.add_argument("--base-url", default="http://127.0.0.1:1234/v1")
    llm_prompt.add_argument("--model", default="qwen/qwen3.5-9b")
    llm_prompt.add_argument("--temperature", type=float, default=0.2)
    llm_prompt.add_argument("--max-tokens", type=int, default=1400)
    llm_prompt.add_argument("--timeout", type=int, default=300)
    llm_prompt.set_defaults(func=llm_analyze_prompt_command)

    llm_hotspot = llm_subparsers.add_parser("analyze-hotspot", help="Build and analyze one hotspot prompt locally")
    llm_hotspot.add_argument("report", type=Path)
    llm_hotspot.add_argument("path", help="Hotspot path from the report JSON")
    llm_hotspot.add_argument("--out", type=Path)
    llm_hotspot.add_argument("--base-url", default="http://127.0.0.1:1234/v1")
    llm_hotspot.add_argument("--model", default="qwen/qwen3.5-9b")
    llm_hotspot.add_argument("--temperature", type=float, default=0.2)
    llm_hotspot.add_argument("--max-tokens", type=int, default=1400)
    llm_hotspot.add_argument("--timeout", type=int, default=300)
    llm_hotspot.set_defaults(func=llm_analyze_hotspot_command)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
