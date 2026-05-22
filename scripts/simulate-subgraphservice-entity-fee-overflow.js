#!/usr/bin/env node

const UINT256_MAX = (1n << 256n) - 1n;

function checkedMul(a, b) {
  const result = a * b;
  if (result > UINT256_MAX) throw new Error(`uint256 multiplication overflow: ${a} * ${b}`);
  return result;
}

function checkedAdd(a, b) {
  const result = a + b;
  if (result > UINT256_MAX) throw new Error(`uint256 addition overflow: ${a} + ${b}`);
  return result;
}

function subgraphServiceExpectedTokens({ collectionSeconds, tokensPerSecond, tokensPerEntityPerSecond, entities }) {
  const entityRate = checkedMul(tokensPerEntityPerSecond, entities);
  const rate = checkedAdd(tokensPerSecond, entityRate);
  return checkedMul(collectionSeconds, rate);
}

function recurringCollectorCap({ collectionSeconds, maxOngoingTokensPerSecond, maxInitialTokens, firstCollection }) {
  const ongoing = checkedMul(maxOngoingTokensPerSecond, collectionSeconds);
  return firstCollection ? checkedAdd(ongoing, maxInitialTokens) : ongoing;
}

const scenario = {
  collectionSeconds: 1n,
  tokensPerSecond: 0n,
  tokensPerEntityPerSecond: UINT256_MAX,
  entities: 2n,
  maxOngoingTokensPerSecond: 1_000_000_000_000_000_000n,
  maxInitialTokens: 0n,
  firstCollection: false,
};

console.log("SubgraphService entity-fee overflow simulation");
console.log(`UINT256_MAX = ${UINT256_MAX}`);
console.log("Scenario:");
for (const [key, value] of Object.entries(scenario)) console.log(`  ${key}: ${value}`);

try {
  const expected = subgraphServiceExpectedTokens(scenario);
  console.log(`SubgraphService expectedTokens: ${expected}`);
} catch (error) {
  console.log(`SubgraphService expectedTokens: REVERT (${error.message})`);
}

try {
  const cap = recurringCollectorCap(scenario);
  console.log(`RecurringCollector cap: ${cap}`);
} catch (error) {
  console.log(`RecurringCollector cap: REVERT (${error.message})`);
}

