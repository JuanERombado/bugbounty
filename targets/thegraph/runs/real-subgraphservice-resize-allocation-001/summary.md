# SubgraphService RESIZE-ALLOCATION-001

Command:

```powershell
python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id RESIZE-ALLOCATION-001 --run-id real-subgraphservice-resize-allocation-001 --timeout 180
```

Result: `clean`

Meaning: the local harness deployed the real `SubgraphService` implementation, registered an indexer, opened an allocation, resized it up and down, and verified allocation accounting stayed synchronized.

Checks:

- Resize from 2 ether to 5 ether updates allocation tokens.
- Resize from 5 ether to 1 ether updates allocation tokens.
- `getSubgraphAllocatedTokens` matches the resized amount after each transition.
- `allocationProvisionTracker(indexer)` matches the resized amount after each transition.
- Same-size resize reverts.
- Unauthorized resize reverts.

Evidence:

- `foundry-result.json`
- `judgment.json`
- `../../pocs/generated/real-subgraphservice-resize-allocation-001/test/SubgraphServiceRealHarness.t.sol`

Security interpretation: this rejects the narrow `RESIZE-ALLOCATION-001` hypothesis and is not report-ready evidence.

Next step: extend this setup into `stopService` to confirm allocation close reverses subgraph and provision accounting cleanly.
