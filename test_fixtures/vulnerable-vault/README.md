# Vulnerable Vault Fixture

This fixture is a tiny local-only target for proving the workbench validation loop before touching real bounty code.

## Seeded Bugs

1. Accounting bug: `VulnerableVault.withdraw` sends ETH out but does not decrement `totalDeposits`.
2. Access-control bug: `VulnerableVault.setFeeRecipient` has no owner check.

`FixedVault` in the same source file shows the expected invariant behavior:

- `address(this).balance == totalDeposits`
- only the owner can set `feeRecipient`

## Demo

```powershell
python -m backend.hotspot_hub.cli validate fixture-slice --fixture vulnerable-vault
```

Expected result:

- vulnerable invariant run fails
- fixed invariant run passes
- judgment status is `reproduced`
