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
| Solidity compiler / `solc` + `solc-select` | Compile Solidity contracts and switch exact compiler versions | Required | 20-100 MB | Installed locally; versions `0.8.27`, `0.8.22`, `0.7.6`, `0.7.3` |
| Semgrep | General static analysis rules | High | 200-700 MB | Installed locally: `.tools/semgrep` is ~341 MB |
| Hardhat project deps | Compile/test JS/TS Solidity repos | High | 500 MB-2 GB per repo | Target-dependent |
| pnpm | Smaller/faster JS dependency installs | Medium | 50-150 MB plus shared store | Installed globally |

## Advanced Analysis Stack

| Tool | Purpose | Install Priority | Rough Disk Use | Notes |
|---|---:|---:|---:|---|
| Echidna | Solidity property fuzzing | High | 50-200 MB | Installed locally: `.tools/echidna` is ~86 MB |
| Medusa | Fast Solidity fuzzing | High | 50-200 MB | Installed locally: `.tools/medusa` is ~32 MB |
| Halmos | Symbolic testing for Foundry projects | Medium | 150-600 MB | Installed locally: `.tools/halmos` is ~179 MB |
| Mythril | EVM symbolic analysis | Medium | 300 MB-1 GB | Installed via Docker image `mythril/myth:latest`, ~1.02 GB, with local wrapper |
| Manticore | Symbolic execution | Low | 500 MB-2 GB | Deferred; heavier, slower, more niche |
| Certora CLI | Formal verification workflows | Medium | 100-500 MB plus Java | Requires project-specific specs |
| Scribble | Runtime assertion instrumentation | Medium | 100-500 MB with JS deps | Installed globally via npm package `eth-scribble`, version `0.7.10` |
| Aderyn | Solidity static analysis/reporting | Medium | 30-150 MB | Installed through WSL Ubuntu wrapper, version `0.6.8` |
| Surya | Solidity call graphs and inheritance maps | Low | 50-200 MB with JS deps | Installed globally via npm, version `0.4.13` |

## Supporting Utilities

| Tool | Purpose | Install Priority | Rough Disk Use | Notes |
|---|---:|---:|---:|---|
| ripgrep / `rg` | Fast local search | Required | 5-20 MB | Already available in many dev setups |
| jq | JSON inspection | Medium | 5-20 MB | Installed via winget, version `1.8.1` |
| Graphviz | Call graph rendering | Medium | 50-200 MB | Installed via winget, version `14.1.5` |
| Docker Desktop | Isolated tool runs and reproducible environments | Optional | 1-3 GB plus images | Installed globally; images can add many GB |

## Storage Budget

- Minimal useful stack: Slither + Foundry + solc + Semgrep = about 500 MB-1.5 GB.
- Practical Web3 stack: add Hardhat deps, fuzzers, Graphviz = about 3-8 GB.
- Heavy research stack: add Docker images, symbolic tools, multiple target repos = 10-30+ GB.

## Current Local Installs

- Slither: installed locally at `.tools/slither`, about 90 MB.
- Foundry: installed locally at `.tools/foundry`, about 175 MB.
- Semgrep: installed locally at `.tools/semgrep`, about 341 MB.
- `solc-select`: installed locally at `.tools/solc-select`, about 22 MB, with compiler versions `0.8.27`, `0.8.22`, `0.7.6`, and `0.7.3`.
- Echidna: installed locally at `.tools/echidna`, about 86 MB, version `2.3.2`.
- Medusa: installed locally at `.tools/medusa`, about 32 MB, version `1.5.1`.
- Halmos: installed locally at `.tools/halmos`, about 179 MB, version `0.3.3`.
- Mythril: installed as Docker image `mythril/myth:latest`, about 1.02 GB, with `.tools/mythril/Scripts/myth.cmd` wrapper.
- Scribble: installed globally with npm package `eth-scribble`, version `0.7.10`.
- Aderyn: installed in WSL Ubuntu, version `0.6.8`, with `.tools/aderyn/aderyn.cmd` wrapper.
- Surya: installed globally with npm package `surya`, version `0.4.13`.
- jq: installed globally with winget, version `1.8.1`.
- Graphviz: installed globally with winget, version `14.1.5`.
- pnpm: installed globally, version `10.25.0`.
- Docker: installed globally.
- Cargo: installed globally.
- Current `.tools` total: about 968 MB, plus about 1.02 GB for the Mythril Docker image.

## Remaining Install Queue

All planned global workbench tools are installed or wrapper-backed.

Target-specific dependency installs, such as Hardhat package installs inside cloned repos, are not counted as global workbench tools.

## Wrapper Notes

- Aderyn's current npm/release distribution does not support Windows x64 directly, so `aderyn.cmd` calls the WSL Ubuntu install.
- Mythril failed to install natively on Windows Python 3.12 because `pyethash` could not build, so `myth.cmd` calls the official Docker image.
- Docker Desktop must be running for Mythril.
