// Local-only model for TLW3: removing a token destination does not revoke wallet allowances.

const assert = require("assert");

class MockToken {
  constructor() {
    this.allowances = new Map();
  }

  approve(owner, spender, amount) {
    this.allowances.set(`${owner}:${spender}`, BigInt(amount));
  }

  allowance(owner, spender) {
    return this.allowances.get(`${owner}:${spender}`) || 0n;
  }
}

class MockManager {
  constructor() {
    this.destinations = [];
  }

  addTokenDestination(destination) {
    this.destinations.push(destination);
  }

  removeTokenDestination(destination) {
    this.destinations = this.destinations.filter((value) => value !== destination);
  }

  getTokenDestinations() {
    return this.destinations;
  }
}

function approveProtocol({ token, manager, wallet }) {
  for (const destination of manager.getTokenDestinations()) {
    token.approve(wallet, destination, (1n << 256n) - 1n);
  }
}

function revokeProtocol({ token, manager, wallet }) {
  for (const destination of manager.getTokenDestinations()) {
    token.approve(wallet, destination, 0n);
  }
}

function runCaseRemovedDestinationKeepsAllowance() {
  const token = new MockToken();
  const manager = new MockManager();
  const wallet = "tokenLockWallet";
  const staking = "staking";

  manager.addTokenDestination(staking);
  approveProtocol({ token, manager, wallet });
  manager.removeTokenDestination(staking);
  revokeProtocol({ token, manager, wallet });

  const allowance = token.allowance(wallet, staking);
  assert(allowance > 0n, "removed destination allowance should remain in this model");
  return {
    name: "removed destination keeps allowance",
    managerDestinations: manager.getTokenDestinations(),
    allowanceStillSet: allowance.toString(),
  };
}

const cases = [runCaseRemovedDestinationKeepsAllowance()];

console.log(
  JSON.stringify(
    {
      hypothesis: "TLW3",
      result:
        "model confirms revokeProtocol only revokes current manager destinations, so removed destinations can keep prior allowance",
      cases,
    },
    null,
    2,
  ),
);
