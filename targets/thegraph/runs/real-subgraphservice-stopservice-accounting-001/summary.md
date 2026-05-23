# SubgraphService STOPSERVICE-ACCOUNTING-001

Command:

```powershell
python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id STOPSERVICE-ACCOUNTING-001 --run-id real-subgraphservice-stopservice-accounting-001 --timeout 180
```

Result: `clean`

Meaning: the local harness deployed the real `SubgraphService` implementation, registered an indexer, opened an allocation, stopped service for that allocation, and verified close accounting was released.

Checks:

- `stopService` changes the allocation from open to closed.
- Historical allocation owner, subgraph deployment ID, and token amount remain queryable.
- `getSubgraphAllocatedTokens` returns to zero after close.
- `allocationProvisionTracker(indexer)` returns to zero after close.
- Stopping the same closed allocation twice reverts.
- Unauthorized stop attempt reverts.

Evidence:

- `foundry-result.json`
- `judgment.json`
- `../../pocs/generated/real-subgraphservice-stopservice-accounting-001/test/SubgraphServiceRealHarness.t.sol`

Security interpretation: this rejects the narrow `STOPSERVICE-ACCOUNTING-001` hypothesis and is not report-ready evidence.

Next step: move from allocation lifecycle accounting into `collect(IndexingRewards)` or query/indexing fee collection, where reward/payment value movement is more likely to expose high-value bugs.
