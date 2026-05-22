"""Initialize a local target workspace from a public Immunefi program URL."""

from __future__ import annotations

import html
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


DIRECTORIES = [
    "scope",
    "assets",
    "audits",
    "code-map",
    "hypotheses",
    "pocs",
    "reports",
    "known-bugs",
]


@dataclass(frozen=True)
class ProgramPage:
    url: str
    title: str
    description: str
    text: str
    links: list[str]
    warnings: list[str]


class ProgramHTMLParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.links: list[str] = []
        self.description = ""
        self._skip_depth = 0
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key.lower(): value or "" for key, value in attrs}
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True
        if tag == "a" and attrs_dict.get("href"):
            self.links.append(urllib.parse.urljoin(self.base_url, attrs_dict["href"]))
        if tag == "meta":
            name = attrs_dict.get("name", "").lower()
            prop = attrs_dict.get("property", "").lower()
            if name == "description" or prop == "og:description":
                self.description = attrs_dict.get("content", "").strip()

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if not value:
            return
        if self._in_title:
            self.title_parts.append(value)
        elif not self._skip_depth:
            self.text_parts.append(value)

    def page(self, url: str, warnings: list[str]) -> ProgramPage:
        title = html.unescape(" ".join(self.title_parts)).strip()
        text = html.unescape(" ".join(self.text_parts)).strip()
        description = html.unescape(self.description).strip()
        unique_links = sorted(set(self.links))
        return ProgramPage(
            url=url,
            title=title or "Untitled Immunefi program",
            description=description,
            text=text,
            links=unique_links,
            warnings=warnings,
        )


def initialize_target(program_url: str, workspace: Path, target_name: str | None = None) -> dict[str, Any]:
    """Create a local target foundation and return UI-ready status JSON."""

    normalized_url = validate_immunefi_url(program_url)
    slug = make_slug(target_name) if target_name else slug_from_url(normalized_url)
    page = fetch_program_page(normalized_url)
    if not target_name and page.title:
        slug = slug_from_url(normalized_url) or make_slug(page.title)

    target_dir = workspace / "targets" / slug
    created_dirs = ensure_target_dirs(target_dir)
    generated = build_scope_payload(slug, target_name, normalized_url, page)

    scope_path = target_dir / "scope" / f"{slug}.scope.json"
    init_path = target_dir / "scope" / f"{slug}.initializer.latest.json"
    readme_path = target_dir / "README.md"

    warnings = list(page.warnings)
    written_files: list[str] = []
    skipped_files: list[str] = []

    if scope_path.exists():
        skipped_files.append(str(scope_path))
        warnings.append("Existing scope JSON was not overwritten.")
    else:
        write_json(scope_path, generated)
        written_files.append(str(scope_path))

    write_json(init_path, generated)
    written_files.append(str(init_path))

    if not readme_path.exists():
        readme_path.write_text(build_target_readme(slug, generated), encoding="utf-8")
        written_files.append(str(readme_path))
    else:
        skipped_files.append(str(readme_path))

    return {
        "ok": True,
        "slug": slug,
        "target_name": generated["target_name"],
        "target_dir": str(target_dir),
        "created_directories": [str(item) for item in created_dirs],
        "written_files": written_files,
        "skipped_files": skipped_files,
        "warnings": warnings,
        "preview": {
            "title": generated["program_title"],
            "summary": generated["program_summary"],
            "resource_count": len(generated["resources"]),
            "status": generated["status"],
        },
        "next_steps": [
            "Review the generated scope JSON and replace placeholders with exact in-scope assets and accepted impacts.",
            "Add repository URLs from the Immunefi resources page.",
            "Run the asset ranking script once scope is structured.",
        ],
    }


def validate_immunefi_url(value: str) -> str:
    parsed = urllib.parse.urlparse(value.strip())
    if parsed.scheme != "https":
        raise ValueError("Use an https Immunefi program URL.")
    if parsed.netloc.lower() not in {"immunefi.com", "www.immunefi.com"}:
        raise ValueError("Only Immunefi program URLs are supported in this initializer.")
    if not parsed.path.startswith("/bug-bounty/"):
        raise ValueError("URL must look like https://immunefi.com/bug-bounty/<program>/...")
    return urllib.parse.urlunparse(parsed._replace(netloc="immunefi.com"))


def slug_from_url(program_url: str) -> str:
    parts = [part for part in urllib.parse.urlparse(program_url).path.split("/") if part]
    if "bug-bounty" in parts:
        index = parts.index("bug-bounty")
        if len(parts) > index + 1:
            return make_slug(parts[index + 1])
    return "new-target"


def make_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "new-target"


def fetch_program_page(program_url: str) -> ProgramPage:
    warnings: list[str] = []
    request = urllib.request.Request(
        program_url,
        headers={
            "User-Agent": "bug-bounty-workbench/0.1 local-scope-initializer",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            content = response.read(2_000_000).decode(charset, errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        warnings.append(f"Could not fetch page automatically: {exc}")
        content = ""

    parser = ProgramHTMLParser(program_url)
    if content:
        parser.feed(content)
    return parser.page(program_url, warnings)


def ensure_target_dirs(target_dir: Path) -> list[Path]:
    created: list[Path] = []
    for name in DIRECTORIES:
        path = target_dir / name
        if not path.exists():
            created.append(path)
        path.mkdir(parents=True, exist_ok=True)
    return created


def build_scope_payload(slug: str, target_name: str | None, program_url: str, page: ProgramPage) -> dict[str, Any]:
    title = clean_title(page.title)
    inferred_name = target_name or infer_target_name(title, slug)
    resources = collect_resource_links(program_url, page.links)
    raw_excerpt = page.text[:2500]
    summary = page.description or first_sentence(page.text) or "Manual review needed after initialization."

    return {
        "schema_version": "0.2",
        "target_name": inferred_name,
        "target_slug": slug,
        "program_url": program_url,
        "initialized_at": datetime.now(timezone.utc).isoformat(),
        "source": "immunefi_public_program_page",
        "program_title": title,
        "program_summary": summary,
        "status": "needs_manual_scope_review",
        "assets_in_scope": [],
        "out_of_scope": [],
        "accepted_impacts": [],
        "known_issue_sources": [],
        "resources": resources,
        "initial_questions": [
            "Which assets are explicitly in scope?",
            "Which paid impacts are accepted for this program?",
            "Which repositories and audits should be reviewed before hypothesis work?",
            "Which testing activities are prohibited by the program rules?",
        ],
        "raw_excerpt": raw_excerpt,
    }


def clean_title(value: str) -> str:
    title = re.sub(r"\s+", " ", value).strip()
    return title.replace(" | Immunefi", "").replace(" - Immunefi", "") or "Untitled Immunefi program"


def infer_target_name(title: str, slug: str) -> str:
    if title and title != "Untitled Immunefi program":
        return re.sub(r"\s+Bug Bounty.*$", "", title, flags=re.IGNORECASE).strip()
    return slug.replace("-", " ").title()


def first_sentence(value: str) -> str:
    match = re.search(r"(.{40,280}?[.!?])\s", value)
    return match.group(1).strip() if match else ""


def collect_resource_links(program_url: str, links: list[str]) -> list[dict[str, str]]:
    parsed = urllib.parse.urlparse(program_url)
    base = urllib.parse.urlunparse(parsed._replace(fragment=""))
    program_slug = slug_from_url(program_url)
    candidates = {program_url, base}
    for suffix in ("information", "resources", "scope"):
        candidates.add(f"https://immunefi.com/bug-bounty/{program_slug}/{suffix}/#top")

    for link in links:
        lower = link.lower()
        if any(term in lower for term in ("github", "docs", "audit", "scope", "resource", program_slug)):
            candidates.add(link)

    resources = []
    for link in sorted(candidates):
        resources.append({"url": link, "type": classify_link(link), "status": "needs_review"})
    return resources


def classify_link(link: str) -> str:
    lower = link.lower()
    if "github.com" in lower:
        return "repository"
    if "audit" in lower:
        return "audit"
    if "docs" in lower or "documentation" in lower:
        return "docs"
    if "scope" in lower:
        return "scope"
    if "resources" in lower:
        return "resources"
    return "program"


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def build_target_readme(slug: str, payload: dict[str, Any]) -> str:
    return f"""# {payload["target_name"]}

Initialized from: {payload["program_url"]}

## Status

Manual scope review is required before ranking assets or writing hypotheses.

## Next Steps

1. Fill `scope/{slug}.scope.json` with exact in-scope assets.
2. Add accepted paid impacts and out-of-scope rules.
3. Add repository and audit links under `resources`.
4. Run the local ranking and code mapping scripts.
5. Create hypotheses only after scope, impact, and duplicate-risk gates pass.
"""
