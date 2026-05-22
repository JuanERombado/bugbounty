// Local-only model for BC5: invalid permit can fall back to existing allowance.

const assert = require("assert");

class MockPermitToken {
  constructor() {
    this.allowances = new Map();
    this.permitCalls = 0;
  }

  allowance(owner, spender) {
    return this.allowances.get(`${owner}:${spender}`) || 0;
  }

  setAllowance(owner, spender, amount) {
    this.allowances.set(`${owner}:${spender}`, amount);
  }

  permit() {
    this.permitCalls += 1;
    throw new Error("GRT: invalid permit");
  }
}

function permitFallback({ token, owner, spender, value }) {
  try {
    token.permit(owner, spender, value);
    return { ok: true, path: "permit" };
  } catch (error) {
    if (token.allowance(owner, spender) >= value) {
      return { ok: true, path: "existing allowance" };
    }
    return { ok: false, error: error.message };
  }
}

function addToL2WithPermit({ token, sender, user, amount }) {
  assert.notStrictEqual(amount, 0, "Must add more than 0");
  assert.notStrictEqual(user, "0x0", "destination != 0");
  if (user !== sender) {
    throw new Error("Only tokens owner can call");
  }

  const permitResult = permitFallback({
    token,
    owner: user,
    spender: "BillingConnector",
    value: amount,
  });

  if (!permitResult.ok) {
    throw new Error(permitResult.error);
  }

  return { event: "TokensSentToL2", owner: user, destination: user, amount, permitPath: permitResult.path };
}

function runCaseOwnerWithExistingAllowance() {
  const token = new MockPermitToken();
  token.setAllowance("alice", "BillingConnector", 100);
  const result = addToL2WithPermit({ token, sender: "alice", user: "alice", amount: 50 });

  assert.strictEqual(result.permitPath, "existing allowance");
  return { name: "owner invalid permit with existing allowance", result };
}

function runCaseOwnerWithoutAllowance() {
  const token = new MockPermitToken();
  let error;
  try {
    addToL2WithPermit({ token, sender: "alice", user: "alice", amount: 50 });
  } catch (err) {
    error = err.message;
  }

  assert.strictEqual(error, "GRT: invalid permit");
  return { name: "owner invalid permit without allowance", error };
}

function runCaseThirdPartyCannotUseAllowance() {
  const token = new MockPermitToken();
  token.setAllowance("alice", "BillingConnector", 100);
  let error;
  try {
    addToL2WithPermit({ token, sender: "mallory", user: "alice", amount: 50 });
  } catch (err) {
    error = err.message;
  }

  assert.strictEqual(error, "Only tokens owner can call");
  return { name: "third party cannot use owner allowance", error };
}

const cases = [
  runCaseOwnerWithExistingAllowance(),
  runCaseOwnerWithoutAllowance(),
  runCaseThirdPartyCannotUseAllowance(),
];

console.log(
  JSON.stringify(
    {
      hypothesis: "BC5",
      result:
        "invalid permit can fall back to existing allowance, but only the token owner can trigger the path",
      cases,
    },
    null,
    2,
  ),
);
