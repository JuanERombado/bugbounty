# Hotspot Hub Backend

Reusable local backend for mapping bug bounty target repositories before spending LLM tokens.

## Design

1. `engine.py` orchestrates scans for a target directory.
2. `scanners/` contains local scanner adapters.
3. `models.py` defines normalized UI/API-ready data structures.
4. `prompt_builder.py` builds a targeted LLM payload from one selected hotspot.
5. `cli.py` gives the future desktop UI a simple subprocess-friendly entry point.
6. `server.py` serves the dashboard and exposes the project initialization API.

## First Run

```powershell
python -m backend.hotspot_hub.cli scan "external/thegraph-contracts" --out "targets/thegraph/code-map/hotspot-report.json"
```

This uses the built-in complexity scanner and runs Semgrep/Slither only if those tools are installed.

Optional scanner installs:

```powershell
pip install semgrep slither-analyzer
```

## Output

The report is JSON and contains:

- `target`: scanned path and timing metadata.
- `hotspots`: ranked files/functions with risk score and local evidence.
- `findings`: normalized static-analysis alerts.
- `scanner_runs`: raw scanner status summaries.

## Tool Status

```powershell
python -m backend.hotspot_hub.cli tools status
```

The status command returns JSON with installed/missing tools, resolved binary paths, versions, and local `.tools` disk usage.

## Next Integration Point

The dashboard can call `python -m backend.hotspot_hub.cli scan <repo> --out <json>` and render the resulting `hotspots` array.

## Dashboard Server

```powershell
python -m backend.hotspot_hub.server --host 127.0.0.1 --port 4173
```

The first API endpoint is `POST /api/projects/initialize`, which accepts an Immunefi URL and creates the local target foundation.
