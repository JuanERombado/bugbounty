# PaymentsEscrow Summary

## Plain-English Purpose

`PaymentsEscrow` holds GRT for payer, collector, and receiver tuples, then lets the collector collect payment or the payer thaw and withdraw unused escrow.

## Value Movement

- `deposit` pulls GRT from `msg.sender` and credits `msg.sender` as payer.
- `depositTo` pulls GRT from `msg.sender` but credits an arbitrary payer account.
- `thaw` marks part of a payer account for withdrawal after the escrow thawing period.
- `adjustThaw` changes the thaw amount and can preserve or reset the thaw timer depending on direction and flag.
- `withdraw` sends thawed tokens back to the payer.
- `collect` is called by a collector and pays through `GraphPayments`, reducing escrow balance first.

## Role Checks

- Only the payer controls thaw, cancel thaw, and withdraw for its own escrow account.
- Any caller can fund any payer account using `depositTo`, but the caller supplies the tokens.
- The collector is implicitly `msg.sender` in `collect`.
- `collect` is limited by the payer/collector/receiver escrow account balance.
- All mutating functions require the controller not to be paused.

## Accounting Invariants

- Escrow account `balance` should match funds available to the payer/collector tuple.
- `tokensThawing` should never exceed `balance` after collection.
- `getBalance` reports collectable balance as `balance - tokensThawing`.
- Collection should reduce the escrow contract token balance by exactly the collected amount.
- Withdraw should pay at most `min(tokensThawing, balance)` to the payer.

## First Things To Hunt

- `depositTo` interactions with payer-controlled thawing and agreement accounting.
- Collection while a full balance is thawing.
- Timer reset behavior around `thaw` versus `adjustThaw`.
- External call ordering in `collect`.
- Pause behavior across escrow and collector contracts.

## Next Step

Map `RecurringCollector`, because it decides when escrowed funds are collectable.
