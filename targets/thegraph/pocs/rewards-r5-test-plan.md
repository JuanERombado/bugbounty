# Rewards R5 Test Plan

## Question

Can L2 reward issuance exceed the L1 bridge mint allowance and allow too much GRT to be minted on L1?

## Local-Only Setup

- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/gateway/l1GraphTokenGateway.test.ts`
- Contract under test: `L1GraphTokenGateway`
- Related concern: L2 reward issuance must stay coordinated with L1 mint allowance.

## Tests Used

- `mints tokens up to the L2 mint allowance`
- `does not reuse consumed L2 mint allowance after a mixed escrow and mint withdrawal`
- `reverts if the amount to mint is over the allowance`

## Expected Safe Behavior

The L1 gateway may mint only the shortfall above escrow balance and only within the remaining L2 mint allowance.

## Result

Rejected.

The L1 gateway enforced the allowance and rejected over-minting.

## Command

```powershell
pnpm exec hardhat test --network hardhat tests/unit/gateway/l1GraphTokenGateway.test.ts --grep "mints tokens up to the L2 mint allowance|amount to mint is over the allowance|does not reuse consumed"
```

## Evidence

- `3 passing`
- Minting up to the cap succeeds.
- Minting over the cap reverts.
- Previously consumed allowance cannot be reused after a mixed escrow-plus-mint withdrawal.

## Next Step

Move to `DisputeManager` and map value movement, slashing paths, arbitrator roles, and dispute lifecycle invariants.
