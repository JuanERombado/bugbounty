# Tool Install Log

Last bulk install completed on 2026-05-21.

## Installed Native Or Local Tools

- Foundry `1.7.1`: `.tools/foundry`.
- Slither `0.11.5`: `.tools/slither`.
- Semgrep `1.163.0`: `.tools/semgrep`.
- solc-select `1.2.0` plus Solidity `0.8.27`, `0.8.22`, `0.7.6`, `0.7.3`: `.tools/solc-select`.
- Echidna `2.3.2`: `.tools/echidna`.
- Medusa `1.5.1`: `.tools/medusa`.
- Halmos `0.3.3`: `.tools/halmos`.
- jq `1.8.1`: winget.
- Graphviz `14.1.5`: winget.
- Scribble `0.7.10`: global npm package `eth-scribble`.
- Surya `0.4.13`: global npm package `surya`.

## Wrapper-Backed Tools

- Aderyn `0.6.8`: installed inside WSL Ubuntu and called through `.tools/aderyn/aderyn.cmd`.
- Mythril `0.24.8`: installed as Docker image `mythril/myth:latest` and called through `.tools/mythril/Scripts/myth.cmd`.

## Important Notes

- `.tools/` is intentionally ignored by Git, so binaries and wrappers are local machine state.
- Docker Desktop must be running before `myth` works.
- Restart terminals or Codex if winget-installed `jq` or `dot` are not found on PATH.
- The authoritative current status snapshot is `targets/thegraph/code-map/tool-status.sample.json`.
