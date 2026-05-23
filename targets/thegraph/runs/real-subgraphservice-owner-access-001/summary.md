# SubgraphService OWNER-ACCESS-001

Command:

```powershell
python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id OWNER-ACCESS-001 --run-id real-subgraphservice-owner-access-001 --timeout 180
```

Result: `clean`

Meaning: the local harness deployed the real `SubgraphService` implementation through an `ERC1967Proxy`, initialized it with a local owner, and confirmed the selected owner-only economic setters reject a non-owner while accepting the owner.

Evidence:

- `foundry-result.json`
- `judgment.json`
- `../../pocs/generated/real-subgraphservice-owner-access-001/test/SubgraphServiceRealHarness.t.sol`

Security interpretation: this rejects the narrow `OWNER-ACCESS-001` hypothesis and is not report-ready evidence.

Next step: move from owner-access checks to value-flow setup for `register`, `startService`, `collect`, or indexing agreement transitions.
