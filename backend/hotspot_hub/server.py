"""Tiny local dashboard server for the Bug Bounty Workbench."""

from __future__ import annotations

import argparse
import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote

from .target_initializer import initialize_target


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
APP_ROOT = WORKSPACE_ROOT / "app"


class WorkbenchHandler(BaseHTTPRequestHandler):
    server_version = "BugBountyWorkbench/0.1"

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        if path.startswith("/api/"):
            self.write_json({"ok": False, "error": "Unknown API route"}, HTTPStatus.NOT_FOUND)
            return
        self.serve_static(path)

    def do_POST(self) -> None:
        if self.path == "/api/projects/initialize":
            self.initialize_project()
            return
        self.write_json({"ok": False, "error": "Unknown API route"}, HTTPStatus.NOT_FOUND)

    def initialize_project(self) -> None:
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8") or "{}")
            program_url = payload.get("programUrl", "")
            target_name = payload.get("targetName") or None
            result = initialize_target(program_url, WORKSPACE_ROOT, target_name)
            self.write_json(result)
        except ValueError as exc:
            self.write_json({"ok": False, "error": str(exc)}, HTTPStatus.BAD_REQUEST)
        except json.JSONDecodeError:
            self.write_json({"ok": False, "error": "Request body must be valid JSON."}, HTTPStatus.BAD_REQUEST)
        except Exception as exc:  # pragma: no cover - defensive UI boundary.
            self.write_json({"ok": False, "error": f"Initialization failed: {exc}"}, HTTPStatus.INTERNAL_SERVER_ERROR)

    def serve_static(self, raw_path: str) -> None:
        relative = "index.html" if raw_path in {"", "/"} else unquote(raw_path.lstrip("/"))
        candidate = (APP_ROOT / relative).resolve()
        if not str(candidate).startswith(str(APP_ROOT.resolve())) or not candidate.is_file():
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return

        content_type = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
        data = candidate.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def write_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        data = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.address_string()} - {format % args}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the local Bug Bounty Workbench dashboard")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=4173, type=int)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    server = ThreadingHTTPServer((args.host, args.port), WorkbenchHandler)
    print(f"Bug Bounty Workbench running at http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping dashboard server.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
