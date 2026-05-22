# GraphTokenLockWallet TLW3 Impact Notes

## Local Primitive

Removed token destinations keep old wallet allowances because `revokeProtocol()` only loops over the manager's current destination list.

## Real Destination Check

| Destination class | Pull behavior | Current impact read |
| --- | --- | --- |
| Legacy staking functions | Pull tokens from `msg.sender` during beneficiary-forwarded calls | Stale allowance alone does not let a third party drain a wallet. |
| L1 transfer tool | `depositToL2Locked` pulls from `msg.sender` and validates `msg.sender` as a wallet | Stale allowance is useful only when the wallet/beneficiary calls the tool. |
| L2 transfer tool | `withdrawToL1Locked` pulls from `msg.sender` and maps the L2 wallet back to L1 | Stale allowance is useful only when the wallet/beneficiary calls the tool. |
| Horizon staking | `delegate` and provision paths pull from `msg.sender` | Stale allowance alone does not show outsider-controlled drain. |
| Subgraph service `setPaymentsDestination` | No token pull in the allowed function itself | Not an allowance-drain path by itself. |
| Test-only `TokenPullerMock` | Can pull from arbitrary `_from` using existing allowance | Proves the primitive, not a real deployed impact. |

## Interpretation

TLW3 is a real authorization hygiene issue, but not yet an Immunefi-ready impact because current local sources do not show a real destination that lets an arbitrary caller spend a removed wallet allowance.

The strongest remaining angle is upgrade/deprecation risk: if a removed destination is an upgradeable proxy or later unsafe contract, existing wallets may have no way to revoke it through `revokeProtocol()` after removal.

## Next Step

Check deployment artifacts and upgradeability for token destinations, especially transfer-tool proxies and Horizon migration transactions.
