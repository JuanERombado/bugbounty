# Next Paid-Report Step

The next best move is to stop broad exploration and run one focused paid-impact lane end to end.

## Recommended Lane

Continue with `SubgraphService` payment flow because it touches payer funds, agreements, collector payments, escrow accounting, and agreement lifecycle state.

## Why This Lane

- It is closer to money movement than generic code quality issues.
- It has several interacting contracts, which increases the chance of logic gaps.
- It follows the current research thread after RAM1 was stopped by duplicate-risk review.
- It can be tested locally without touching live deployments.

## Immediate Workflow

1. Re-read `targets/thegraph/code-map/subgraphservice-payment-flow-summary.md`.
2. Pick exactly one hypothesis from `targets/thegraph/hypotheses/subgraphservice-payment-flow-hypotheses.md`.
3. Run the duplicate-risk gate before writing more PoC code.
4. Convert only the strongest surviving hypothesis into a Foundry or Hardhat local test.
5. If the test fails to prove paid impact, reject it quickly and move to the next hypothesis.

## Success Criteria

A paid-report candidate must show:

- Explicit in-scope asset.
- Exact accepted impact.
- Local-only reproducible PoC.
- Concrete accounting, fund-loss, unauthorized payment, or blocked-withdrawal impact.
- Duplicate-risk notes showing why it is not already covered.

## Avoid

- More broad scanning before choosing a single hypothesis.
- Reporting scanner output without local proof.
- Chasing RAM1 unless it is materially different from Trust audit `TRST-M-2`.
- Spending time on medium/low issues unless they can be reframed into accepted high or critical impact.
