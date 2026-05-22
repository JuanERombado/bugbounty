# Curation Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`.

## C1: Multi-Curator Exits Can Leave Unclaimable Pool Dust

- Status: rejected
- Asset: Curation
- Hypothesis: rounding across multiple curators and collected fees can leave GRT or signal dust trapped after all curators exit.
- Why it might matter: trapped pool value is direct user value loss if material or repeatable.
- Impact if true: user funds stuck or incorrectly distributed.
- Minimal local test idea: two curators mint, staking collects fees, both curators fully burn, and final pool tokens/signal should be zero.
- Evidence that rejects it: final burn clears pool tokens and pool signal.
- Result: targeted local test passed; two curators minted, fees were collected, both fully exited, and final pool tokens/signal were zero.
- Rejection reason: the final burn clears pool accounting even after multi-curator fee distribution.

## C2: `collect` Can Overstate Pool Tokens If Staking Does Not Transfer GRT

- Status: rejected
- Asset: Curation / Staking
- Hypothesis: `collect` increments pool tokens without pulling GRT itself, so a bad staking path could make curation accounting exceed actual GRT balance.
- Why it might matter: later burns may fail or drain unrelated funds.
- Impact if true: accounting mismatch or user funds at risk.
- Out-of-scope risk: if it requires malicious or privileged staking behavior, it may not be a Curation bug by itself.
- Minimal local test idea: impersonate staking, call `collect` without transferring GRT, then attempt burns and check accounting mismatch.
- Evidence that rejects it: real staking paths always transfer GRT before `collect`.
- Result: invariant added to the real `Staking.collect` test helper; curation pool token increases match actual GRT balance increases in `Curation`.
- Rejection reason: the real staking path pushes tokens before calling `Curation.collect`; a fake staking caller requires privileged controller configuration.

## C3: Below-Minimum Pool State Can Be Abused

- Status: new
- Asset: Curation
- Hypothesis: after burns leave a curated pool below `minimumCurationDeposit`, later small mints may behave unexpectedly.
- Why it might matter: minimum-deposit logic only applies to uninitialized pools.
- Impact if true: share/accounting manipulation around very small pools.
- Minimal local test idea: burn nearly all signal, mint small amounts below minimum, and check value conservation.
- Evidence that rejects it: existing tests show below-minimum existing pools can still receive deposits safely.

## C4: Slippage Checks Miss A State Change

- Status: rejected
- Asset: Curation
- Hypothesis: `tokensToSignal` or `signalToTokens` can quote one value but state changes before execution produce a worse result not caught by slippage.
- Why it might matter: users rely on minimum output checks.
- Impact if true: users receive less signal/GRT than requested.
- Minimal local test idea: quote output, mutate pool, then call with stale minimum and confirm revert.
- Evidence that rejects it: stale minimum output reverts with `Slippage protection`.
- Result: targeted local mint test passed; after another curator changed the pool, using the stale signal quote as `_signalOutMin` reverted with `Slippage protection`.
- Rejection reason: mint-side stale quotes are protected by the minimum-output check.

## Picked First Test

C1 was tested first because it is a pure local accounting test with a clear pass/fail result and no live-system assumptions.

Next best target: `RewardsManager`, because the remaining Curation branches are either covered by existing tests or mostly governance/configuration edges.
