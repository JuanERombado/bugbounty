# SubgraphService STARTSERVICE-ALLOCATION-001

Command:

```powershell
python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id STARTSERVICE-ALLOCATION-001 --run-id real-subgraphservice-startservice-allocation-001 --timeout 180
```

Result: `clean`

Meaning: the local harness deployed the real `SubgraphService` implementation through an `ERC1967Proxy`, registered an indexer through the real registration path, signed an allocation proof with a local Foundry key, and verified allocation accounting after `startService`.

Checks:

- `startService` creates an open allocation for the expected indexer.
- Allocation state records the expected subgraph deployment ID and token amount.
- `getSubgraphAllocatedTokens` increases by exactly the allocation token amount.
- Reusing the same allocation ID reverts.
- A mismatched allocation proof reverts.

Evidence:

- `foundry-result.json`
- `judgment.json`
- `../../pocs/generated/real-subgraphservice-startservice-allocation-001/test/SubgraphServiceRealHarness.t.sol`

Security interpretation: this rejects the narrow `STARTSERVICE-ALLOCATION-001` hypothesis and is not report-ready evidence.

Next step: extend the allocation setup into `resizeAllocation`, `stopService`, or `collect(IndexingRewards)` to test accounting reversals and reward state transitions.
