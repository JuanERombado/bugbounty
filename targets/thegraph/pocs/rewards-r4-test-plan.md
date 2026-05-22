# Rewards R4 Test Plan

## Question

Can switching between local issuance and allocator-controlled issuance double count or drop rewards?

## Local-Only Setup

- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/rewards/rewards-issuance-allocator.test.ts`
- Contract under test: `RewardsManager`
- Helper contract: `MockIssuanceAllocator`

## Test Used

- `should accumulate rewards using allocator rate over time`
- `should maintain reward consistency when switching between rates`

## Expected Safe Behavior

Rewards should accrue at the active rate for each phase, and total accumulated rewards should equal the sum of local-rate and allocator-rate periods.

## Result

Rejected.

The focused local tests passed, including a switch from local issuance to allocator issuance and back to local issuance.

## Command

```powershell
pnpm exec hardhat test --network hardhat tests/unit/rewards/rewards-issuance-allocator.test.ts --grep "accumulate rewards using allocator rate|maintain reward consistency"
```

## Evidence

- `2 passing`
- Allocator-rate accrual matched the configured allocator rate.
- Local-to-allocator-to-local switching preserved phase-by-phase reward consistency.

## Next Step

Test R1 by checking whether minimum-signal threshold changes affect pending rewards exactly as documented.
