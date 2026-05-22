// Local-only arithmetic model for GraphTokenLock TLW1.
// Mirrors availableAmount(), releasableAmount(), release(), totalOutstandingAmount(), and surplusAmount().

const assert = require("assert");

class TokenLockModel {
  constructor({ managedAmount, startTime, endTime, periods, balance }) {
    this.managedAmount = BigInt(managedAmount);
    this.startTime = BigInt(startTime);
    this.endTime = BigInt(endTime);
    this.periods = BigInt(periods);
    this.balance = BigInt(balance);
    this.releasedAmount = 0n;
    this.revokedAmount = 0n;
  }

  duration() {
    return this.endTime - this.startTime;
  }

  periodDuration() {
    return this.duration() / this.periods;
  }

  amountPerPeriod() {
    return this.managedAmount / this.periods;
  }

  sinceStartTime(now) {
    const current = BigInt(now);
    if (current <= this.startTime) return 0n;
    return current - this.startTime;
  }

  currentPeriod(now) {
    return this.sinceStartTime(now) / this.periodDuration() + 1n;
  }

  passedPeriods(now) {
    return this.currentPeriod(now) - 1n;
  }

  availableAmount(now) {
    const current = BigInt(now);
    if (current < this.startTime) return 0n;
    if (current > this.endTime) return this.managedAmount;
    return this.passedPeriods(now) * this.amountPerPeriod();
  }

  releasableAmount(now) {
    const releasable = this.availableAmount(now) - this.releasedAmount;
    return this.balance < releasable ? this.balance : releasable;
  }

  release(now) {
    const amount = this.releasableAmount(now);
    assert(amount > 0n, "No available releasable amount");
    this.releasedAmount += amount;
    this.balance -= amount;
    return amount;
  }

  totalOutstandingAmount() {
    if (this.releasedAmount + this.revokedAmount > this.managedAmount) {
      throw new Error("SafeMath: subtraction overflow");
    }
    return this.managedAmount - this.releasedAmount - this.revokedAmount;
  }

  surplusAmount() {
    const outstanding = this.totalOutstandingAmount();
    return this.balance > outstanding ? this.balance - outstanding : 0n;
  }
}

function runCaseCleanlyDivisibleSchedule() {
  const lock = new TokenLockModel({
    managedAmount: 60n,
    startTime: 100n,
    endTime: 160n,
    periods: 6n,
    balance: 70n,
  });
  const released = lock.release(160n);

  assert.strictEqual(released, 60n);
  assert.strictEqual(lock.releasedAmount, 60n);
  assert.strictEqual(lock.surplusAmount(), 10n);
  return {
    name: "cleanly divisible schedule at endTime",
    released: released.toString(),
    releasedAmount: lock.releasedAmount.toString(),
    surplus: lock.surplusAmount().toString(),
  };
}

function runCaseUnevenDurationOverstatesAvailableAtEndTime() {
  const lock = new TokenLockModel({
    managedAmount: 60n,
    startTime: 100n,
    endTime: 110n,
    periods: 6n,
    balance: 70n,
  });
  const released = lock.release(110n);
  let outstandingError = null;
  try {
    lock.totalOutstandingAmount();
  } catch (error) {
    outstandingError = error.message;
  }

  assert.strictEqual(released, 70n);
  assert.strictEqual(lock.releasedAmount, 70n);
  assert.strictEqual(outstandingError, "SafeMath: subtraction overflow");
  return {
    name: "uneven duration at exact endTime consumes surplus",
    released: released.toString(),
    releasedAmount: lock.releasedAmount.toString(),
    managedAmount: lock.managedAmount.toString(),
    outstandingError,
  };
}

function runCaseAfterEndTimeCapsToManagedAmount() {
  const lock = new TokenLockModel({
    managedAmount: 60n,
    startTime: 100n,
    endTime: 110n,
    periods: 6n,
    balance: 70n,
  });
  const released = lock.release(111n);

  assert.strictEqual(released, 60n);
  assert.strictEqual(lock.surplusAmount(), 10n);
  return {
    name: "after endTime caps to managed amount",
    released: released.toString(),
    releasedAmount: lock.releasedAmount.toString(),
    surplus: lock.surplusAmount().toString(),
  };
}

const cases = [
  runCaseCleanlyDivisibleSchedule(),
  runCaseUnevenDurationOverstatesAvailableAtEndTime(),
  runCaseAfterEndTimeCapsToManagedAmount(),
];

console.log(
  JSON.stringify(
    {
      hypothesis: "TLW1",
      result:
        "model finds a narrow exact-endTime uneven-duration case where release can consume surplus and make outstanding accounting underflow",
      cases,
    },
    null,
    2,
  ),
);
