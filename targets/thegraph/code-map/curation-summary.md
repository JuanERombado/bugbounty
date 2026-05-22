# Curation Summary

## Plain-English Purpose

`Curation` lets curators deposit GRT into a subgraph deployment pool and receive signal shares that can later be burned for GRT from that same pool.

## Value Movement

- `mint` pulls GRT from the curator, burns any curation tax, adds the rest to the pool, and mints curation signal.
- `burn` burns a curator's signal, removes the calculated GRT from the pool, and sends that GRT to the curator.
- `collect` adds query-fee rewards to an existing curated pool, but it trusts the staking contract to have already transferred the GRT to `Curation`.

## Role Checks

- Normal users can call `mint` and `burn`.
- Only the configured staking contract can call `collect`.
- Only the governor can change reserve ratio, minimum deposit, curation tax, and token master.
- `mint` and `burn` are blocked when the protocol is partially paused.

## Accounting Invariants

- Pool token accounting should match the GRT actually held for that pool.
- Total pool signal should match the curation token supply.
- Burning all signal should empty the pool.
- Collected fees should be claimable by signal holders according to their share.
- Slippage checks must protect users from worse-than-expected signal or token output.

## First Things To Hunt

- Rounding dust after multiple curators enter and exit.
- Fee collection followed by partial burns and final burns.
- Minimum-deposit edge cases after a pool falls below the minimum.
- Trust boundary between staking `collect` and actual token transfers.
- GNS conversion between name signal and version signal.
