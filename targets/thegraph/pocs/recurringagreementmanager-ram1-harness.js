#!/usr/bin/env node

function currentBeforeCollection({ escrowBalance, managerBalance, tokensToCollect }) {
  if (tokensToCollect <= escrowBalance) return escrowBalance;
  const deficit = tokensToCollect - escrowBalance;
  if (deficit < managerBalance) return escrowBalance + deficit;
  return escrowBalance;
}

function expectedBeforeCollection({ escrowBalance, managerBalance, tokensToCollect }) {
  if (tokensToCollect <= escrowBalance) return escrowBalance;
  const deficit = tokensToCollect - escrowBalance;
  if (deficit <= managerBalance) return escrowBalance + deficit;
  return escrowBalance;
}

const scenario = {
  escrowBalance: 1000n,
  managerBalance: 250n,
  tokensToCollect: 1250n,
};

const current = currentBeforeCollection(scenario);
const expected = expectedBeforeCollection(scenario);

console.log("RAM1 exact-deficit JIT top-up model");
console.log(`escrowBalance=${scenario.escrowBalance}`);
console.log(`managerBalance=${scenario.managerBalance}`);
console.log(`tokensToCollect=${scenario.tokensToCollect}`);
console.log(`currentAfter=${current}`);
console.log(`expectedAfter=${expected}`);

if (current !== scenario.tokensToCollect && expected === scenario.tokensToCollect) {
  console.log("candidate=true: strict '<' skips an exact-deficit top-up");
  process.exit(0);
}

console.log("candidate=false");
process.exit(1);
