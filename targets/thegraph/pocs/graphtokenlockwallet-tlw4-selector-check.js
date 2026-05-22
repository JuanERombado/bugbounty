const { createRequire } = require('module')
const path = require('path')

const graphRequire = createRequire(
  path.join(__dirname, '../../../external/thegraph-contracts/packages/token-distribution/package.json'),
)
const { utils } = graphRequire('ethers')

const walletFunctions = [
  'initialize(address,address,address,address,uint256,uint256,uint256,uint256,uint256,uint256,uint8)',
  'setManager(address)',
  'approveProtocol()',
  'revokeProtocol()',
  'release()',
  'withdrawSurplus(uint256)',
  'revoke()',
  'acceptLock()',
  'cancelLock()',
  'setBeneficiary(address)',
]

const authorizedFunctions = [
  'stake(uint256)',
  'unstake(uint256)',
  'withdraw()',
  'delegate(address,uint256)',
  'undelegate(address,uint256)',
  'withdrawDelegated(address,address)',
  'setDelegationParameters(uint32,uint32,uint32)',
  'setOperator(address,bool)',
  'depositToL2Locked(uint256,address,uint256,uint256,uint256)',
  'withdrawETH(address,uint256)',
  'setL2WalletAddressManually(address)',
  'transferLockedDelegationToL2(address,uint256,uint256,uint256)',
  'transferLockedStakeToL2(uint256,uint256,uint256,uint256)',
  'withdrawToL1Locked(uint256)',
  'provisionLocked(address,address,uint256,uint32,uint64)',
  'thaw(address,address,uint256)',
  'deprovision(address,address,uint256)',
  'setDelegationFeeCut(address,address,uint8,uint256)',
  'setOperatorLocked(address,address,bool)',
  'withdrawDelegated(address,address,uint256)',
  'setPaymentsDestination(address)',
]

const bySelector = new Map()

for (const group of [
  ['wallet', walletFunctions],
  ['authorized', authorizedFunctions],
]) {
  for (const signature of group[1]) {
    const selector = utils.id(signature).slice(0, 10)
    const entries = bySelector.get(selector) || []
    entries.push({ group: group[0], signature })
    bySelector.set(selector, entries)
  }
}

const collisions = [...bySelector.entries()].filter(([, entries]) => entries.length > 1)

console.log('Checked signatures:', walletFunctions.length + authorizedFunctions.length)
console.log('Collisions:', collisions.length)
for (const [selector, entries] of collisions) {
  console.log(selector)
  for (const entry of entries) {
    console.log(`  ${entry.group}: ${entry.signature}`)
  }
}
