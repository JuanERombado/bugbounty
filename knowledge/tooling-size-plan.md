# Local Security Tooling Size Plan

These are practical disk-space estimates for a Windows local bug bounty workbench. Actual size varies by version, package cache, compiler versions, target repo dependencies, and Docker images.

## Recommended Core Stack

| Tool | Purpose | Install Priority | Rough Disk Use | Status |
|---|---:|---:|---:|---|
| Python 3.12 | Backend engine, scripts, Python scanners | Required | 100-250 MB | Installed globally |
| Node.js + npm | Hardhat, TypeScript tooling, dashboard builds | Required | 100-300 MB | Installed globally |
| Git | Clone target repos and inspect history | Required | 200-400 MB | Installed globally |
| Slither / `slither-analyzer` | Solidity static analysis | Required | 90-250 MB | Installed locally: `.tools/slither` is ~90 MB |
| Foundry / `forge` | Compile and run local Solidity tests | Required | 100-300 MB | Installed locally: `.tools/foundry` is ~175 MB |
| Solidity compiler / `solc` | Compile Solidity contracts | Required | 20-80 MB per compiler version | Not installed |
| Semgrep | General static analysis rules | High | 200-700 MB | Installed locally: `.tools/semgrep` is ~341 MB |
| Hardhat project deps | Compile/test JS/TS Solidity repos | High | 500 MB-2 GB per repo | Target-dependent |
| pnpm | Smaller/faster JS dependency installs | Medium | 50-150 MB plus shared store | Not installed |

## Advanced Analysis Stack

| Tool | Purpose | Install Priority | Rough Disk Use | Notes |
|---|---:|---:|---:|---|
| Echidna | Solidity property fuzzing | High | 50-200 MB | Strong for invariant testing |
| Medusa | Fast Solidity fuzzing | High | 50-200 MB | Useful complement to Echidna |
| Halmos | Symbolic testing for Foundry projects | Medium | 150-600 MB | Often pulls solver dependencies |
| Mythril | EVM symbolic analysis | Medium | 300 MB-1 GB | Can be noisy but useful for triage |
| Manticore | Symbolic execution | Low | 500 MB-2 GB | Heavier, slower, more niche |
| Certora CLI | Formal verification workflows | Medium | 100-500 MB plus Java | Requires project-specific specs |
| Scribble | Runtime assertion instrumentation | Medium | 100-500 MB with JS deps | Useful for invariant scaffolding |
| Aderyn | Solidity static analysis/reporting | Medium | 30-150 MB | Good extra detector perspective |
| Surya | Solidity call graphs and inheritance maps | Low | 50-200 MB with JS deps | Useful for visualization |

## Supporting Utilities

| Tool | Purpose | Install Priority | Rough Disk Use | Notes |
|---|---:|---:|---:|---|
| ripgrep / `rg` | Fast local search | Required | 5-20 MB | Already available in many dev setups |
| jq | JSON inspection | Medium | 5-20 MB | Handy for scanner output |
| Graphviz | Call graph rendering | Medium | 50-200 MB | Useful with Surya/Slither outputs |
| Docker Desktop | Isolated tool runs and reproducible environments | Optional | 1-3 GB plus images | Installed globally; images can add many GB |

## Storage Budget

- Minimal useful stack: Slither + Foundry + solc + Semgrep = about 500 MB-1.5 GB.
- Practical Web3 stack: add Hardhat deps, fuzzers, Graphviz = about 3-8 GB.
- Heavy research stack: add Docker images, symbolic tools, multiple target repos = 10-30+ GB.

## Current Local Installs

- Slither: installed locally at `.tools/slither`, about 90 MB.
- Foundry: installed locally at `.tools/foundry`, about 175 MB.
- Semgrep: installed locally at `.tools/semgrep`, about 341 MB.
- Current `.tools` total: about 605 MB.
