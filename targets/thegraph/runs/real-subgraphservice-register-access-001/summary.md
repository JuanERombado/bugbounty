# SubgraphService REGISTER-ACCESS-001

Command:

```powershell
python -m backend.hotspot_hub.cli validate real-foundry-slice --target thegraph --repo-root external/thegraph-contracts --contract-path packages/subgraph-service/contracts/SubgraphService.sol --contract-name SubgraphService --hypothesis-id REGISTER-ACCESS-001 --run-id real-subgraphservice-register-access-001 --timeout 180
```

Result: `clean`

Meaning: the local harness deployed the real `SubgraphService` implementation through an `ERC1967Proxy`, mocked the Horizon staking and dispute-manager dependencies needed by registration, and verified three registration gate behaviors.

Checks:

- Authorized indexer with a valid provision can register and set `paymentsDestination`.
- Unauthorized caller cannot register on behalf of the indexer.
- Authorized caller without a provision cannot register.

Evidence:

- `foundry-result.json`
- `judgment.json`
- `../../pocs/generated/real-subgraphservice-register-access-001/test/SubgraphServiceRealHarness.t.sol`

Security interpretation: this rejects the narrow `REGISTER-ACCESS-001` hypothesis and is not report-ready evidence.

Next step: extend this mock setup into `startService` allocation accounting or `collect` value-flow invariants.
