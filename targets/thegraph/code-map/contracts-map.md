# Contract Map

Source repo: `external\thegraph-contracts`

Use this as an index, then ask AI to explain one high-priority contract at a time.

## `packages\contracts\contracts\arbitrum\AddressAliasHelper.sol`

- Contracts: AddressAliasHelper
- Tags: bridge, permission
- Functions: applyL1ToL2Alias, undoL1ToL2Alias
- Modifiers: none
- Events: none

## `packages\contracts\contracts\arbitrum\L1ArbitrumMessenger.sol`

- Contracts: L1ArbitrumMessenger
- Tags: bridge, permission
- Functions: sendTxToL2, sendTxToL2, getBridge, getL2ToL1Sender
- Modifiers: none
- Events: TxToL2

## `packages\contracts\contracts\arbitrum\L2ArbitrumMessenger.sol`

- Contracts: L2ArbitrumMessenger
- Tags: bridge, permission
- Functions: sendTxToL1
- Modifiers: none
- Events: TxToL1

## `packages\contracts\contracts\bancor\BancorFormula.sol`

- Contracts: BancorFormula
- Tags: token
- Functions: calculatePurchaseReturn, calculateSaleReturn, calculateCrossReserveReturn, calculateFundCost, calculateLiquidateReturn, power, generalLog, floorLog2, findPositionInMaxExpArray, generalExp, optimalLog, optimalExp, calculateCrossConnectorReturn
- Modifiers: none
- Events: none

## `packages\contracts\contracts\curation\Curation.sol`

- Contracts: Curation
- Tags: curation, governance, graphtoken, rewards, rewardsmanager, staking, token
- Functions: initialize, setDefaultReserveRatio, setMinimumCurationDeposit, setCurationTaxPercentage, setCurationTokenMaster, collect, mint, burn, getCurationPoolTokens, isCurated, getCuratorSignal, getCurationPoolSignal, tokensToSignal, _tokensToSignal, signalToTokens, _setDefaultReserveRatio, _setMinimumCurationDeposit, _setCurationTaxPercentage, _setCurationTokenMaster, _updateRewards
- Modifiers: none
- Events: Signalled, Burned, Collected

## `packages\contracts\contracts\curation\CurationStorage.sol`

- Contracts: CurationV1Storage, CurationV2Storage, CurationV3Storage
- Tags: curation, governance, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\curation\GraphCurationToken.sol`

- Contracts: GraphCurationToken
- Tags: curation, governance, governor, token
- Functions: initialize, mint, burnFrom
- Modifiers: none
- Events: none

## `packages\contracts\contracts\discovery\erc1056\EthereumDIDRegistry.sol`

- Contracts: EthereumDIDRegistry
- Tags: registry
- Functions: identityOwner, checkSignature, validDelegate, changeOwner, changeOwner, changeOwnerSigned, addDelegate, addDelegate, addDelegateSigned, revokeDelegate, revokeDelegate, revokeDelegateSigned, setAttribute, setAttribute, setAttributeSigned, revokeAttribute, revokeAttribute, revokeAttributeSigned
- Modifiers: onlyOwner
- Events: DIDOwnerChanged, DIDDelegateChanged, DIDAttributeChanged

## `packages\contracts\contracts\discovery\GNS.sol`

- Contracts: GNS
- Tags: connector, curation, governance, token
- Functions: initialize, approveAll, setOwnerTaxPercentage, setSubgraphNFT, setCounterpartGNSAddress, setDefaultName, updateSubgraphMetadata, publishNewSubgraph, publishNewVersion, deprecateSubgraph, mintSignal, burnSignal, transferSignal, withdraw, migrateLegacySubgraph, subgraphSignal, subgraphTokens, isLegacySubgraph, tokensToNSignal, nSignalToTokens, vSignalToNSignal, nSignalToVSignal, getCuratorSignal, isPublished, getLegacySubgraphKey
- Modifiers: onlySubgraphAuth
- Events: SubgraphNFTUpdated, SetDefaultName, SubgraphMetadataUpdated, SubgraphVersionUpdated, SignalMinted, SignalBurned, SignalTransferred, SubgraphPublished, SubgraphUpgraded, SubgraphDeprecated, GRTWithdrawn, CounterpartGNSAddressUpdated, LegacySubgraphClaimed

## `packages\contracts\contracts\discovery\GNSStorage.sol`

- Contracts: GNSV1Storage, GNSV2Storage, GNSV3Storage
- Tags: curation, governance, l1gns, registry
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\discovery\L1GNS.sol`

- Contracts: L1GNS
- Tags: bridge, curation, graphtoken, l1gns, token
- Functions: sendSubgraphToL2, sendCuratorBalanceToBeneficiaryOnL2, _sendTokensAndMessageToL2GNS
- Modifiers: none
- Events: SubgraphSentToL2, CuratorBalanceSentToL2

## `packages\contracts\contracts\discovery\L1GNSStorage.sol`

- Contracts: L1GNSV1Storage
- Tags: l1gns
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\discovery\ServiceRegistry.sol`

- Contracts: ServiceRegistry
- Tags: governance, registry, staking
- Functions: _isAuth, initialize, register, registerFor, _register, unregister, unregisterFor, _unregister, isRegistered
- Modifiers: none
- Events: ServiceRegistered, ServiceUnregistered

## `packages\contracts\contracts\discovery\ServiceRegistryStorage.sol`

- Contracts: ServiceRegistryV1Storage
- Tags: governance, registry
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\discovery\SubgraphNFT.sol`

- Contracts: SubgraphNFT
- Tags: governance, governor, token
- Functions: setMinter, _setMinter, setTokenDescriptor, _setTokenDescriptor, setBaseURI, mint, burn, setSubgraphMetadata, tokenURI
- Modifiers: onlyMinter
- Events: MinterUpdated, TokenDescriptorUpdated, SubgraphMetadataUpdated

## `packages\contracts\contracts\discovery\SubgraphNFTDescriptor.sol`

- Contracts: SubgraphNFTDescriptor
- Tags: token
- Functions: tokenURI
- Modifiers: none
- Events: none

## `packages\contracts\contracts\disputes\DisputeManager.sol`

- Contracts: DisputeManager
- Tags: disputemanager, disputes, governance, slashing, staking, token, dispute
- Functions: _onlyArbitrator, initialize, setArbitrator, _setArbitrator, setMinimumDeposit, _setMinimumDeposit, setFishermanRewardPercentage, _setFishermanRewardPercentage, setSlashingPercentage, _setSlashingPercentage, isDisputeCreated, encodeHashReceipt, areConflictingAttestations, getAttestationIndexer, createQueryDispute, createQueryDisputeConflict, _createQueryDisputeWithAttestation, createIndexingDispute, _createIndexingDisputeWithAllocation, acceptDispute, rejectDispute, drawDispute, _isDisputeInConflict, _drawDisputeInConflict, _pullSubmitterDeposit
- Modifiers: onlyArbitrator, onlyPendingDispute
- Events: QueryDisputeCreated, IndexingDisputeCreated, DisputeAccepted, DisputeRejected, DisputeDrawn, DisputeLinked

## `packages\contracts\contracts\disputes\DisputeManagerStorage.sol`

- Contracts: DisputeManagerV1Storage
- Tags: disputemanager, disputes, governance, slashing, dispute
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\epochs\EpochManager.sol`

- Contracts: EpochManager
- Tags: governance, governor
- Functions: initialize, setEpochLength, runEpoch, isCurrentEpochRun, blockNum, blockHash, currentEpoch, currentEpochBlock, currentEpochBlockSinceStart, epochsSince, epochsSinceUpdate
- Modifiers: none
- Events: EpochRun, EpochLengthUpdate

## `packages\contracts\contracts\epochs\EpochManagerStorage.sol`

- Contracts: EpochManagerV1Storage
- Tags: governance
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\gateway\BridgeEscrow.sol`

- Contracts: BridgeEscrow
- Tags: bridge, bridgeescrow, escrow, governance, governor, graphtoken, token
- Functions: initialize, approveAll, revokeAll
- Modifiers: none
- Events: none

## `packages\contracts\contracts\gateway\GraphTokenGateway.sol`

- Contracts: GraphTokenGateway
- Tags: bridge, governance, governor, graphtoken, token
- Functions: setPauseGuardian, setPaused, paused, _notPaused, _checksBeforeUnpause
- Modifiers: onlyGovernorOrGuardian
- Events: none

## `packages\contracts\contracts\gateway\L1GraphTokenGateway.sol`

- Contracts: L1GraphTokenGateway
- Tags: bridge, bridgeescrow, escrow, governance, graphtoken, token
- Functions: initialize, setArbitrumAddresses, setL2TokenAddress, setL2CounterpartAddress, setEscrowAddress, addToCallhookAllowlist, removeFromCallhookAllowlist, updateL2MintAllowance, setL2MintAllowanceParametersManual, outboundTransfer, finalizeInboundTransfer, calculateL2TokenAddress, counterpartGateway, getOutboundCalldata, _checksBeforeUnpause, _parseOutboundData, accumulatedL2MintAllowanceAtBlock, _mintFromL2, _l2MintAmountAllowed
- Modifiers: onlyL2Counterpart
- Events: DepositInitiated, WithdrawalFinalized, ArbitrumAddressesSet, L2TokenAddressSet, L2CounterpartAddressSet, EscrowAddressSet, AddedToCallhookAllowlist, RemovedFromCallhookAllowlist, L2MintAllowanceUpdated, TokensMintedFromL2

## `packages\contracts\contracts\governance\Controller.sol`

- Contracts: Controller
- Tags: governance, governor, registry
- Functions: getGovernor, setContractProxy, unsetContractProxy, getContractProxy, updateController, setPartialPaused, setPaused, setPauseGuardian, paused, partialPaused
- Modifiers: onlyGovernorOrGuardian
- Events: SetContractProxy

## `packages\contracts\contracts\governance\Governed.sol`

- Contracts: Governed
- Tags: governance, governor
- Functions: _initialize, transferOwnership, acceptOwnership
- Modifiers: onlyGovernor
- Events: NewPendingOwnership, NewOwnership

## `packages\contracts\contracts\governance\Managed.sol`

- Contracts: Managed
- Tags: curation, governance, graphtoken, rewards, rewardsmanager, staking, token
- Functions: _notPartialPaused, _notPaused, _onlyGovernor, _onlyController, _initialize, setController, _setController, curation, epochManager, rewardsManager, staking, graphToken, graphTokenGateway, gns, _resolveContract, _syncContract, syncAllContracts
- Modifiers: notPartialPaused, notPaused, onlyController, onlyGovernor
- Events: ParameterUpdated, SetController, ContractSynced

## `packages\contracts\contracts\governance\Pausable.sol`

- Contracts: Pausable
- Tags: governance, governor
- Functions: _setPartialPaused, _setPaused, _setPauseGuardian
- Modifiers: none
- Events: PartialPauseChanged, PauseChanged, NewPauseGuardian

## `packages\contracts\contracts\l2\curation\L2Curation.sol`

- Contracts: L2Curation
- Tags: curation, governance, graphtoken, rewards, rewardsmanager, staking, token
- Functions: initialize, setDefaultReserveRatio, setMinimumCurationDeposit, setCurationTaxPercentage, setCurationTokenMaster, setSubgraphService, collect, mint, mintTaxFree, burn, getCurationPoolTokens, isCurated, getCuratorSignal, getCurationPoolSignal, tokensToSignal, tokensToSignalNoTax, tokensToSignalToTokensNoTax, signalToTokens, _setMinimumCurationDeposit, _setCurationTaxPercentage, _setCurationTokenMaster, _updateRewards, _tokensToSignal
- Modifiers: onlyGNS
- Events: Signalled, Burned, Collected, SubgraphServiceSet

## `packages\contracts\contracts\l2\discovery\L2GNS.sol`

- Contracts: L2GNS
- Tags: bridge, curation, graphtoken, token
- Functions: onTokenTransfer, finishSubgraphTransferFromL1, publishNewVersion, getAliasedL2SubgraphID, getUnaliasedL1SubgraphID, _receiveSubgraphFromL1, _mintSignalFromL1, _getSubgraphData
- Modifiers: onlyL2Gateway
- Events: SubgraphReceivedFromL1, SubgraphL2TransferFinalized, CuratorBalanceReceived, CuratorBalanceReturnedToBeneficiary

## `packages\contracts\contracts\l2\gateway\L2GraphTokenGateway.sol`

- Contracts: L2GraphTokenGateway
- Tags: bridge, governance, graphtoken, token
- Functions: initialize, setL2Router, setL1TokenAddress, setL1CounterpartAddress, outboundTransfer, finalizeInboundTransfer, outboundTransfer, calculateL2TokenAddress, getOutboundCalldata, _checksBeforeUnpause, _parseOutboundData
- Modifiers: onlyL1Counterpart
- Events: DepositFinalized, WithdrawalInitiated, L2RouterSet, L1TokenAddressSet, L1CounterpartAddressSet

## `packages\contracts\contracts\l2\staking\L2Staking.sol`

- Contracts: L2Staking
- Tags: bridge, delegation, graphtoken, staking, token
- Functions: onTokenTransfer, _receiveIndexerStake, _receiveDelegation
- Modifiers: onlyL2Gateway
- Events: StakeDelegated

## `packages\contracts\contracts\l2\token\GraphTokenUpgradeable.sol`

- Contracts: GraphTokenUpgradeable
- Tags: governance, governor, graphtoken, rewards, token
- Functions: permit, addMinter, removeMinter, renounceMinter, mint, isMinter, _initialize, _addMinter, _removeMinter, _getChainID
- Modifiers: onlyMinter
- Events: MinterAdded, MinterRemoved

## `packages\contracts\contracts\l2\token\L2GraphToken.sol`

- Contracts: L2GraphToken
- Tags: bridge, governance, governor, graphtoken, token
- Functions: initialize, setGateway, setL1Address, bridgeMint, bridgeBurn
- Modifiers: onlyGateway
- Events: BridgeMinted, BridgeBurned, GatewaySet, L1AddressSet

## `packages\contracts\contracts\payments\AllocationExchange.sol`

- Contracts: AllocationExchange
- Tags: governance, governor, graphtoken, staking, token
- Functions: approveAll, withdraw, setAuthority, _setAuthority, redeem, redeemMany, _redeem
- Modifiers: none
- Events: AuthoritySet, AllocationRedeemed, TokensWithdrawn

## `packages\contracts\contracts\rewards\RewardsManager.sol`

- Contracts: RewardsManager
- Tags: curation, governance, rewards, rewardsmanager, staking, token
- Functions: initialize, supportsInterface, setIssuancePerBlock, _setIssuancePerBlock, setSubgraphAvailabilityOracle, setMinimumSubgraphSignal, setSubgraphService, setIssuanceAllocator, beforeIssuanceAllocationChange, setProviderEligibilityOracle, setReclaimAddress, setDefaultReclaimAddress, setRevertOnIneligible, setDenied, _setDenied, isDenied, getAllocatedIssuancePerBlock, getRawIssuancePerBlock, getIssuanceAllocator, getReclaimAddress, getDefaultReclaimAddress, getProviderEligibilityOracle, getRevertOnIneligible, getNewRewardsPerSignal, _getNewRewardsPerSignal
- Modifiers: onlySubgraphAvailabilityOracle
- Events: none

## `packages\contracts\contracts\rewards\RewardsManagerStorage.sol`

- Contracts: RewardsManagerV1Storage, RewardsManagerV2Storage, RewardsManagerV3Storage, RewardsManagerV4Storage, RewardsManagerV5Storage, RewardsManagerV6Storage
- Tags: accounting, governance, rewards, rewardsmanager, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\rewards\SubgraphAvailabilityManager.sol`

- Contracts: SubgraphAvailabilityManager
- Tags: governance, governor, rewards, rewardsmanager
- Functions: setVoteTimeLimit, setOracle, vote, voteMany, _vote, checkVotes
- Modifiers: onlyOracle
- Events: OracleSet, VoteTimeLimitSet, OracleVote

## `packages\contracts\contracts\staking\L1Staking.sol`

- Contracts: L1Staking
- Tags: delegation, governor, graphtoken, l1staking, staking, token, vesting
- Functions: setL1GraphTokenLockTransferTool, transferStakeToL2, transferLockedStakeToL2, transferDelegationToL2, transferLockedDelegationToL2, unlockDelegationToTransferredIndexer, _transferStakeToL2, _transferDelegationToL2, _sendTokensAndMessageToL2Staking
- Modifiers: none
- Events: none

## `packages\contracts\contracts\staking\L1StakingStorage.sol`

- Contracts: L1StakingV1Storage
- Tags: delegation, graphtoken, l1staking, staking, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\staking\libs\Exponential.sol`

- Contracts: LibExponential
- Tags: rewards, staking
- Functions: exponentialRebates
- Modifiers: none
- Events: none

## `packages\contracts\contracts\staking\libs\LibFixedMath.sol`

- Contracts: LibFixedMath
- Tags: permission, staking
- Functions: one, add, sub, mul, div, mulDiv, uintMul, abs, invert, toFixed, toFixed, toFixed, toFixed, toInteger, ln, exp, _mul, _div, _add
- Modifiers: none
- Events: none

## `packages\contracts\contracts\staking\libs\MathUtils.sol`

- Contracts: MathUtils
- Tags: staking
- Functions: weightedAverageRoundingUp, min, diffOrZero
- Modifiers: none
- Events: none

## `packages\contracts\contracts\staking\libs\Stakes.sol`

- Contracts: Stakes
- Tags: staking, token
- Functions: deposit, release, allocate, unallocate, lockTokens, unlockTokens, withdrawTokens, tokensUsed, tokensSecureStake, tokensAvailable, tokensAvailableWithDelegation, tokensWithdrawable
- Modifiers: none
- Events: none

## `packages\contracts\contracts\staking\Staking.sol`

- Contracts: Staking
- Tags: curation, governance, graphtoken, l1staking, rewards, rewardsmanager, slashing, staking, token
- Functions: initialize, setExtensionImpl, setCounterpartStakingAddress, setMinimumIndexerStake, setThawingPeriod, setCurationPercentage, setProtocolPercentage, setMaxAllocationEpochs, setRebateParameters, setOperator, stake, unstake, withdraw, setRewardsDestination, allocate, allocateFrom, closeAllocation, collect, isAllocation, hasStake, getAllocation, getAllocationData, isActiveAllocation, getAllocationState, getSubgraphAllocatedTokens
- Modifiers: none
- Events: none

## `packages\contracts\contracts\staking\StakingExtension.sol`

- Contracts: StakingExtension
- Tags: delegation, governor, graphtoken, staking, token
- Functions: initialize, setDelegationTaxPercentage, setDelegationRatio, setDelegationUnbondingPeriod, setSlasher, delegate, undelegate, withdrawDelegated, slash, getDelegation, delegationRatio, delegationUnbondingPeriod, delegationTaxPercentage, delegationPools, rewardsDestination, operatorAuth, subgraphAllocations, slashers, minimumIndexerStake, thawingPeriod, curationPercentage, protocolPercentage, maxAllocationEpochs, alphaNumerator, alphaDenominator
- Modifiers: onlySlasher
- Events: none

## `packages\contracts\contracts\staking\StakingStorage.sol`

- Contracts: StakingV1Storage, StakingV2Storage, StakingV3Storage, StakingV4Storage
- Tags: curation, delegation, governance, slashing, staking, token, dispute
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\arbitrum\ArbSysMock.sol`

- Contracts: ArbSysMock
- Tags: graphtoken, token
- Functions: sendTxToL1
- Modifiers: none
- Events: L2ToL1Tx

## `packages\contracts\contracts\tests\arbitrum\BridgeMock.sol`

- Contracts: BridgeMock
- Tags: bridge
- Functions: deliverMessageToInbox, executeCall, setInbox, setOutbox, activeOutbox, allowedInboxes, allowedOutboxes, messageCount
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\arbitrum\InboxMock.sol`

- Contracts: InboxMock
- Tags: bridge
- Functions: sendL2Message, setBridge, sendUnsignedTransaction, sendContractTransaction, sendL1FundedUnsignedTransaction, sendL1FundedContractTransaction, createRetryableTicket, depositEth, pauseCreateRetryables, unpauseCreateRetryables, startRewriteAddress, stopRewriteAddress, _deliverMessage, deliverToBridge
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\arbitrum\OutboxMock.sol`

- Contracts: OutboxMock
- Tags: bridge
- Functions: setBridge, l2ToL1Sender, l2ToL1Block, l2ToL1EthBlock, l2ToL1Timestamp, l2ToL1BatchNum, l2ToL1OutputId, processOutgoingMessages, outboxEntryExists, executeTransaction, executeBridgeCall
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\CallhookReceiverMock.sol`

- Contracts: CallhookReceiverMock
- Tags: token
- Functions: onTokenTransfer
- Modifiers: none
- Events: TransferReceived

## `packages\contracts\contracts\tests\ens\IENS.sol`

- Contracts: IENS
- Tags: registry
- Functions: owner, setSubnodeRecord
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\GovernedMock.sol`

- Contracts: GovernedMock
- Tags: governance, governor
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\L1GraphTokenLockTransferToolBadMock.sol`

- Contracts: L1GraphTokenLockTransferToolBadMock
- Tags: graphtoken, token
- Functions: setL2WalletAddress, pullETH
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\L1GraphTokenLockTransferToolMock.sol`

- Contracts: L1GraphTokenLockTransferToolMock
- Tags: graphtoken, token
- Functions: setL2WalletAddress, pullETH
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\LegacyGNSMock.sol`

- Contracts: LegacyGNSMock
- Tags: l1gns
- Functions: createLegacySubgraph, getSubgraphDeploymentID, getSubgraphNSignal
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\MockIssuanceAllocator.sol`

- Contracts: MockIssuanceAllocator
- Tags: rewards, rewardsmanager
- Functions: callBeforeIssuanceAllocationChange, getTargetIssuancePerBlock, distributeIssuance, setTargetAllocation, supportsInterface
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\MockRewardsEligibilityOracle.sol`

- Contracts: MockRewardsEligibilityOracle
- Tags: rewards
- Functions: setIndexerEligible, setDefaultResponse, isEligible, supportsInterface
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\MockSubgraphService.sol`

- Contracts: MockSubgraphService
- Tags: rewards, rewardsmanager, token
- Functions: setAllocation, setSubgraphAllocatedTokens, getAllocationData, getSubgraphAllocatedTokens, callReclaimRewards
- Modifiers: none
- Events: none

## `packages\contracts\contracts\token\GraphToken.sol`

- Contracts: GraphToken
- Tags: governance, governor, graphtoken, rewards, rewardsmanager, token
- Functions: permit, addMinter, removeMinter, renounceMinter, mint, isMinter, _addMinter, _removeMinter, _getChainID
- Modifiers: onlyMinter
- Events: MinterAdded, MinterRemoved

## `packages\contracts\contracts\upgrades\GraphProxyAdmin.sol`

- Contracts: GraphProxyAdmin
- Tags: governance, governor
- Functions: getProxyImplementation, getProxyPendingImplementation, getProxyAdmin, changeProxyAdmin, upgrade, acceptProxy, acceptProxyAndCall
- Modifiers: none
- Events: none

## `packages\contracts\contracts\utils\TokenUtils.sol`

- Contracts: TokenUtils
- Tags: graphtoken, token
- Functions: pullTokens, pushTokens, burnTokens
- Modifiers: none
- Events: none

## `packages\horizon\contracts\data-service\DataService.sol`

- Contracts: DataService
- Tags: delegation, token
- Functions: getThawingPeriodRange, getVerifierCutRange, getProvisionTokensRange, getDelegationRatio, __DataService_init, __DataService_init_unchained
- Modifiers: none
- Events: none

## `packages\horizon\contracts\data-service\extensions\DataServiceFees.sol`

- Contracts: DataServiceFees
- Tags: delegation, staking, token
- Functions: releaseStake, _lockStake, _releaseStake, _processStakeClaim, _deleteStakeClaim, _getNextStakeClaim
- Modifiers: none
- Events: none

## `packages\horizon\contracts\data-service\extensions\DataServiceFeesStorage.sol`

- Contracts: DataServiceFeesV1Storage
- Tags: token
- Functions: none
- Modifiers: none
- Events: none

## `packages\horizon\contracts\data-service\libraries\ProvisionTracker.sol`

- Contracts: ProvisionTracker
- Tags: delegation, economic, staking, token
- Functions: lock, release, check
- Modifiers: none
- Events: none

## `packages\horizon\contracts\data-service\libraries\StakeClaims.sol`

- Contracts: StakeClaims
- Tags: delegation, staking, token
- Functions: lockStake, processStakeClaim, deleteStakeClaim, getNextStakeClaim, buildStakeClaimId, _buildStakeClaimId
- Modifiers: none
- Events: StakeClaimLocked, StakeClaimReleased, StakeClaimsReleased

## `packages\horizon\contracts\data-service\utilities\ProvisionManager.sol`

- Contracts: ProvisionManager
- Tags: delegation, staking, token
- Functions: _requireAuthorizedForProvision, __ProvisionManager_init, __ProvisionManager_init_unchained, _acceptProvisionParameters, _setDelegationRatio, _setProvisionTokensRange, _setVerifierCutRange, _setThawingPeriodRange, _requireValidProvision, _checkProvisionTokens, _checkProvisionTokens, _checkProvisionParameters, _checkProvisionParameters, _getDelegationRatio, _getProvisionTokensRange, _getThawingPeriodRange, _getVerifierCutRange, _getProvision, _checkValueInRange, _requireLTE
- Modifiers: none
- Events: ProvisionTokensRangeSet, DelegationRatioSet, VerifierCutRangeSet, ThawingPeriodRangeSet

## `packages\horizon\contracts\data-service\utilities\ProvisionManagerStorage.sol`

- Contracts: ProvisionManagerV1Storage
- Tags: delegation, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\horizon\contracts\mocks\AfterCollectionGasReportingMock.sol`

- Contracts: AfterCollectionGasReportingMock
- Tags: accounting, token
- Functions: isEligible, afterCollection
- Modifiers: none
- Events: none

## `packages\horizon\contracts\mocks\ControllerMock.sol`

- Contracts: ControllerMock
- Tags: governance, governor, registry
- Functions: setContractProxy, unsetContractProxy, updateController, setPartialPaused, setPaused, setPauseGuardian, getGovernor, getContractProxy, paused, partialPaused
- Modifiers: none
- Events: SetContractProxy

## `packages\horizon\contracts\mocks\CurationMock.sol`

- Contracts: CurationMock
- Tags: curation, token
- Functions: signal, isCurated, collect
- Modifiers: none
- Events: none

## `packages\horizon\contracts\mocks\MockGRTToken.sol`

- Contracts: MockGRTToken
- Tags: graphtoken, token
- Functions: burn, burnFrom, addMinter, removeMinter, renounceMinter, permit, increaseAllowance, decreaseAllowance, isMinter, mint
- Modifiers: none
- Events: none

## `packages\horizon\contracts\mocks\RewardsManagerMock.sol`

- Contracts: RewardsManagerMock
- Tags: rewards, rewardsmanager, token
- Functions: takeRewards, onSubgraphAllocationUpdate, onSubgraphSignalUpdate
- Modifiers: none
- Events: none

## `packages\horizon\contracts\payments\collectors\GraphTallyCollector.sol`

- Contracts: GraphTallyCollector
- Tags: token
- Functions: collect, collect, recoverRAVSigner, encodeRAV, _collect, _recoverRAVSigner, _encodeRAV, _requireAuthorizedSigner
- Modifiers: none
- Events: none

## `packages\horizon\contracts\payments\collectors\RecurringCollector.sol`

- Contracts: RecurringCollector
- Tags: delegation
- Functions: _getStorage, pauseGuardians, _checkPauseGuardian, initialize, pause, unpause, setPauseGuardian, collect, accept, _validateAndStoreAgreement, cancel, update, recoverRCASigner, recoverRCAUSigner, hashRCA, hashRCAU, getAgreement, getCollectionInfo, getMaxNextClaim, generateAgreementId, offer, _offerNew, _offerUpdate, cancel, getAgreementDetails
- Modifiers: onlyPauseGuardian
- Events: none

## `packages\horizon\contracts\payments\GraphPayments.sol`

- Contracts: GraphPayments
- Tags: delegation, escrow, graphtoken, staking, token
- Functions: initialize, collect
- Modifiers: none
- Events: none

## `packages\horizon\contracts\payments\PaymentsEscrow.sol`

- Contracts: PaymentsEscrow
- Tags: escrow, graphtoken, token
- Functions: initialize, deposit, depositTo, thaw, adjustThaw, cancelThaw, withdraw, collect, getBalance, _deposit
- Modifiers: notPaused
- Events: none

## `packages\horizon\contracts\staking\HorizonStaking.sol`

- Contracts: HorizonStaking
- Tags: delegation, economic, graphtoken, staking, token
- Functions: stake, stakeTo, stakeToProvision, unstake, withdraw, forceWithdraw, provision, addToProvision, thaw, deprovision, reprovision, setProvisionParameters, acceptProvisionParameters, delegate, addToDelegationPool, undelegate, withdrawDelegated, redelegate, setDelegationFeeCut, delegate, undelegate, withdrawDelegated, forceWithdrawDelegated, slash, provisionLocked
- Modifiers: onlyAuthorized, onlyAuthorizedOrVerifier
- Events: none

## `packages\horizon\contracts\staking\HorizonStakingBase.sol`

- Contracts: HorizonStakingBase
- Tags: delegation, staking, token
- Functions: getSubgraphService, getServiceProvider, getStake, getIdleStake, getDelegationPool, getDelegation, getDelegationFeeCut, getProvision, getTokensAvailable, getProviderTokensAvailable, getDelegatedTokensAvailable, getThawRequest, getThawRequestList, getThawedTokens, getMaxThawingPeriod, isAllowedLockedVerifier, isDelegationSlashingEnabled, _getIdleStake, _getDelegationPool, _getProviderTokensAvailable, _getNextProvisionThawRequest, _getNextDelegationThawRequest, _getThawRequestList, _getThawRequest, _getNextThawRequest
- Modifiers: none
- Events: none

## `packages\horizon\contracts\staking\HorizonStakingStorage.sol`

- Contracts: HorizonStakingV1Storage
- Tags: curation, delegation, slashing, staking, token, dispute
- Functions: none
- Modifiers: none
- Events: none

## `packages\horizon\contracts\staking\utilities\Managed.sol`

- Contracts: Managed
- Tags: governor, staking
- Functions: none
- Modifiers: notPaused, onlyGovernor
- Events: none

## `packages\horizon\contracts\utilities\GraphDirectory.sol`

- Contracts: GraphDirectory
- Tags: escrow, governance, graphtoken, rewards, rewardsmanager, staking, token
- Functions: _graphToken, _graphStaking, _graphPayments, _graphPaymentsEscrow, _graphController, _graphEpochManager, _graphRewardsManager, _graphTokenGateway, _graphProxyAdmin, _getContractFromController
- Modifiers: none
- Events: GraphDirectoryInitialized

## `packages\horizon\test\unit\data-service\DataService.t.sol`

- Contracts: DataServiceTest
- Tags: delegation, staking, token
- Functions: setUp, test_Constructor_WhenTheContractIsDeployedWithAValidController, test_DelegationRatio_WhenSettingTheDelegationRatio, test_DelegationRatio_WhenGettingTheDelegationRatio, test_ProvisionTokens_WhenSettingAValidRange, test_ProvisionTokens_RevertWhen_SettingAnInvalidRange, test_ProvisionTokens_WhenGettingTheRange, test_ProvisionTokens_WhenGettingTheRangeWithAnOverridenGetter, test_ProvisionTokens_WhenCheckingAValidProvision_WithThawing, test_ProvisionTokens_WhenCheckingAValidProvision, test_ProvisionTokens_WhenCheckingWithAnOverridenChecker, test_ProvisionTokens_RevertWhen_CheckingAnInvalidProvision, test_VerifierCut_WhenSettingAValidRange, test_VerifierCut_RevertWhen_SettingAnInvalidRange, test_VerifierCut_RevertWhen_SettingAnInvalidMax, test_VerifierCut_WhenGettingTheRange, test_VerifierCut_WhenGettingTheRangeWithAnOverridenGetter, test_VerifierCut_WhenCheckingAValidProvision, test_VerifierCut_WhenCheckingWithAnOverridenChecker, test_VerifierCut_RevertWhen_CheckingAnInvalidProvision, test_ThawingPeriod_WhenSettingAValidRange, test_ThawingPeriod_RevertWhen_SettingAnInvalidRange, test_ThawingPeriod_WhenGettingTheRange, test_ThawingPeriod_WhenGettingTheRangeWithAnOverridenGetter, test_ThawingPeriod_WhenCheckingAValidProvision
- Modifiers: givenProvisionParametersChanged
- Events: none

## `packages\horizon\test\unit\data-service\DataServiceUpgradeable.t.sol`

- Contracts: DataServiceUpgradeableTest
- Tags: delegation, governor, token
- Functions: test_WhenTheContractIsDeployed, _deployDataService
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\extensions\DataServiceFees.t.sol`

- Contracts: DataServiceFeesTest, StakeClaimsHarness
- Tags: staking, token
- Functions: test_Lock_RevertWhen_ZeroTokensAreLocked, setUp, test_Lock_WhenTheProvisionHasEnoughTokens, test_Lock_WhenTheProvisionHasJustEnoughTokens, test_Lock_RevertWhen_TheProvisionHasNotEnoughTokens, test_Release_WhenNIsValid, test_ProcessStakeClaim_RevertWhen_ClaimNotFound, test_Release_WhenNIsNotValid, _assertLockStake, _assertReleaseStake, processStakeClaim
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\extensions\DataServicePausable.t.sol`

- Contracts: DataServicePausableTest
- Tags: staking
- Functions: setUp, test_Pause_WhenTheProtocolIsNotPaused, test_Pause_RevertWhen_TheProtocolIsPaused, test_Pause_RevertWhen_TheCallerIsNotAPauseGuardian, test_Unpause_WhenTheProtocolIsPaused, test_Unpause_RevertWhen_TheProtocolIsNotPaused, test_Unpause_RevertWhen_TheCallerIsNotAPauseGuardian, test_SetPauseGuardian_WhenSettingAPauseGuardian, test_SetPauseGuardian_WhenRemovingAPauseGuardian, test_SetPauseGuardian_RevertWhen_AlreadyPauseGuardian, test_SetPauseGuardian_RevertWhen_AlreadyNotPauseGuardian, test_PausedProtectedFn_RevertWhen_TheProtocolIsPaused, test_PausedProtectedFn_WhenTheProtocolIsNotPaused, test_UnpausedProtectedFn_WhenTheProtocolIsPaused, test_UnpausedProtectedFn_RevertWhen_TheProtocolIsNotPaused, _assertPause, _assertUnpause, _assertSetPauseGuardian
- Modifiers: whenTheCallerIsAPauseGuardian
- Events: Paused, Unpaused

## `packages\horizon\test\unit\data-service\extensions\DataServicePausableUpgradeable.t.sol`

- Contracts: DataServicePausableUpgradeableTest
- Tags: delegation, token
- Functions: setUp, test_WhenTheContractIsDeployed, test_SetPauseGuardian, test_SetPauseGuardian_Remove, test_RevertWhen_SetPauseGuardian_NoChange_AlreadyFalse, test_RevertWhen_SetPauseGuardian_NoChange_AlreadyTrue, test_Pause, test_RevertWhen_Pause_NotGuardian, test_Unpause, test_RevertWhen_Unpause_NotGuardian, _deployDataService
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\implementations\DataServiceBase.sol`

- Contracts: DataServiceBase
- Tags: delegation, token
- Functions: register, acceptProvisionPendingParameters, startService, stopService, collect, slash, setDelegationRatio, setProvisionTokensRange, setVerifierCutRange, setThawingPeriodRange, checkProvisionTokens, checkProvisionParameters, acceptProvisionParameters
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\implementations\DataServiceImpPausable.sol`

- Contracts: DataServiceImpPausable
- Tags: delegation, token
- Functions: register, acceptProvisionPendingParameters, startService, stopService, collect, slash, setPauseGuardian, pausedProtectedFn, unpausedProtectedFn
- Modifiers: none
- Events: PausedProtectedFn, UnpausedProtectedFn

## `packages\horizon\test\unit\data-service\implementations\DataServiceOverride.sol`

- Contracts: DataServiceOverride
- Tags: token
- Functions: _getProvisionTokensRange, _getVerifierCutRange, _getThawingPeriodRange, _checkProvisionTokens, _checkProvisionParameters
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\libraries\ProvisionTracker.t.sol`

- Contracts: ProvisionTrackerWrapper, ProvisionTrackerTest
- Tags: delegation, staking, token
- Functions: lock, release, test_Lock_GivenTheProvisionHasSufficientAvailableTokens, test_Lock_RevertGiven_TheProvisionHasInsufficientAvailableTokens, test_Release_GivenTheProvisionHasSufficientLockedTokens, test_Release_RevertGiven_TheProvisionHasInsufficientLockedTokens
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\utilities\ProvisionManager.t.sol`

- Contracts: ProvisionManagerTest
- Tags: staking
- Functions: setUp, test_OnlyValidProvision, test_OnlyAuthorizedForProvision
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\escrow\collect.t.sol`

- Contracts: GraphEscrowCollectTest
- Tags: delegation, escrow, staking, token
- Functions: testCollect_Tokens, testCollect_Tokens_NoProvision, testCollect_RevertWhen_SenderHasInsufficientAmountInEscrow, testCollect_MultipleCollections, testCollect_EntireBalance, testCollect_CapsTokensThawingToZero_ResetsThawEndTimestamp, testCollect_CapsTokensThawingBelowBalance, testCollect_RevertWhen_InconsistentCollection
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\escrow\constructor.t.sol`

- Contracts: GraphEscrowConstructorTest
- Tags: escrow, governance, graphtoken, rewards, rewardsmanager, staking, token
- Functions: setUp, testConstructor_MaxWaitPeriodBoundary, testConstructor_RevertWhen_ThawingPeriodTooLong, testConstructor_ZeroThawingPeriod
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\escrow\deposit.t.sol`

- Contracts: GraphEscrowDepositTest
- Tags: escrow, staking, token
- Functions: testDeposit_Tokens, testDepositTo_Tokens, testDeposit_MultipleDeposits
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\escrow\getters.t.sol`

- Contracts: GraphEscrowGettersTest
- Tags: escrow, staking, token
- Functions: testGetBalance, testEscrowAccounts, testGetBalance_WhenThawing, testGetBalance_WhenCollectedOverThawing
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\escrow\GraphEscrow.t.sol`

- Contracts: GraphEscrowTest
- Tags: escrow, staking, token
- Functions: _approveEscrow, _thawEscrow, _cancelThawEscrow, _withdrawEscrow, _collectEscrow
- Modifiers: approveEscrow, useDeposit, depositAndThawTokens
- Events: none

## `packages\horizon\test\unit\escrow\isolation.t.sol`

- Contracts: GraphEscrowIsolationTest
- Tags: escrow, staking, token
- Functions: testIsolation_DifferentCollectorsSamePayerReceiver, testIsolation_DifferentReceiversSamePayerCollector, testIsolation_ThawOneTupleDoesNotAffectAnother, testIsolation_EscrowAccounts_NeverUsedAccount
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\escrow\paused.t.sol`

- Contracts: GraphEscrowPausedTest
- Tags: escrow, governor, token
- Functions: testPaused_RevertWhen_Deposit, testPaused_RevertWhen_DepositTo, testPaused_RevertWhen_ThawTokens, testPaused_RevertWhen_CancelThaw, testPaused_RevertWhen_AdjustThaw, testPaused_RevertWhen_WithdrawTokens, testPaused_RevertWhen_CollectTokens
- Modifiers: usePaused
- Events: none

## `packages\horizon\test\unit\escrow\thaw.t.sol`

- Contracts: GraphEscrowThawTest
- Tags: escrow, token
- Functions: testThaw_PartialBalanceThaw, testThaw_FullBalanceThaw, testThaw_Tokens_SuccesiveCalls, testThaw_Tokens_RevertWhen_AmountIsZero, testThaw_RevertWhen_InsufficientAmount, testThaw_CancelRequest, testThaw_CancelRequest_RevertWhen_NoThawing, testThaw_AlwaysResetsTimerOnSuccessiveCalls, testThaw_ResetsTimerOnIncrease, testAdjustThaw_CapsAtBalance, testAdjustThaw_ZeroAmountCancelsAll, testAdjustThaw_NoopWhenRequestedEqualsCurrentThawing, testAdjustThaw_PreservesTimerOnDecrease, testAdjustThaw_EvenIfTimerResetFalse_ProceedsWithNewThaw, testAdjustThaw_EvenIfTimerResetFalse_ProceedsWithDecrease, testAdjustThaw_EvenIfTimerResetFalse_SkipsIncreaseWhenTimerWouldReset, testAdjustThaw_EvenIfTimerResetFalse_ProceedsWhenTimerUnchanged, testAdjustThaw_EvenIfTimerResetFalse_CancelsThawing
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\escrow\withdraw.t.sol`

- Contracts: GraphEscrowWithdrawTest
- Tags: escrow, staking, token
- Functions: testWithdraw_Tokens, testWithdraw_RevertWhen_NotThawing, testWithdraw_RevertWhen_StillThawing, testWithdraw_RevertWhen_AtExactThawEndTimestamp, testWithdraw_SucceedsOneSecondAfterThawEnd, testWithdraw_BalanceAfterCollect
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\GraphBase.t.sol`

- Contracts: GraphBaseTest
- Tags: curation, escrow, governance, governor, graphtoken, rewards, rewardsmanager, staking, token
- Functions: setUp, deployProtocolContracts, setupProtocol, unpauseProtocol, createUser, mint, approve, _computeAddress, _deployContract
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\mocks\HorizonStakingMock.t.sol`

- Contracts: HorizonStakingMock
- Tags: staking, token
- Functions: setProvision, getProvision, isAuthorized, setIsAuthorized, getProviderTokensAvailable
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\graph-tally-collector\collect\collect.t.sol`

- Contracts: GraphTallyCollectTest
- Tags: token
- Functions: _getQueryFeeEncodedData, _getRav, testGraphTally_Collect, testGraphTally_Collect_Multiple, testGraphTally_Collect_RevertWhen_NoProvision, testGraphTally_Collect_RevertWhen_ProvisionEmpty, testGraphTally_Collect_PreventSignerAttack, testGraphTally_Collect_RevertWhen_CallerNotDataService, testGraphTally_Collect_RevertWhen_PayerMismatch, testGraphTally_Collect_RevertWhen_InconsistentRAVTokens, testGraphTally_Collect_RevertWhen_SignerNotAuthorized, testGraphTally_Collect_ThawingSigner, testGraphTally_Collect_RevertIf_SignerWasRevoked, testGraphTally_Collect_ThawingSignerCanceled, testGraphTally_CollectPartial, testGraphTally_CollectPartial_RevertWhen_AmountTooHigh, testGraphTally_Collect_SeparateAllocationTracking
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\graph-tally-collector\coverageGaps.t.sol`

- Contracts: GraphTallyCollectorCoverageGapsTest
- Tags: token
- Functions: test_RecoverRAVSigner, test_Authorizations_UnknownSigner, test_Authorizations_KnownSigner
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\graph-tally-collector\GraphTallyCollector.t.sol`

- Contracts: GraphTallyTest
- Tags: escrow, staking
- Functions: setUp, _getSignerProof, _authorizeSigner, _thawSigner, _cancelThawSigner, _revokeAuthorizedSigner, _collect, _collect, _collectRav
- Modifiers: useSigner
- Events: none

## `packages\horizon\test\unit\payments\GraphPayments.t.sol`

- Contracts: GraphPaymentsExtended, GraphPaymentsTest
- Tags: delegation, escrow, staking, token
- Functions: readController, _collect, testConstructor, testConstructor_RevertIf_InvalidProtocolPaymentCut, testInitialize, testCollect, testCollect_WithRestaking, testCollect_WithBeneficiary, testCollect_NoProvision, testCollect_RevertWhen_InvalidDataServiceCut, testCollect_WithZeroAmount, testCollect_RevertWhen_UnauthorizedCaller, testCollect_WithNoDelegation, testCollect_ViaMulticall
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\acceptUnsigned.t.sol`

- Contracts: RecurringCollectorAcceptUnsignedTest
- Tags: token
- Functions: _newApprover, _makeSimpleRCA, test_AcceptUnsigned, test_AcceptUnsigned_Revert_WhenNoOfferStored, test_AcceptUnsigned_Revert_WhenHashNotAuthorized, test_AcceptUnsigned_Revert_WhenWrongMagicValue, test_AcceptUnsigned_Revert_WhenNotDataService, test_AcceptUnsigned_Idempotent_WhenAlreadyAccepted, test_AcceptUnsigned_Revert_WhenDeadlineElapsed
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\acceptValidation.t.sol`

- Contracts: RecurringCollectorAcceptValidationTest
- Tags: token
- Functions: _makeValidRCA, _signAndAccept, test_Accept_Revert_WhenDataServiceZero, test_Accept_Revert_WhenServiceProviderZero, test_Accept_Revert_WhenEndsAtNotAfterDeadline, test_Accept_Revert_WhenCollectionWindowTooSmall, test_Accept_Revert_WhenMaxEqualsMin, test_Accept_Revert_WhenDurationTooShort, test_Accept_Revert_WhenCallerNotDataService, test_Accept_Revert_WhenMaxOngoingTokensOverflows, test_Accept_OK_WhenMaxOngoingTokensAtBoundary
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\afterCollection.t.sol`

- Contracts: RecurringCollectorAfterCollectionTest
- Tags: token
- Functions: _newApprover, _acceptUnsignedAgreement, test_BeforeCollection_CallbackInvoked, test_BeforeCollection_CollectionSucceedsWhenCallbackReverts, test_AfterCollection_CallbackInvoked, test_AfterCollection_NoCallbacks_WhenAgreementOwnerConditionUnset, test_AfterCollection_CollectionSucceedsWhenCallbackReverts, test_Collect_Revert_WhenInsufficientCallbackGas, test_Collect_Revert_WhenInsufficientCallbackGas_EligibilityPrecheck, test_AfterCollection_NotCalledForEOAPayer
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\agreementDetailsState.t.sol`

- Contracts: RecurringCollectorAgreementDetailsStateTest
- Tags: token
- Functions: _makeRca, _makeRcau, _acceptUnsigned, test_OfferNew_FreshOffer_State_Registered, test_OfferUpdate_FreshOffer_State_RegisteredUpdate, test_OfferNew_AfterAccept_State_RegisteredAccepted, test_OfferUpdate_AfterApply_State_RegisteredAcceptedUpdate, test_OfferNew_AfterProviderCancel_State_FullyDecorated, test_GetAgreementDetails_VersionNext_SettledIndependentOfActive, test_GetAgreementDetails_VersionCurrent_SettledIndependentOfPending
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\collect.t.sol`

- Contracts: RecurringCollectorCollectTest
- Tags: staking, token
- Functions: test_Collect_Revert_WhenInvalidData, test_Collect_Revert_WhenCallerNotDataService, test_Collect_Revert_WhenUnauthorizedDataService, test_Collect_Revert_WhenUnknownAgreement, test_Collect_Revert_WhenCanceledAgreementByServiceProvider, test_Collect_Revert_WhenCollectingTooSoon, test_Collect_OK_WhenCollectingPastMaxSeconds, test_Collect_OK_WhenCollectingTooMuch, test_Collect_OK, test_Collect_RevertWhen_ExceedsMaxSlippage, test_Collect_OK_WithMaxSlippageDisabled, test_Collect_Revert_WhenZeroTokensBypassesTemporalValidation
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\eligibility.t.sol`

- Contracts: RecurringCollectorEligibilityTest
- Tags: token
- Functions: _newApprover, _acceptUnsignedAgreement, test_Collect_OK_WhenEligible, test_Collect_Revert_WhenNotEligible, test_Collect_OK_WhenPayerDoesNotImplementEligibility, test_Collect_OK_WhenEOAPayer, test_Collect_OK_ZeroTokensSkipsEligibilityCheck, test_Collect_OK_WhenPayerReturnsMalformedData
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\getAgreementDetails.t.sol`

- Contracts: RecurringCollectorGetAgreementDetailsTest
- Tags: token
- Functions: test_GetAgreementDetails_Accepted, test_GetAgreementDetails_StoredOffer, test_GetAgreementDetails_Unknown, test_GetAgreementDetails_Canceled, test_GetAgreementDetails_CanceledByServiceProvider_Flags, test_GetAgreementDetails_CanceledByPayer_Flags, test_GetAgreementDetails_Accepted_ElapsedSetsSettled
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\getMaxNextClaim.t.sol`

- Contracts: RecurringCollectorGetMaxNextClaimTest
- Tags: token
- Functions: test_GetMaxNextClaim_NotAccepted, test_GetMaxNextClaim_StoredOffer_BeforeAccept, test_GetMaxNextClaim_StoredOffer_ExpiredDeadline, test_GetMaxNextClaim_StoredUpdate_PendingScope, test_GetMaxNextClaim_MaxOfActiveAndPending, test_GetMaxNextClaim_CanceledByServiceProvider, test_GetMaxNextClaim_Accepted_NeverCollected, test_GetMaxNextClaim_Accepted_AfterCollection, test_GetMaxNextClaim_CanceledByPayer_SameBlock, test_GetMaxNextClaim_CanceledByPayer_WithWindow, test_GetMaxNextClaim_CanceledByPayer_AfterCollection, test_GetMaxNextClaim_Accepted_PastEndsAt, test_GetMaxNextClaim_Accepted_PastEndsAt_NeverCollected, test_GetMaxNextClaim_MaxSecondsPerCollectionCaps, test_GetMaxNextClaim_WindowSmallerThanMaxSecondsPerCollection, test_GetMaxNextClaim_PreAcceptanceActiveAtExactDeadline_StillCounts, test_GetMaxNextClaim_PendingAtExactDeadline_StillCounts, test_GetMaxNextClaim_PendingIgnored_AfterDeadline, test_GetMaxNextClaim_PostUpdate_PendingDoesNotDoubleCountActive, test_GetMaxNextClaim_PendingScope_CoversPostUpdateCollection, test_GetMaxNextClaim_PendingScope_CoversPostUpdateCollection_AfterPriorCollect, testFuzz_GetMaxNextClaim_PendingScope_CoversPostUpdateCollection
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\hashRoundTrip.t.sol`

- Contracts: RecurringCollectorHashRoundTripTest
- Tags: token
- Functions: setUp, _makeRCA, _offerRCA, _offerAndAcceptRCA, _makeUpdate, _verifyOfferRoundTrip, test_HashRoundTrip_RCA_Pending, test_HashRoundTrip_RCA_PersistsAfterAccept, test_HashRoundTrip_RCAU_Pending, test_HashRoundTrip_RCAU_PersistsAfterUpdate, test_HashRoundTrip_CancelPending_ActiveStays, test_HashRoundTrip_RCAU_PreAcceptOverwrite
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\mixedPath.t.sol`

- Contracts: RecurringCollectorMixedPathTest
- Tags: token
- Functions: test_MixedPath_UnsignedAccept_UnsignedUpdate_OK, test_MixedPath_ECDSAAccept_UnsignedUpdate_RevertsForEOA, test_MixedPath_ECDSAAccept_ECDSAUpdate_OK, test_MixedPath_OfferNew_PreservesPendingRcau
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\MockAgreementOwner.t.sol`

- Contracts: MockAgreementOwner
- Tags: token
- Functions: setShouldRevert, setShouldRevertOnBeforeCollection, beforeCollection, setShouldRevertOnCollected, afterCollection, setProviderIneligible, isEligible, supportsInterface
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\offerStorageLifecycle.t.sol`

- Contracts: RecurringCollectorOfferStorageLifecycleTest
- Tags: token
- Functions: _makeRca, _makeRcau, test_OfferNew_StoresEntryAtHash_EmitsEvent, test_OfferNew_Idempotent_WhenResubmittedSameHash, test_OfferNew_EntryPersistsAcrossAccept, test_OfferNew_PostAccept_DifferentHash_Reverts, test_Cancel_ScopePending_OnAcceptedActiveHash_NoOp, test_Cancel_ScopePending_OnPostUpdateActiveHash_NoOp, test_Update_DeletesPriorActiveOffer_PromotesRcauToCurrent, test_OfferUpdate_ReplacesPriorPending_DeletesReplaced, test_CancelPreAcceptanceRca_PreservesPendingRcau, test_CancelPreAcceptance_EitherOrder, test_CancelPreAcceptanceRca_NoPending_OnlyDeletesRca, test_OfferTypeConstants_NoneIsZero_OthersNonZero, test_Offer_Revert_WhenOfferTypeIsNone, test_OfferUpdate_PostUpdate_PreservesActiveRcauBytes, test_OfferUpdate_PostUpdate_BothVersionsRetrievable, test_OfferUpdate_Revert_OnCancelledAgreement, test_Cancel_ClearsStalePendingRcau, test_Cancel_PreservesActiveRcauBytes
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\pause.t.sol`

- Contracts: RecurringCollectorPauseTest
- Tags: governor
- Functions: _governor, _setGuardian, _pause, test_SetPauseGuardian_OK, test_SetPauseGuardian_Remove, test_SetPauseGuardian_Revert_WhenNotGovernor, test_SetPauseGuardian_Revert_WhenNoChange, test_SetPauseGuardian_Revert_WhenNoChange_AlreadySet, test_Pause_OK, test_Pause_Revert_WhenNotGuardian, test_Unpause_OK, test_Unpause_Revert_WhenNotGuardian, test_Accept_Revert_WhenPaused, test_Collect_Revert_WhenPaused, test_Cancel_Revert_WhenPaused, test_Update_Revert_WhenPaused, test_Offer_Revert_WhenPaused, test_OfferBeforePause_AcceptAfterUnpause
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\PaymentsEscrowMock.t.sol`

- Contracts: PaymentsEscrowMock
- Tags: escrow
- Functions: initialize, collect, deposit, depositTo, thaw, adjustThaw, cancelThaw, withdraw, getBalance, escrowAccounts, MAX_WAIT_PERIOD, WITHDRAW_ESCROW_THAWING_PERIOD
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\returndataBomb.t.sol`

- Contracts: HugeReturnPayer, RecurringCollectorReturndataBombTest
- Tags: token
- Functions: setReturnBytes, supportsInterface, beforeCollection, afterCollection, test_Collect_BoundsReturndataCopy_WhenPayerReturnsHuge
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\shared.t.sol`

- Contracts: RecurringCollectorSharedTest
- Tags: escrow, staking
- Functions: setUp, _sensibleAuthorizeAndAccept, _authorizeAndAccept, _accept, _setupValidProvision, _cancel, _expectCollectCallAndEmit, _generateValidCollection, _generateCollectParams, _generateCollectData, _fuzzyCancelAgreementBy, _paymentType
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\updateUnsigned.t.sol`

- Contracts: RecurringCollectorUpdateUnsignedTest
- Tags: token
- Functions: _newApprover, _acceptUnsigned, _makeSimpleRCA, _makeSimpleRCAU, test_UpdateUnsigned, test_UpdateUnsigned_Revert_WhenHashNotAuthorized, test_UpdateUnsigned_Revert_WhenWrongMagicValue, test_UpdateUnsigned_Revert_WhenNotDataService, test_UpdateUnsigned_Revert_WhenNotAccepted, test_UpdateUnsigned_Revert_WhenInvalidNonce, test_UpdateUnsigned_Revert_WhenNoOfferStored, test_UpdateUnsigned_Revert_WhenDeadlineElapsed
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\upgradeScenario.t.sol`

- Contracts: RecurringCollectorUpgradeScenarioTest
- Tags: escrow, governor, staking
- Functions: setUp, test_Upgrade_InitializeRevertsOnSecondCall, test_Upgrade_StatePreservedAfterUpgrade, test_Upgrade_RevertWhen_NotProxyAdminOwner
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\shared\horizon-staking\HorizonStakingShared.t.sol`

- Contracts: HorizonStakingSharedTest
- Tags: delegation, staking, token
- Functions: _useProvision, _createProvision, _stake, _stakeTo, _stakeToProvision, _unstake, _withdraw, _provision, _provisionLocked, _provision, _addToProvision, _thaw, _deprovision, _reprovision, _setProvisionParameters, _acceptProvisionParameters, _setOperator, _setOperatorLocked, _setOperator, _delegate, _delegate, _delegate, _undelegate, _undelegate, _undelegate
- Modifiers: useIndexer, useOperator, useStake, useProvision, useProvisionDataService, useDelegationFeeCut
- Events: Transfer

## `packages\horizon\test\unit\shared\payments-escrow\PaymentsEscrowShared.t.sol`

- Contracts: PaymentsEscrowSharedTest
- Tags: escrow, token
- Functions: _depositTokens, _depositToTokens
- Modifiers: useGateway
- Events: none

## `packages\horizon\test\unit\staking\coverageGaps.t.sol`

- Contracts: HorizonStakingCoverageGapsTest
- Tags: delegation, staking, token
- Functions: test_GetSubgraphService, test_GetIdleStake_NoStake, test_GetIdleStake_WithStake, test_GetDelegation_NoDelegation, test_GetDelegation_WithDelegation, test_GetThawedTokens_ZeroRequests_Delegation
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\delegation\addToPool.t.sol`

- Contracts: HorizonStakingDelegationAddToPoolTest
- Tags: delegation, slashing, staking, token
- Functions: test_Delegation_AddToPool_Verifier, test_Delegation_AddToPool_Payments, test_Delegation_AddToPool_RevertWhen_ZeroTokens, test_Delegation_AddToPool_RevertWhen_PoolHasNoShares, test_Delegation_AddToPool_RevertWhen_NoProvision, test_Delegation_AddToPool_WhenInvalidPool, test_Delegation_AddToPool_WhenInvalidPool_RevertWhen_PoolHasNoShares
- Modifiers: useValidDelegationAmount, useValidAddToPoolAmount
- Events: none

## `packages\horizon\test\unit\staking\delegation\delegate.t.sol`

- Contracts: HorizonStakingDelegateTest
- Tags: delegation, slashing, staking, token
- Functions: testDelegate_Tokens, testDelegate_Tokens_WhenThawing, testDelegate_Tokens_WhenAllThawing, testDelegate_RevertWhen_ZeroTokens, testDelegate_RevertWhen_UnderMinDelegation, testDelegate_LegacySubgraphService, testDelegate_RevertWhen_InvalidPool, testDelegate_RevertWhen_ThawingShares_InvalidPool, testDelegate_AfterRecoveringPool, testDelegate_RevertWhen_ProvisionNotCreated
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\delegation\forceWithdrawDelegated.t.sol`

- Contracts: HorizonStakingForceWithdrawDelegatedTest
- Tags: delegation, staking, token
- Functions: _setLegacyDelegation, _forceWithdrawDelegated, testForceWithdrawDelegated_Tokens, testForceWithdrawDelegated_CalledByDelegator, testForceWithdrawDelegated_RevertWhen_NoTokens
- Modifiers: useDelegator
- Events: none

## `packages\horizon\test\unit\staking\delegation\legacyWithdraw.t.sol`

- Contracts: HorizonStakingLegacyWithdrawDelegationTest
- Tags: delegation, staking, token
- Functions: _setLegacyDelegation, _legacyWithdrawDelegated, testWithdraw_Legacy, testWithdraw_Legacy_RevertWhen_NoTokens
- Modifiers: useDelegator
- Events: none

## `packages\horizon\test\unit\staking\delegation\redelegate.t.sol`

- Contracts: HorizonStakingWithdrawDelegationTest
- Tags: delegation, staking, token
- Functions: _setupNewIndexer, _setupNewIndexerAndVerifier, testRedelegate_MoveToNewServiceProvider, testRedelegate_MoveToNewServiceProviderAndNewVerifier, testRedelegate_RevertWhen_VerifierZeroAddress, testRedelegate_RevertWhen_ServiceProviderZeroAddress, testRedelegate_MoveZeroTokensToNewServiceProviderAndVerifier
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\delegation\undelegate.t.sol`

- Contracts: HorizonStakingUndelegateTest
- Tags: delegation, staking, token
- Functions: testUndelegate_Tokens, testMultipleUndelegate_Tokens, testUndelegate_RevertWhen_InsuficientTokens, testUndelegate_RevertWhen_TooManyUndelegations, testUndelegate_RevertWhen_ZeroShares, testUndelegate_RevertWhen_OverShares, testUndelegate_LegacySubgraphService, testUndelegate_RevertWhen_InvalidPool, testUndelegate_AfterRecoveringPool, testUndelegate_ThawingShares_AfterRecoveringPool
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\delegation\withdraw.t.sol`

- Contracts: HorizonStakingWithdrawDelegationTest
- Tags: delegation, slashing, staking, token
- Functions: testWithdrawDelegation_Tokens, testWithdrawDelegation_RevertWhen_NotThawing, testWithdrawDelegation_ZeroTokens, testWithdrawDelegation_LegacySubgraphService, testWithdrawDelegation_RevertWhen_InvalidPool, testWithdrawDelegation_AfterRecoveringPool, testWithdrawDelegation_GetThawedTokens
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\governance\governance.t.sol`

- Contracts: HorizonStakingGovernanceTest
- Tags: delegation, governance, governor, slashing, staking
- Functions: testGovernance_SetAllowedLockedVerifier, testGovernance_RevertWhen_SetAllowedLockedVerifier_NotGovernor, testGovernance_SetDelgationSlashingEnabled, testGovernance_SetDelgationSlashing_NotGovernor, testGovernance__SetMaxThawingPeriod, testGovernance__SetMaxThawingPeriod_NotGovernor
- Modifiers: useGovernor
- Events: none

## `packages\horizon\test\unit\staking\HorizonStaking.t.sol`

- Contracts: HorizonStakingTest
- Tags: delegation, governor, slashing, staking, token
- Functions: none
- Modifiers: usePausedStaking, useThawAndDeprovision, useDelegation, useLockedVerifier, useDelegationSlashing, useUndelegate
- Events: none

## `packages\horizon\test\unit\staking\legacy\isAllocation.t.sol`

- Contracts: HorizonStakingIsAllocationTest
- Tags: rewards, staking, token
- Functions: test_IsAllocation_ReturnsFalse_WhenAllocationDoesNotExist, test_IsAllocation_ReturnsTrue_WhenActiveAllocationExists, test_IsAllocation_ReturnsTrue_WhenClosedAllocationExists, test_IsAllocation_ReturnsFalse_WhenIndexerIsZeroAddress, _setLegacyAllocationInStaking
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\operator\locked.t.sol`

- Contracts: HorizonStakingOperatorLockedTest
- Tags: staking
- Functions: testOperatorLocked_Set, testOperatorLocked_RevertWhen_VerifierNotAllowed, testOperatorLocked_RevertWhen_CallerIsServiceProvider, testOperatorLocked_SetLegacySubgraphService
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\operator\operator.t.sol`

- Contracts: HorizonStakingOperatorTest
- Tags: staking
- Functions: testOperator_SetOperator, testOperator_RevertWhen_CallerIsServiceProvider, testOperator_RemoveOperator
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\provision\deprovision.t.sol`

- Contracts: HorizonStakingDeprovisionTest
- Tags: staking, token
- Functions: testDeprovision_AllRequests, testDeprovision_ThawedRequests, testDeprovision_OperatorMovingTokens, testDeprovision_RevertWhen_OperatorNotAuthorized, testDeprovision_RevertWhen_NoThawingTokens, testDeprovision_StillThawing, testDeprovision_AfterProvisionFullySlashed, testDeprovision_AfterResetingThawingPool
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\provision\locked.t.sol`

- Contracts: HorizonStakingProvisionLockedTest
- Tags: governor, staking, token
- Functions: testProvisionLocked_Create, testProvisionLocked_RevertWhen_VerifierNotAllowed, testProvisionLocked_RevertWhen_OperatorNotAllowed
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\provision\parameters.t.sol`

- Contracts: HorizonStakingProvisionParametersTest
- Tags: governor, staking, token
- Functions: test_ProvisionParametersSet, test_ProvisionParametersSet_RevertWhen_ProvisionNotExists, test_ProvisionParametersSet_RevertWhen_CallerNotAuthorized, test_ProvisionParametersSet_RevertWhen_ProtocolPaused, test_ProvisionParametersSet_MaxMaxThawingPeriodChanged, test_ProvisionParametersAccept, test_ProvisionParametersAccept_SameParameters, test_ProvisionParameters_RevertIf_InvalidMaxVerifierCut, test_ProvisionParameters_RevertIf_InvalidThawingPeriod, test_ProvisionParametersAccept_RevertWhen_ProvisionNotExists, test_ProvisionParametersAccept_RevertWhen_MaxThawingPeriodReduced
- Modifiers: useValidParameters
- Events: none

## `packages\horizon\test\unit\staking\provision\provision.t.sol`

- Contracts: HorizonStakingProvisionTest
- Tags: staking, token
- Functions: testProvision_Create, testProvision_RevertWhen_ZeroTokens, testProvision_RevertWhen_MaxVerifierCutTooHigh, testProvision_RevertWhen_ThawingPeriodTooHigh, testProvision_RevertWhen_ThereIsNoIdleStake, testProvision_RevertWhen_AlreadyExists, testProvision_RevertWhen_OperatorNotAuthorized, testProvision_AddTokensToProvision, testProvision_OperatorAddTokensToProvision, testProvision_AddTokensToProvision_RevertWhen_NotAuthorized, testProvision_StakeToProvision, testProvision_Operator_StakeToProvision, testProvision_Verifier_StakeToProvision, testProvision_StakeToProvision_RevertWhen_NotAuthorized
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\provision\reprovision.t.sol`

- Contracts: HorizonStakingReprovisionTest
- Tags: staking, token
- Functions: testReprovision_MovingTokens, testReprovision_OperatorMovingTokens, testReprovision_RevertWhen_OperatorNotAuthorizedForNewDataService, testReprovision_RevertWhen_NoThawingTokens
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\provision\thaw.t.sol`

- Contracts: HorizonStakingThawTest
- Tags: staking, token
- Functions: testThaw_Tokens, testThaw_MultipleRequests, testThaw_OperatorCanStartThawing, testThaw_RevertWhen_OperatorNotAuthorized, testThaw_RevertWhen_InsufficientTokensAvailable, testThaw_RevertWhen_OverMaxThawRequests, testThaw_RevertWhen_ThawingZeroTokens, testThaw_RevertWhen_ProvisionFullySlashed, testThaw_AfterResetingThawingPool, testThaw_GetThawedTokens, testThaw_GetThawedTokens_AfterProvisionFullySlashed, testThaw_GetThawedTokens_AfterRecoveringProvision
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\serviceProvider\serviceProvider.t.sol`

- Contracts: HorizonStakingServiceProviderTest
- Tags: delegation, staking, token
- Functions: testServiceProvider_GetProvider, testServiceProvider_SetDelegationFeeCut, testServiceProvider_GetProvision, testServiceProvider_GetTokensAvailable, testServiceProvider_GetTokensAvailable_WithDelegation, testServiceProvider_GetProviderTokensAvailable, testServiceProvider_RevertIf_InvalidDelegationFeeCut
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\slash\slash.t.sol`

- Contracts: HorizonStakingSlashTest
- Tags: delegation, slashing, staking, token
- Functions: testSlash_Tokens, testSlash_Tokens_RevertWhen_TooManyVerifierTokens, testSlash_DelegationDisabled_SlashingOverProviderTokens, testSlash_DelegationEnabled_SlashingOverProviderTokens, testSlash_OverProvisionSize, testSlash_RevertWhen_NoProvision, testSlash_Everything, testSlash_Everything_WithUndelegation, testSlash_RoundDown_TokensThawing_Provision, testSlash_RoundDown_TokensThawing_Delegation
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\stake\forceWithdraw.t.sol`

- Contracts: HorizonStakingForceWithdrawTest
- Tags: staking, token
- Functions: _forceWithdraw, testForceWithdraw_Tokens, testForceWithdraw_CalledByServiceProvider, testForceWithdraw_RevertWhen_ZeroTokens
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\stake\stake.t.sol`

- Contracts: HorizonStakingStakeTest
- Tags: staking, token
- Functions: testStake_Tokens, testStake_RevertWhen_ZeroTokens, testStakeTo_Tokens, testStakeTo_RevertWhen_ZeroTokens
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\stake\unstake.t.sol`

- Contracts: HorizonStakingUnstakeTest
- Tags: staking, token
- Functions: testUnstake_Tokens, testUnstake_RevertWhen_ZeroTokens, testUnstake_RevertWhen_NoIdleStake, testUnstake_RevertWhen_NotDeprovision
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\staking\stake\withdraw.t.sol`

- Contracts: HorizonStakingWithdrawTest
- Tags: staking, token
- Functions: testWithdraw_Tokens, testWithdraw_RevertWhen_ZeroTokens
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\utilities\GraphDirectory.t.sol`

- Contracts: GraphDirectoryTest
- Tags: escrow, graphtoken, rewards, rewardsmanager, staking, token
- Functions: test_WhenTheContractIsDeployedWithAValidController, test_RevertWhen_TheContractIsDeployedWithAnInvalidController, test_RevertWhen_TheContractIsDeployedWithTheZeroAddressAsTheInvalidController, test_WhenTheContractGettersAreCalled, test_RevertWhen_AnInvalidContractGetterIsCalled, _deployImplementation, _getContractFromController
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\utilities\GraphDirectoryImplementation.sol`

- Contracts: GraphDirectoryImplementation
- Tags: escrow, governance, graphtoken, rewards, rewardsmanager, staking, token
- Functions: getContractFromController, graphToken, graphStaking, graphPayments, graphPaymentsEscrow, graphController, graphEpochManager, graphRewardsManager, graphTokenGateway, graphProxyAdmin
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\utils\Constants.sol`

- Contracts: Constants
- Tags: delegation, escrow, rewards, staking, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\arbitrum\IArbToken.sol`

- Contracts: IArbToken
- Tags: bridge, permission, token
- Functions: bridgeMint, bridgeBurn, l1Address
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\arbitrum\IBridge.sol`

- Contracts: IBridge
- Tags: bridge, permission
- Functions: deliverMessageToInbox, executeCall, setInbox, setOutbox, activeOutbox, allowedInboxes, allowedOutboxes, inboxAccs, messageCount
- Modifiers: none
- Events: MessageDelivered, BridgeCallTriggered, InboxToggle, OutboxToggle

## `packages\interfaces\contracts\contracts\arbitrum\IInbox.sol`

- Contracts: IInbox
- Tags: bridge, permission
- Functions: sendL2Message, sendUnsignedTransaction, sendContractTransaction, sendL1FundedUnsignedTransaction, sendL1FundedContractTransaction, createRetryableTicket, depositEth, bridge, pauseCreateRetryables, unpauseCreateRetryables, startRewriteAddress, stopRewriteAddress
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\arbitrum\IMessageProvider.sol`

- Contracts: IMessageProvider
- Tags: bridge, permission
- Functions: none
- Modifiers: none
- Events: InboxMessageDelivered, InboxMessageDeliveredFromOrigin

## `packages\interfaces\contracts\contracts\arbitrum\IOutbox.sol`

- Contracts: IOutbox
- Tags: bridge, permission
- Functions: l2ToL1Sender, l2ToL1Block, l2ToL1EthBlock, l2ToL1Timestamp, l2ToL1BatchNum, l2ToL1OutputId, processOutgoingMessages, outboxEntryExists
- Modifiers: none
- Events: OutboxEntryCreated, OutBoxTransactionExecuted

## `packages\interfaces\contracts\contracts\arbitrum\ITokenGateway.sol`

- Contracts: ITokenGateway
- Tags: bridge, cross-chain, permission, token
- Functions: outboundTransfer, finalizeInboundTransfer, calculateL2TokenAddress
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\curation\ICuration.sol`

- Contracts: ICuration
- Tags: curation, token
- Functions: setDefaultReserveRatio, setMinimumCurationDeposit, setCurationTaxPercentage, setCurationTokenMaster, mint, burn, collect, isCurated, getCuratorSignal, getCurationPoolSignal, getCurationPoolTokens, tokensToSignal, signalToTokens, curationTaxPercentage
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\curation\IGraphCurationToken.sol`

- Contracts: IGraphCurationToken
- Tags: curation, token
- Functions: initialize, burnFrom, mint
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\discovery\erc1056\IEthereumDIDRegistry.sol`

- Contracts: IEthereumDIDRegistry
- Tags: registry
- Functions: identityOwner, setAttribute
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\discovery\IGNS.sol`

- Contracts: IGNS
- Tags: curation, token
- Functions: approveAll, setOwnerTaxPercentage, setDefaultName, updateSubgraphMetadata, publishNewSubgraph, publishNewVersion, deprecateSubgraph, mintSignal, burnSignal, transferSignal, withdraw, ownerOf, subgraphSignal, subgraphTokens, tokensToNSignal, nSignalToTokens, vSignalToNSignal, nSignalToVSignal, getCuratorSignal, isPublished, isLegacySubgraph, getLegacySubgraphKey
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\discovery\IServiceRegistry.sol`

- Contracts: IServiceRegistry
- Tags: registry
- Functions: register, registerFor, unregister, unregisterFor, isRegistered
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\discovery\ISubgraphNFT.sol`

- Contracts: ISubgraphNFT
- Tags: token
- Functions: setMinter, setTokenDescriptor, setBaseURI, mint, burn, setSubgraphMetadata, tokenURI
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\discovery\ISubgraphNFTDescriptor.sol`

- Contracts: ISubgraphNFTDescriptor
- Tags: token
- Functions: tokenURI
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\disputes\IDisputeManager.sol`

- Contracts: IDisputeManager
- Tags: disputemanager, disputes, slashing, token, dispute
- Functions: setArbitrator, setMinimumDeposit, setFishermanRewardPercentage, setSlashingPercentage, isDisputeCreated, encodeHashReceipt, areConflictingAttestations, getAttestationIndexer, createQueryDispute, createQueryDisputeConflict, createIndexingDispute, acceptDispute, rejectDispute, drawDispute
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\gateway\ICallhookReceiver.sol`

- Contracts: ICallhookReceiver
- Tags: bridge, governor, graphtoken, token
- Functions: onTokenTransfer
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\governance\IController.sol`

- Contracts: IController
- Tags: governance, governor, registry
- Functions: getGovernor, setContractProxy, unsetContractProxy, updateController, getContractProxy, setPartialPaused, setPaused, setPauseGuardian, paused, partialPaused
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\governance\IGoverned.sol`

- Contracts: IGoverned
- Tags: governance, governor
- Functions: governor, pendingGovernor, transferOwnership, acceptOwnership
- Modifiers: none
- Events: NewPendingOwnership, NewOwnership

## `packages\interfaces\contracts\contracts\governance\IManaged.sol`

- Contracts: IManaged
- Tags: governance, registry
- Functions: setController, syncAllContracts, controller
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\l2\curation\IL2Curation.sol`

- Contracts: IL2Curation
- Tags: accounting, curation, token
- Functions: setSubgraphService, mintTaxFree, tokensToSignalNoTax, tokensToSignalToTokensNoTax
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\l2\discovery\IL2GNS.sol`

- Contracts: IL2GNS
- Tags: bridge, l1gns, token
- Functions: finishSubgraphTransferFromL1, getAliasedL2SubgraphID, getUnaliasedL1SubgraphID
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\l2\gateway\IL2GraphTokenGateway.sol`

- Contracts: IL2GraphTokenGateway
- Tags: graphtoken, token
- Functions: initialize, setL2Router, setL1TokenAddress, setL1CounterpartAddress, outboundTransfer, finalizeInboundTransfer, outboundTransfer, calculateL2TokenAddress, getOutboundCalldata
- Modifiers: none
- Events: DepositFinalized, WithdrawalInitiated, L2RouterSet, L1TokenAddressSet, L1CounterpartAddressSet

## `packages\interfaces\contracts\contracts\l2\staking\IL2Staking.sol`

- Contracts: IL2Staking
- Tags: delegation, staking
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\l2\staking\IL2StakingBase.sol`

- Contracts: IL2StakingBase
- Tags: delegation, staking
- Functions: none
- Modifiers: none
- Events: TransferredDelegationReturnedToDelegator

## `packages\interfaces\contracts\contracts\l2\staking\IL2StakingTypes.sol`

- Contracts: IL2StakingTypes
- Tags: bridge, delegation, staking
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\l2\token\IL2GraphToken.sol`

- Contracts: IL2GraphToken
- Tags: bridge, graphtoken, token
- Functions: gateway, l1Address, initialize, setGateway, setL1Address, bridgeMint, bridgeBurn
- Modifiers: none
- Events: BridgeMinted, BridgeBurned, GatewaySet, L1AddressSet

## `packages\interfaces\contracts\contracts\rewards\ILegacyRewardsManager.sol`

- Contracts: ILegacyRewardsManager
- Tags: rewards, rewardsmanager
- Functions: getRewards
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\rewards\IRewardsIssuer.sol`

- Contracts: IRewardsIssuer
- Tags: rewards, token
- Functions: getAllocationData, getSubgraphAllocatedTokens
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\rewards\IRewardsManager.sol`

- Contracts: IRewardsManager
- Tags: rewards, rewardsmanager, token
- Functions: setMinimumSubgraphSignal, setSubgraphService, setReclaimAddress, setDefaultReclaimAddress, setRevertOnIneligible, getRevertOnIneligible, setSubgraphAvailabilityOracle, setDenied, isDenied, subgraphService, getReclaimAddress, getDefaultReclaimAddress, getAllocatedIssuancePerBlock, getRawIssuancePerBlock, getNewRewardsPerSignal, getAccRewardsPerSignal, getAccRewardsForSubgraph, getAccRewardsPerAllocatedToken, getRewards, calcRewards, updateAccRewardsPerSignal, takeRewards, reclaimRewards, onSubgraphSignalUpdate, onSubgraphAllocationUpdate
- Modifiers: none
- Events: HorizonRewardsAssigned, RewardsDenied, RewardsDenylistUpdated, SubgraphServiceSet, RewardsDeniedDueToEligibility, ReclaimAddressSet, DefaultReclaimAddressSet, RewardsReclaimed

## `packages\interfaces\contracts\contracts\rewards\IRewardsManagerDeprecated.sol`

- Contracts: IRewardsManagerDeprecated
- Tags: rewards, rewardsmanager
- Functions: issuancePerBlock, setIssuancePerBlock
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\rewards\RewardsCondition.sol`

- Contracts: RewardsCondition
- Tags: curation, rewards, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\staking\IL1GraphTokenLockTransferTool.sol`

- Contracts: IL1GraphTokenLockTransferTool
- Tags: delegation, graphtoken, l1staking, staking, token
- Functions: pullETH, l2WalletAddress
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\staking\IL1Staking.sol`

- Contracts: IL1Staking
- Tags: delegation, l1staking, staking
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\staking\IL1StakingBase.sol`

- Contracts: IL1StakingBase
- Tags: delegation, governor, graphtoken, l1staking, staking, token
- Functions: setL1GraphTokenLockTransferTool, transferStakeToL2, transferLockedStakeToL2, transferDelegationToL2, transferLockedDelegationToL2, unlockDelegationToTransferredIndexer
- Modifiers: none
- Events: IndexerStakeTransferredToL2, DelegationTransferredToL2, L1GraphTokenLockTransferToolSet, StakeDelegatedUnlockedDueToL2Transfer

## `packages\interfaces\contracts\contracts\staking\IStaking.sol`

- Contracts: IStaking
- Tags: governance, staking
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\staking\IStakingBase.sol`

- Contracts: IStakingBase
- Tags: curation, delegation, staking, token
- Functions: initialize, setExtensionImpl, setCounterpartStakingAddress, setMinimumIndexerStake, setThawingPeriod, setCurationPercentage, setProtocolPercentage, setMaxAllocationEpochs, setRebateParameters, setOperator, stake, stakeTo, unstake, withdraw, setRewardsDestination, setDelegationParameters, allocate, allocateFrom, closeAllocation, collect, isOperator, hasStake, getIndexerStakedTokens, getIndexerCapacity, getAllocation
- Modifiers: none
- Events: StakeDeposited, StakeLocked, StakeWithdrawn, AllocationCreated, AllocationClosed, RebateCollected, DelegationParametersUpdated, SetOperator, SetRewardsDestination, ExtensionImplementationSet

## `packages\interfaces\contracts\contracts\staking\IStakingData.sol`

- Contracts: IStakingData
- Tags: delegation, rewards, staking, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\staking\IStakingExtension.sol`

- Contracts: IStakingExtension
- Tags: delegation, staking, token
- Functions: setDelegationRatio, setDelegationUnbondingPeriod, setDelegationTaxPercentage, setSlasher, delegate, undelegate, withdrawDelegated, slash, getDelegation, isDelegator, getWithdraweableDelegatedTokens, delegationRatio, delegationUnbondingPeriod, delegationTaxPercentage, delegationPools, operatorAuth, rewardsDestination, subgraphAllocations, slashers, minimumIndexerStake, thawingPeriod, curationPercentage, protocolPercentage, maxAllocationEpochs, alphaNumerator
- Modifiers: none
- Events: StakeDelegated, StakeDelegatedLocked, StakeDelegatedWithdrawn, StakeSlashed, SlasherUpdate

## `packages\interfaces\contracts\contracts\staking\libs\IStakes.sol`

- Contracts: IStakes
- Tags: staking, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\token\IGraphToken.sol`

- Contracts: IGraphToken
- Tags: graphtoken, permission, token
- Functions: burn, burnFrom, mint, addMinter, removeMinter, renounceMinter, isMinter, permit, increaseAllowance, decreaseAllowance
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\upgrades\IGraphProxyAdmin.sol`

- Contracts: IGraphProxyAdmin
- Tags: governance, governor
- Functions: getProxyImplementation, getProxyPendingImplementation, getProxyAdmin, changeProxyAdmin, upgrade, upgradeTo, upgradeToAndCall, acceptProxy, acceptProxyAndCall, governor
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\data-service\IDataService.sol`

- Contracts: IDataService
- Tags: economic, staking, token
- Functions: register, acceptProvisionPendingParameters, startService, stopService, collect, slash, getThawingPeriodRange, getVerifierCutRange, getProvisionTokensRange, getDelegationRatio
- Modifiers: none
- Events: ServiceProviderRegistered, ProvisionPendingParametersAccepted, ServiceStarted, ServiceStopped, ServicePaymentCollected, ServiceProviderSlashed

## `packages\interfaces\contracts\data-service\IDataServiceFees.sol`

- Contracts: IDataServiceFees
- Tags: economic
- Functions: releaseStake
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\horizon\IAgreementOwner.sol`

- Contracts: IAgreementOwner
- Tags: escrow, token
- Functions: beforeCollection, afterCollection
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\horizon\IGraphPayments.sol`

- Contracts: IGraphPayments
- Tags: delegation, escrow, rewards, staking, token
- Functions: PROTOCOL_PAYMENT_CUT, initialize, collect
- Modifiers: none
- Events: GraphPaymentCollected

## `packages\interfaces\contracts\horizon\IGraphTallyCollector.sol`

- Contracts: IGraphTallyCollector
- Tags: token
- Functions: collect, recoverRAVSigner, encodeRAV
- Modifiers: none
- Events: RAVCollected

## `packages\interfaces\contracts\horizon\IHorizonStaking.sol`

- Contracts: IHorizonStaking
- Tags: staking
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\horizon\internal\IHorizonStakingBase.sol`

- Contracts: IHorizonStakingBase
- Tags: delegation, staking, token
- Functions: getSubgraphService, getServiceProvider, getStake, getIdleStake, getDelegationPool, getDelegation, getDelegationFeeCut, getProvision, getTokensAvailable, getProviderTokensAvailable, getDelegatedTokensAvailable, getThawRequest, getThawRequestList, getThawedTokens, getMaxThawingPeriod, isAllowedLockedVerifier, isDelegationSlashingEnabled
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\horizon\internal\IHorizonStakingMain.sol`

- Contracts: IHorizonStakingMain
- Tags: delegation, slashing, staking, token
- Functions: stake, stakeTo, stakeToProvision, unstake, withdraw, provision, addToProvision, thaw, deprovision, reprovision, setProvisionParameters, acceptProvisionParameters, delegate, addToDelegationPool, undelegate, withdrawDelegated, redelegate, setDelegationFeeCut, delegate, undelegate, withdrawDelegated, slash, provisionLocked, setOperatorLocked, setAllowedLockedVerifier
- Modifiers: none
- Events: HorizonStakeDeposited, HorizonStakeWithdrawn, ProvisionCreated, ProvisionIncreased, ProvisionThawed, TokensDeprovisioned, ProvisionParametersStaged, ProvisionParametersSet, OperatorSet, ProvisionSlashed, DelegationSlashed, DelegationSlashingSkipped, VerifierTokensSent, TokensDelegated, TokensUndelegated

## `packages\interfaces\contracts\horizon\internal\IHorizonStakingTypes.sol`

- Contracts: IHorizonStakingTypes
- Tags: delegation, economic, slashing, staking, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\horizon\IPaymentsCollector.sol`

- Contracts: IPaymentsCollector
- Tags: token
- Functions: collect
- Modifiers: none
- Events: PaymentCollected

## `packages\interfaces\contracts\horizon\IPaymentsEscrow.sol`

- Contracts: IPaymentsEscrow
- Tags: escrow, token
- Functions: MAX_WAIT_PERIOD, WITHDRAW_ESCROW_THAWING_PERIOD, initialize, deposit, depositTo, thaw, adjustThaw, cancelThaw, withdraw, collect, getBalance, escrowAccounts
- Modifiers: none
- Events: Deposit, CancelThaw, Thaw, Withdraw, EscrowCollected

## `packages\interfaces\contracts\horizon\IRecurringCollector.sol`

- Contracts: IRecurringCollector
- Tags: token
- Functions: pause, unpause, pauseGuardians, accept, cancel, update, hashRCA, hashRCAU, recoverRCASigner, recoverRCAUSigner, getAgreement, getCollectionInfo, generateAgreementId
- Modifiers: none
- Events: AgreementAccepted, AgreementCanceled, AgreementUpdated, RCACollected, PauseGuardianSet, PayerCallbackFailed, OfferStored, OfferCancelled

## `packages\interfaces\contracts\issuance\agreement\IRecurringAgreementHelper.sol`

- Contracts: IRecurringAgreementHelper
- Tags: escrow, permission, token
- Functions: auditGlobal, auditProviders, auditProviders, auditProvider, getAgreements, getAgreements, getCollectors, getCollectors, getProviders, getProviders, checkStaleness, reconcile, reconcileCollector, reconcileAll
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\agreement\IRecurringAgreementManagement.sol`

- Contracts: IRecurringAgreementManagement
- Tags: escrow
- Functions: offerAgreement, cancelAgreement, reconcileAgreement, forceRemoveAgreement, reconcileProvider, emergencyClearEligibilityOracle
- Modifiers: none
- Events: AgreementAdded, AgreementRejected, AgreementRemoved, AgreementReconciled, ProviderRemoved, CollectorRemoved

## `packages\interfaces\contracts\issuance\agreement\IRecurringAgreements.sol`

- Contracts: IRecurringAgreements
- Tags: escrow, token
- Functions: getEscrowBasis, getMinOnDemandBasisThreshold, getMinFullBasisMargin, getMinThawFraction, getMinResidualEscrowFactor, getSumMaxNextClaim, getTotalEscrowDeficit, getCollectorCount, getCollectorAt, getProviderCount, getProviderAt, getSumMaxNextClaim, getEscrowAccount, getEscrowSnap, getAgreementCount, getAgreementAt, getAgreementInfo, getAgreementMaxNextClaim
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\agreement\IRecurringEscrowManagement.sol`

- Contracts: IRecurringEscrowManagement
- Tags: escrow, token
- Functions: setEscrowBasis, setMinOnDemandBasisThreshold, setMinFullBasisMargin, setMinThawFraction, setMinResidualEscrowFactor
- Modifiers: none
- Events: EscrowFunded, EscrowWithdrawn, EscrowBasisSet, MinOnDemandBasisThresholdSet, MinFullBasisMarginSet, MinThawFractionSet, MinResidualEscrowFactorSet

## `packages\interfaces\contracts\issuance\allocate\IIssuanceAllocationAdministration.sol`

- Contracts: IIssuanceAllocationAdministration
- Tags: governance, governor, token
- Functions: setIssuancePerBlock, setIssuancePerBlock, setTargetAllocation, setTargetAllocation, setTargetAllocation, notifyTarget, forceTargetNoChangeNotificationBlock, setDefaultTarget, setDefaultTarget, distributePendingIssuance, distributePendingIssuance, setSelfMintingEventMode, getSelfMintingEventMode
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\allocate\IIssuanceAllocationDistribution.sol`

- Contracts: IIssuanceAllocationDistribution
- Tags: permission
- Functions: distributeIssuance, getTargetIssuancePerBlock
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\allocate\ISendTokens.sol`

- Contracts: ISendTokens
- Tags: token
- Functions: sendTokens
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\common\IEmergencyRoleControl.sol`

- Contracts: IEmergencyRoleControl
- Tags: governance, governor
- Functions: emergencyRevokeRole
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\eligibility\IProviderEligibility.sol`

- Contracts: IProviderEligibility
- Tags: rewards, rewardsmanager
- Functions: isEligible
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\eligibility\IProviderEligibilityManagement.sol`

- Contracts: IProviderEligibilityManagement
- Tags: rewards
- Functions: setProviderEligibilityOracle, getProviderEligibilityOracle
- Modifiers: none
- Events: ProviderEligibilityOracleSet

## `packages\interfaces\contracts\issuance\eligibility\IRewardsEligibilityAdministration.sol`

- Contracts: IRewardsEligibilityAdministration
- Tags: permission, rewards
- Functions: setEligibilityPeriod, setOracleUpdateTimeout, setEligibilityValidation, setIndexerRetentionPeriod
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\eligibility\IRewardsEligibilityEvents.sol`

- Contracts: IRewardsEligibilityEvents
- Tags: rewards
- Functions: none
- Modifiers: none
- Events: IndexerEligibilityData, IndexerEligibilityRenewed, EligibilityPeriodUpdated, EligibilityValidationUpdated, OracleUpdateTimeoutUpdated, IndexerTrackingUpdated, IndexerRetentionPeriodSet

## `packages\interfaces\contracts\issuance\eligibility\IRewardsEligibilityHelper.sol`

- Contracts: IRewardsEligibilityHelper
- Tags: permission, rewards
- Functions: removeExpiredIndexers, removeExpiredIndexers, removeExpiredIndexers
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\eligibility\IRewardsEligibilityMaintenance.sol`

- Contracts: IRewardsEligibilityMaintenance
- Tags: permission, rewards
- Functions: removeExpiredIndexer
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\eligibility\IRewardsEligibilityReporting.sol`

- Contracts: IRewardsEligibilityReporting
- Tags: rewards
- Functions: renewIndexerEligibility
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\eligibility\IRewardsEligibilityStatus.sol`

- Contracts: IRewardsEligibilityStatus
- Tags: rewards
- Functions: getEligibilityRenewalTime, getEligibilityPeriod, getOracleUpdateTimeout, getLastOracleUpdateTime, getEligibilityValidation, getIndexerRetentionPeriod, getIndexerCount, getIndexers, getIndexers
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\subgraph-service\IDisputeManager.sol`

- Contracts: IDisputeManager
- Tags: delegation, disputemanager, disputes, slashing, token, dispute
- Functions: initialize, setDisputePeriod, setArbitrator, setDisputeDeposit, setFishermanRewardCut, setMaxSlashingCut, setSubgraphService, createQueryDispute, createQueryDisputeConflict, createIndexingDispute, createIndexingFeeDisputeV1, acceptDispute, acceptDisputeConflict, rejectDispute, drawDispute, cancelDispute, getFishermanRewardCut, getDisputePeriod, isDisputeCreated, encodeReceipt, getAttestationIndexer, getStakeSnapshot, areConflictingAttestations, disputePeriod, fishermanRewardCut
- Modifiers: none
- Events: ArbitratorSet, DisputePeriodSet, DisputeDepositSet, MaxSlashingCutSet, FishermanRewardCutSet, SubgraphServiceSet, QueryDisputeCreated, IndexingFeeDisputeCreated, IndexingDisputeCreated, DisputeAccepted, DisputeRejected, DisputeDrawn, DisputeLinked, DisputeCancelled

## `packages\interfaces\contracts\subgraph-service\internal\IAllocation.sol`

- Contracts: IAllocation
- Tags: rewards, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\subgraph-service\internal\IAllocationManager.sol`

- Contracts: IAllocationManager
- Tags: delegation, rewards, token
- Functions: allocationProvisionTracker, maxPOIStaleness
- Modifiers: none
- Events: AllocationCreated, IndexingRewardsCollected, AllocationResized, AllocationClosed, MaxPOIStalenessSet, POIPresented

## `packages\interfaces\contracts\subgraph-service\ISubgraphService.sol`

- Contracts: ISubgraphService
- Tags: curation, token
- Functions: initialize, closeStaleAllocation, resizeAllocation, setPauseGuardian, setMinimumProvisionTokens, setDelegationRatio, setStakeToFeesRatio, setMaxPOIStaleness, setCurationCut, setIndexingFeesCut, setPaymentsDestination, setBlockClosingAllocationWithActiveAgreement, getBlockClosingAllocationWithActiveAgreement, acceptIndexingAgreement, updateIndexingAgreement, cancelIndexingAgreement, getIndexingAgreement, getAllocation, getLegacyAllocation, encodeAllocationProof, isOverAllocated, getDisputeManager, getGraphTallyCollector, getCuration, indexers
- Modifiers: none
- Events: QueryFeesCollected, PaymentsDestinationSet, StakeToFeesRatioSet, CurationCutSet, IndexingFeesCutSet, BlockClosingAllocationWithActiveAgreementSet

## `packages\interfaces\contracts\token-distribution\IGraphTokenLockWallet.sol`

- Contracts: IGraphTokenLockWallet
- Tags: graphtoken, graphtokenlockwallet, token, vesting
- Functions: beneficiary, token, managedAmount, startTime, endTime, periods, releaseStartTime, vestingCliffTime, revocable, isRevoked, currentTime, duration, sinceStartTime, amountPerPeriod, periodDuration, currentPeriod, passedPeriods, releasableAmount, vestedAmount, releasedAmount, usedAmount, currentBalance, surplusAmount, totalOutstandingAmount, release
- Modifiers: none
- Events: ManagerUpdated, OwnershipTransferred, TokenDestinationsApproved, TokenDestinationsRevoked, TokensReleased, TokensRevoked, TokensWithdrawn

## `packages\interfaces\contracts\toolshed\IControllerToolshed.sol`

- Contracts: IControllerToolshed
- Tags: governance
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IDisputeManagerToolshed.sol`

- Contracts: IDisputeManagerToolshed
- Tags: disputemanager, dispute
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IGraphTallyCollectorToolshed.sol`

- Contracts: IGraphTallyCollectorToolshed
- Tags: token
- Functions: authorizations, tokensCollected
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IGraphTokenLockWalletToolshed.sol`

- Contracts: IGraphTokenLockWalletToolshed
- Tags: delegation, graphtoken, graphtokenlockwallet, rewards, token, vesting
- Functions: stake, unstake, withdraw, provisionLocked, thaw, deprovision, setOperatorLocked, setDelegationFeeCut, setRewardsDestination, delegate, undelegate, withdrawDelegated, withdrawDelegated
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IHorizonStakingToolshed.sol`

- Contracts: IHorizonStakingToolshed
- Tags: staking
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IL2CurationToolshed.sol`

- Contracts: IL2CurationToolshed
- Tags: curation
- Functions: subgraphService
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\internal\IProvisionManager.sol`

- Contracts: IProvisionManager
- Tags: delegation, token
- Functions: none
- Modifiers: none
- Events: ProvisionTokensRangeSet, DelegationRatioSet, VerifierCutRangeSet, ThawingPeriodRangeSet

## `packages\interfaces\contracts\toolshed\internal\IProvisionTracker.sol`

- Contracts: IProvisionTracker
- Tags: token
- Functions: feesProvisionTracker
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IPaymentsEscrowToolshed.sol`

- Contracts: IPaymentsEscrowToolshed
- Tags: escrow
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IRewardsManagerToolshed.sol`

- Contracts: IRewardsManagerToolshed
- Tags: rewards, rewardsmanager
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IServiceRegistryToolshed.sol`

- Contracts: IServiceRegistryToolshed
- Tags: registry
- Functions: services
- Modifiers: none
- Events: ServiceRegistered

## `packages\issuance\contracts\agreement\RecurringAgreementHelper.sol`

- Contracts: RecurringAgreementHelper
- Tags: escrow, graphtoken, permission, token
- Functions: auditGlobal, auditProviders, auditProviders, auditProvider, getAgreements, getAgreements, getCollectors, getCollectors, getProviders, getProviders, checkStaleness, reconcile, reconcileCollector, reconcileAll, _auditProviders, _reconcile
- Modifiers: none
- Events: none

## `packages\issuance\contracts\agreement\RecurringAgreementManager.sol`

- Contracts: RecurringAgreementManager
- Tags: accounting, escrow, governance, governor, graphtoken, token
- Functions: initialize, supportsInterface, beforeIssuanceAllocationChange, getIssuanceAllocator, setIssuanceAllocator, beforeCollection, afterCollection, offerAgreement, forceRemoveAgreement, emergencyClearEligibilityOracle, emergencyRevokeRole, cancelAgreement, reconcileAgreement, reconcileProvider, setEscrowBasis, setMinOnDemandBasisThreshold, setMinFullBasisMargin, setMinThawFraction, setMinResidualEscrowFactor, setProviderEligibilityOracle, _setProviderEligibilityOracle, getProviderEligibilityOracle, isEligible, getSumMaxNextClaim, getEscrowAccount
- Modifiers: none
- Events: DistributeIssuanceFailed

## `packages\issuance\contracts\allocate\DirectAllocation.sol`

- Contracts: DirectAllocation
- Tags: graphtoken, token
- Functions: _getDirectAllocationStorage, initialize, supportsInterface, sendTokens, beforeIssuanceAllocationChange, getIssuanceAllocator, setIssuanceAllocator
- Modifiers: none
- Events: TokensSent

## `packages\issuance\contracts\allocate\IssuanceAllocator.sol`

- Contracts: IssuanceAllocator
- Tags: accounting, graphtoken, rewards, rewardsmanager, token
- Functions: _getIssuanceAllocatorStorage, initialize, supportsInterface, distributeIssuance, _advanceSelfMintingBlock, _distributeIssuance, distributePendingIssuance, distributePendingIssuance, _distributePendingIssuance, _distributePendingWithFullRate, _distributePendingProportionally, setIssuancePerBlock, setIssuancePerBlock, _setIssuancePerBlock, setSelfMintingEventMode, getSelfMintingEventMode, _notifyTarget, notifyTarget, forceTargetNoChangeNotificationBlock, setTargetAllocation, setTargetAllocation, setTargetAllocation, setDefaultTarget, setDefaultTarget, _setDefaultTarget
- Modifiers: none
- Events: IssuanceDistributed, TargetAllocationUpdated, IssuancePerBlockUpdated, DefaultTargetUpdated, IssuanceSelfMintAllowance, IssuanceSelfMintAllowanceAggregate, SelfMintingEventModeUpdated

## `packages\issuance\contracts\common\BaseUpgradeable.sol`

- Contracts: BaseUpgradeable
- Tags: governance, governor, graphtoken, token
- Functions: __BaseUpgradeable_init, __BaseUpgradeable_init_unchained, pause, unpause, paused, supportsInterface
- Modifiers: none
- Events: none

## `packages\issuance\contracts\common\IGraphToken.sol`

- Contracts: IGraphToken
- Tags: graphtoken, token
- Functions: mint
- Modifiers: none
- Events: none

## `packages\issuance\contracts\eligibility\mocks\MockRewardsEligibilityOracle.sol`

- Contracts: MockRewardsEligibilityOracle
- Tags: governor, graphtoken, rewards, rewardsmanager, token
- Functions: initialize, setEligible, isEligible, supportsInterface
- Modifiers: none
- Events: EligibilitySet

## `packages\issuance\contracts\eligibility\RewardsEligibilityHelper.sol`

- Contracts: RewardsEligibilityHelper
- Tags: permission, rewards
- Functions: removeExpiredIndexers, removeExpiredIndexers, removeExpiredIndexers
- Modifiers: none
- Events: none

## `packages\issuance\contracts\eligibility\RewardsEligibilityOracle.sol`

- Contracts: RewardsEligibilityOracle
- Tags: graphtoken, rewards, token
- Functions: _getRewardsEligibilityOracleStorage, initialize, supportsInterface, setEligibilityPeriod, setOracleUpdateTimeout, setEligibilityValidation, setIndexerRetentionPeriod, renewIndexerEligibility, removeExpiredIndexer, isEligible, getEligibilityRenewalTime, getEligibilityPeriod, getOracleUpdateTimeout, getLastOracleUpdateTime, getEligibilityValidation, getIndexerRetentionPeriod, getIndexerCount, getIndexers, getIndexers
- Modifiers: none
- Events: none

## `packages\issuance\contracts\test\allocate\IssuanceAllocatorTestHarness.sol`

- Contracts: IssuanceAllocatorTestHarness
- Tags: graphtoken, token
- Functions: exposedDistributePendingProportionally, exposedDistributePendingWithFullRate
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\afterCollection.t.sol`

- Contracts: RecurringAgreementManagerCollectionCallbackTest
- Tags: escrow, token
- Functions: test_BeforeCollection_TopsUpWhenEscrowShort, test_BeforeCollection_NoOpWhenEscrowSufficient, test_BeforeCollection_NoOp_WhenCallerNotRecurringCollector, test_BeforeCollection_IgnoresUnknownAgreement, test_AfterCollection_ReconcileAndFundEscrow, test_AfterCollection_NoOp_WhenCallerNotRecurringCollector, test_AfterCollection_IgnoresUnknownAgreement, test_AfterCollection_CanceledByServiceProvider
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\approver.t.sol`

- Contracts: RecurringAgreementManagerApproverTest
- Tags: escrow, governor, token
- Functions: test_SupportsInterface_IIssuanceTarget, test_SupportsInterface_IAgreementOwner, test_SupportsInterface_IRecurringAgreementManagement, test_SupportsInterface_IRecurringEscrowManagement, test_SupportsInterface_IProviderEligibilityManagement, test_SupportsInterface_IRecurringAgreements, test_BeforeIssuanceAllocationChange_DoesNotRevert, test_SetIssuanceAllocator_OnlyGovernor, test_SetIssuanceAllocator_Governor, test_GetDeficit_ZeroWhenFullyFunded, test_GetEscrowAccount_MatchesUnderlying, test_GetRequiredEscrow_ZeroForUnknownIndexer, test_GetAgreementMaxNextClaim_ZeroForUnknown, test_GetIndexerAgreementCount_ZeroForUnknown
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\branchCoverage.t.sol`

- Contracts: RecurringAgreementManagerBranchCoverageTest, ZeroIdCollector
- Tags: governor
- Functions: test_SetIssuanceAllocator_Revert_InvalidERC165, test_SetIssuanceAllocator_Revert_EOA, test_OfferAgreement_Revert_UnauthorizedCollector, test_OfferAgreement_Revert_PayerMismatch, test_OfferAgreement_Revert_ZeroServiceProvider, test_OfferAgreement_Revert_UnauthorizedDataService, test_ForceRemoveAgreement_NoOp_UnknownAgreement, test_ForceRemoveAgreement_RemovesTracked, test_EmergencyRevokeRole_Revert_CannotRevokeGovernor, test_EmergencyRevokeRole_Success, test_GetIssuanceAllocator_ReturnsConfiguredValue, test_OfferAgreement_Revert_AgreementIdZero, test_WithdrawAndRebalance_DepositDeficit, offer
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\callbackGas.t.sol`

- Contracts: RecurringAgreementManagerCallbackGasTest
- Tags: escrow, governor, token
- Functions: setUp, test_BeforeCollection_GasWithinBudget_JitDeposit, test_BeforeCollection_GasWithinBudget_EscrowSufficient, test_AfterCollection_GasWithinBudget_FullReconcile, test_AfterCollection_GasWithinBudget_CanceledBySP
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\cancelAgreement.t.sol`

- Contracts: RecurringAgreementManagerCancelAgreementTest
- Tags: escrow
- Functions: test_CancelAgreement_Accepted, test_CancelAgreement_ReconcileAfterCancel, test_CancelAgreement_AlreadyCanceled_StillForwards, test_CancelAgreement_Idempotent_CanceledByServiceProvider, test_CancelAgreement_Offered, test_CancelAgreement_RejectsUnknown_WhenNotOffered, test_CancelAgreement_Revert_WhenNotOperator, test_CancelAgreement_SucceedsWhenPaused, test_CancelAgreement_EmitsEvent, test_CancelAgreement_Succeeds_WhenPaused
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\cancelWithPendingUpdate.t.sol`

- Contracts: RecurringAgreementManagerCancelWithPendingUpdateTest
- Tags: escrow
- Functions: test_CancelAgreement_PendingUpdateEscrowNotFreed, test_CancelAgreement_PendingClearedAfterReconcile
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\cascadeCleanup.t.sol`

- Contracts: RecurringAgreementManagerCascadeCleanupTest
- Tags: governor, token
- Functions: setUp, _collector2, _makeRCAForCollector, _makeRCAForProvider, _offerForCollector, test_Cascade_SingleAgreement_PopulatesSets, test_Cascade_TwoAgreements_SamePair_CountIncrements, test_Cascade_MultiCollector_BothTracked, test_Cascade_MultiProvider_BothTracked, test_Cascade_ReconcileOneOfTwo_PairStaysTracked, test_Cascade_ReconcileLast_PairStaysWhileEscrowThawing, test_Cascade_ReconcileLastProvider_CollectorCleanedUp_OtherCollectorRemains, test_Cascade_ReconcileProvider_CollectorRetainsOtherProvider, test_Cascade_ReaddAfterFullCleanup, test_Cascade_CancelOffered_DeferredCleanup, test_ReconcileCollectorProvider_ReturnsTrue_WhenAgreementsExist, test_ReconcileCollectorProvider_ReturnsFalse_WhenNotTracked, test_ReconcileCollectorProvider_ReturnsTrue_WhenEscrowThawing, test_ReconcileCollectorProvider_ReturnsFalse_AfterThawPeriod, test_ReconcileCollectorProvider_Permissionless, test_Helper_ReconcilePair_FirstCallStartsThaw_SecondCallCompletes, test_Helper_ReconcileCollector_TwoPhase, test_GetCollectors_Enumeration, test_GetCollectorProviders_Enumeration
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\discovery.t.sol`

- Contracts: RecurringAgreementManagerDiscoveryTest
- Tags: escrow, token
- Functions: test_Discovery_AcceptedAgreement_ViaReconcile, test_Discovery_CanceledBySP_ViaReconcile, test_Discovery_Idempotent_SecondReconcileNoReRegister, test_Discovery_RejectsUnknownAgreement, test_Discovery_RejectsUnauthorizedCollector, test_Discovery_RejectsPayerMismatch, test_Discovery_RejectsUnauthorizedDataService, test_OutOfBand_AcceptedThenSPCancel_ReconcileRemoves, test_OutOfBand_CollectionReducesMaxClaim_ReconcileUpdates, test_Discovery_Permissionless
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\edgeCases.t.sol`

- Contracts: RecurringAgreementManagerEdgeCasesTest
- Tags: escrow
- Functions: _getProviderAgreements, test_SupportsInterface_UnknownInterfaceReturnsFalse, test_SupportsInterface_ERC165, test_CancelOffered_CleansUpAgreement, test_CancelOffered_CleansUpPendingUpdate, test_Remove_CleansUpAgreement, test_Remove_CleansUpPendingUpdate, test_Reconcile_ClearsAppliedPendingUpdate, test_OfferUpdate_ReplacesExistingPendingOnCollector, test_Offer_ZeroMaxInitialTokens, test_Offer_ZeroOngoingTokensPerSecond, test_Offer_AllZeroValues, test_Remove_AtExactDeadline_NotAccepted, test_Remove_OneSecondAfterDeadline_NotAccepted, test_Reconcile_WhenCollectionEndEqualsCollectionStart, test_Offer_ZeroTokenBalance_PartialFunding, test_ReconcileBatch_InterleavedDuplicateIndexers, test_ReconcileBatch_EmptyArray, test_ReconcileBatch_NonExistentAgreements, test_UpdateEscrow_FullThawWithdrawCycle, test_OfferUpdate_ZeroValuePendingUpdate_ReplacedByNonZero, test_Reconcile_ZeroValuePendingUpdate_ClearedWhenApplied, test_ReofferAfterRemove_FullLifecycle, test_ReofferAfterRemove_WithDifferentNonce, test_Offer_Revert_ZeroServiceProvider
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\eligibility.t.sol`

- Contracts: RecurringAgreementManagerEligibilityTest
- Tags: governor
- Functions: setUp, test_SetPaymentEligibilityOracle, test_SetPaymentEligibilityOracle_DisableWithZeroAddress, test_SetPaymentEligibilityOracle_NoopWhenSameOracle, test_SetPaymentEligibilityOracle_Revert_WhenNotGovernor, test_GetProviderEligibilityOracle_ReturnsZeroByDefault, test_GetProviderEligibilityOracle_ReturnsSetOracle, test_IsEligible_TrueWhenNoOracle, test_IsEligible_DelegatesToOracle_WhenEligible, test_IsEligible_DelegatesToOracle_WhenNotEligible, test_IsEligible_TrueAfterOracleDisabled, test_SupportsInterface_IProviderEligibility
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\ensureDistributed.t.sol`

- Contracts: RecurringAgreementManagerEnsureDistributedTest, NoERC165Contract
- Tags: escrow, governor, token
- Functions: setUp, test_SetIssuanceAllocator_StoresAddress, test_SetIssuanceAllocator_Revert_WhenNotGovernor, test_SetIssuanceAllocator_CanSetToZero, test_SetIssuanceAllocator_NoopWhenUnchanged, test_BeforeCollection_CallsDistributeWhenEscrowShort, test_BeforeCollection_DistributionPreventsUnnecessaryTempJit, test_BeforeCollection_SkipsDistributeWhenEscrowSufficient, test_UpdateEscrow_CallsDistributeViaAfterCollection, test_UpdateEscrow_CallsDistributeViaOfferAgreement, test_EnsureDistributed_NoopWhenAllocatorNotSet, test_EnsureDistributed_WorksAcrossUint32Boundary, test_EnsureDistributed_SameBlockDedup_AtUint32Boundary, test_SetIssuanceAllocator_Revert_WhenNotERC165, test_SetIssuanceAllocator_Revert_WhenEOA, test_SetIssuanceAllocator_NewAllocatorCalledNextBlock, test_EnsureDistributed_CatchesAllocatorRevert, test_EnsureDistributed_EmitsEventOnAllocatorRevert, doSomething
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\escrowEdgeCases.t.sol`

- Contracts: RecurringAgreementManagerEscrowEdgeCasesTest
- Tags: escrow
- Functions: setUp, _makeRCAForIndexer, _escrowBalance, _escrowThawing, test_RegisteredOnly_TrackedAndCancelable, test_RegisteredOnly_RemovedOnReconcileAfterExpiry, test_RegisteredOnly_ContributesToEscrow, test_BasisDegradation_InsufficientBalance_PartialDeposit, test_BasisDegradation_RecoveryWithSufficientFunding, test_CrossProviderEscrow_IsolatedTracking, test_CrossProviderEscrow_ThawDoesNotAffectOther, test_EligibilityOracle_FlipDuringActiveAgreement, test_EligibilityOracle_EmergencyClear_FailOpen
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\escrowSnapStaleness.t.sol`

- Contracts: RecurringAgreementManagerEscrowSnapStalenessTest
- Tags: escrow, token
- Functions: test_EscrowSnap_SelfCorrectionAfterExternalDeposit, test_EscrowSnap_CorrectionOnExternalIncrease, test_ThresholdBoundary_OnDemandExactThreshold, test_ThresholdBoundary_FullBasisMargin, test_EscrowSnap_DeficitAccuracyMultipleOps
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\fundingModes.t.sol`

- Contracts: RecurringAgreementManagerFundingModesTest
- Tags: escrow, governor
- Functions: setUp, _makeRCAForIndexer, test_SetEscrowBasis_DefaultIsFull, test_SetEscrowBasis_OperatorCanSet, test_SetEscrowBasis_Revert_WhenNotOperator, test_GlobalTracking_TotalRequired, test_GlobalTracking_TotalUndeposited, test_GlobalTracking_TotalUndeposited_WhenPartiallyFunded, test_GlobalTracking_CancelDecrementsCountAndRequired, test_GlobalTracking_RemoveDecrementsCountAndRequired, test_GlobalTracking_ReconcileUpdatesRequired, test_GlobalTracking_TotalUndeposited_MultiProvider, test_GlobalTracking_TotalUndeposited_OverdepositedProviderDoesNotMaskDeficit, test_FullMode_DepositsFullRequired, test_FullMode_ThawsExcess, test_JustInTime_ThawsEverything, test_JustInTime_NoProactiveDeposit, test_JustInTime_JITStillWorks, test_OnDemand_NoProactiveDeposit, test_OnDemand_HoldsAtRequiredLevel, test_OnDemand_PreservesThawFromJIT, test_OnDemand_JITStillWorks, test_Degradation_FullToOnDemand_WhenInsufficientBalance, test_Degradation_NeverReachesJustInTime, test_ModeSwitch_PreservesAgreements
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\fuzz.t.sol`

- Contracts: RecurringAgreementManagerFuzzTest
- Tags: escrow, token
- Functions: testFuzz_Offer_MaxNextClaimCalculation, testFuzz_Offer_EscrowFundedUpToAvailable, testFuzz_Offer_RequiredEscrowIncrements, testFuzz_CancelOffered_RequiredEscrowDecrements, testFuzz_Remove_AfterSPCancel_ClearsState, testFuzz_Reconcile_AfterCollection_UpdatesRequired, testFuzz_OfferUpdate_DoubleFunding, testFuzz_Remove_ExpiredOffer_DeadlineBoundary, testFuzz_GetEscrowAccount_MatchesUnderlying
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\helper.t.sol`

- Contracts: RecurringAgreementHelperTest
- Tags: graphtoken, token
- Functions: test_Constructor_SetsManager, test_Constructor_Revert_ZeroManager, test_Constructor_Revert_ZeroGraphToken, test_Reconcile_AllAgreementsForIndexer, test_Reconcile_EmptyProvider, test_Reconcile_IdempotentWhenUnchanged, test_Reconcile_MultipleAgreements_MixedStates, test_ReconcileBatch_BasicBatch, test_ReconcileBatch_SkipsNonExistent, test_ReconcileBatch_Empty, test_ReconcileBatch_CrossIndexer, test_ReconcileBatch_Permissionless, _setSimulatedAgreement, test_ReconcileBatch_ClearsPendingUpdate
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\helperAudit.t.sol`

- Contracts: RecurringAgreementHelperAuditTest
- Tags: escrow, governor, token
- Functions: setUp, _makeRCAForCollector, _offerForCollector, test_AuditGlobal_EmptyState, test_AuditGlobal_WithAgreements, test_AuditGlobal_MultiCollector, test_AuditPair_NonExistent, test_AuditPair_WithAgreement, test_AuditPair_EscrowThawing, test_AuditPairs_EmptyCollector, test_AuditPairs_MultiplePairs, test_AuditPairs_Paginated, test_GetProviderAgreements_Paginated, test_GetCollectors_Paginated, test_AuditPairs_IsolatesCollectors, test_CheckPairStaleness_DetectsStaleAgreement
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\helperCleanup.t.sol`

- Contracts: RecurringAgreementHelperCleanupTest
- Tags: governor, token
- Functions: setUp, _makeRCAFor, _offerForCollector, _setCanceledBySPOnCollector, test_Reconcile_RemovesCanceledBySP, test_Reconcile_SkipsStillClaimable, test_Reconcile_MixedStates, test_Reconcile_EmptyProvider, test_Reconcile_ExpiredOffer, test_Reconcile_Permissionless, test_ReconcilePair_RemovesAgreementButPairStaysWhileThawing, test_ReconcilePair_PairExistsWhenAgreementsRemain, test_ReconcilePair_IsolatesCollectors, test_ReconcileCollector_AllPairs, test_ReconcileCollector_PartialCleanup, test_ReconcileAll_FullSweep, test_ReconcileAll_EmptyState, test_ReconcileAll_PartialCleanup, test_ReconcilePair_OnlyReconcilesPairAgreements, test_ReconcileAll_AllCollectorsAllProviders, test_Reconcile_ReconcilesThenRemoves, test_Reconcile_NoopWhenAllActive, test_ReconcilePair_RemovesAgreementAndPairAfterThaw
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\lifecycle.t.sol`

- Contracts: RecurringAgreementLifecycleTest
- Tags: escrow, governor, token
- Functions: setUp, _makeRCAFor, _offerForCollector, _setCanceledBySPOnCollector, test_Lifecycle_OfferAcceptCancelReconcileCleanup, test_Lifecycle_EscrowBasisChange_FullToOnDemand, test_Lifecycle_MultiCollectorMultiProvider, test_Lifecycle_ExpiredOffer_CleanupRemoves, test_Lifecycle_ReconcilePair_IsolatesCollectors, test_Lifecycle_EscrowBasisChange_OnDemandToFull
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\mocks\MockGraphToken.sol`

- Contracts: MockGraphToken
- Tags: graphtoken, token
- Functions: mint
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\mocks\MockIssuanceAllocator.sol`

- Contracts: MockIssuanceAllocator
- Tags: graphtoken, token
- Functions: setMintPerDistribution, setShouldRevert, distributeIssuance, getTargetIssuancePerBlock, supportsInterface
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\mocks\MockPaymentsEscrow.sol`

- Contracts: MockPaymentsEscrow
- Tags: escrow, token
- Functions: deposit, thaw, adjustThaw, cancelThaw, _thaw, withdraw, escrowAccounts, getBalance, setAccount, initialize, depositTo, collect, MAX_WAIT_PERIOD, WITHDRAW_ESCROW_THAWING_PERIOD
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\mocks\MockRecurringCollector.sol`

- Contracts: MockRecurringCollector
- Tags: token
- Functions: getUpdateNonce, setUpdateNonce, setAgreement, getAgreementDetails, getMaxNextClaim, getMaxNextClaim, _mockClaimForTerms, offer, _offerNew, _offerUpdate, _storeOffer, _storeOfferTerms, _storeUpdate, cancel, _cancelInternal, generateAgreementId
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\multiCollector.t.sol`

- Contracts: RecurringAgreementManagerMultiCollectorTest
- Tags: escrow, governor, token
- Functions: setUp, _makeRCAForCollector, test_MultiCollector_RequiredEscrowIsolation, test_MultiCollector_BeforeCollectionOnlyOwnAgreements, test_MultiCollector_AfterCollectionOnlyOwnAgreements, test_MultiCollector_SeparateEscrowAccounts, test_MultiCollector_CancelOnlyAffectsOwnCollectorEscrow
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\multiIndexer.t.sol`

- Contracts: RecurringAgreementManagerMultiIndexerTest
- Tags: escrow
- Functions: setUp, _makeRCAForIndexer, test_MultiIndexer_OfferIsolation, test_MultiIndexer_CancelIsolation, test_MultiIndexer_RemoveIsolation, test_MultiIndexer_ReconcileIsolation, test_MultiIndexer_MultipleAgreementsPerIndexer, test_MultiIndexer_CancelAndReconcileIndependently, test_MultiIndexer_MaintainOnlyAffectsTargetIndexer, test_MultiIndexer_FullLifecycle, test_MultiIndexer_GetAgreementInfo
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\offerUpdate.t.sol`

- Contracts: RecurringAgreementManagerOfferUpdateTest
- Tags: escrow
- Functions: test_OfferUpdate_SetsState, test_OfferUpdate_StoresOnCollector, test_OfferUpdate_FundsEscrow, test_OfferUpdate_ReplacesExistingPending, test_OfferUpdate_EmitsEvent, test_OfferUpdate_Revert_WhenNotOffered, test_OfferUpdate_Revert_WhenNotOperator, test_OfferUpdate_Revert_WhenNonceWrong, test_OfferUpdate_Nonce2_AfterFirstAccepted, test_OfferUpdate_Revert_Nonce1_AfterFirstAccepted, test_OfferUpdate_ReconcilesDuringOffer, test_OfferUpdate_Succeeds_WhenPaused
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\reconcile.t.sol`

- Contracts: RecurringAgreementManagerReconcileTest
- Tags: token
- Functions: test_ReconcileAgreement_AfterFirstCollection, test_ReconcileAgreement_CanceledByServiceProvider, test_ReconcileAgreement_CanceledByPayer_WindowOpen, test_ReconcileAgreement_CanceledByPayer_WindowExpired, test_ReconcileAgreement_SkipsNotAccepted, test_ReconcileAgreement_EmitsEvent, test_ReconcileAgreement_NoEmitWhenUnchanged, test_ReconcileAgreement_ReturnsFalse_WhenNotOffered, test_ReconcileAgreement_ExpiredAgreement, test_ReconcileAgreement_ClearsPendingUpdate, test_ReconcileAgreement_KeepsPendingUpdate_WhenNotYetApplied, test_ReconcileAgreement_ReturnsTrue_WhenStillClaimable_Accepted, test_ReconcileAgreement_DeletesExpiredOffer, test_ReconcileAgreement_ReturnsTrue_WhenStillClaimable_NotAccepted, test_ReconcileAgreement_ReturnsTrue_WhenCanceledByPayer_WindowStillOpen, test_ReconcileAgreement_ReducesRequiredEscrow_WithMultipleAgreements, test_ReconcileAgreement_Permissionless, test_ReconcileAgreement_ClearsPendingUpdate_WhenCanceled
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\register.t.sol`

- Contracts: RecurringAgreementManagerOfferTest
- Tags: escrow, token
- Functions: test_Offer_SetsAgreementState, test_Offer_FundsEscrow, test_Offer_PartialFunding_WhenInsufficientBalance, test_Offer_EmitsEvent, test_Offer_StoresOnCollector, test_Offer_MultipleAgreements_SameIndexer, test_Offer_Revert_WhenPayerMismatch, test_Offer_Revert_WhenNotOperator, test_Offer_Revert_WhenUnauthorizedCollector, test_Offer_Succeeds_WhenPaused
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\residualEscrow.t.sol`

- Contracts: RecurringAgreementManagerResidualEscrowTest
- Tags: escrow, token
- Functions: _createAndCancelAgreement, _injectDust, test_ResidualEscrow_DropsTrackingBelowThreshold, test_ResidualEscrow_KeepsTrackingAboveThreshold, test_ResidualEscrow_DustGriefingDropsTracking, test_ResidualEscrow_BlindDrainUntrackedPair, test_ResidualEscrow_BlindDrainWithdrawsMaturedThaw, test_ResidualEscrow_BlindDrainNoopMidThaw, test_ResidualEscrow_ReentryRestoresTracking, test_ResidualEscrow_ReentryWithStaleSnapCorrects, test_ResidualEscrow_SetFactor, test_ResidualEscrow_SetFactor_SameValueNoop, test_ResidualEscrow_SetFactor_EmitsEvent, test_ResidualEscrow_SetFactor_ZeroDisables
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\shared.t.sol`

- Contracts: RecurringAgreementManagerSharedTest
- Tags: escrow, governor, graphtoken, token
- Functions: setUp, _collector, _makeRCA, _makeRCAWithId, _offerAgreement, _makeRCAU, _offerAgreementUpdate, _cancelAgreement, _cancelPendingUpdate, _activeTermsFromRCA, _emptyTerms, _buildAgreementStorage, _setAgreementAccepted, _setAgreementCanceledBySP, _setAgreementCanceledByPayer, _setAgreementCollected
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\updateEscrow.t.sol`

- Contracts: RecurringAgreementManagerUpdateEscrowTest
- Tags: escrow, token
- Functions: test_UpdateEscrow_ThawsExcessWhenNoAgreements, test_UpdateEscrow_WithdrawsCompletedThaw, test_UpdateEscrow_NoopWhenNoBalance, test_UpdateEscrow_NoopWhenStillThawing, test_UpdateEscrow_Permissionless, test_UpdateEscrow_ThawsExcessWithActiveAgreements, test_OfferAgreement_PartialCancelPreservesThawTimer, test_UpdateEscrow_FullCancelWhenDeficit, test_UpdateEscrow_SkipsThawIncreaseToPreserveTimer, _check, _checkAtTimestamp, test_UpdateEscrow_Combinations, test_UpdateEscrow_CrossIndexerIsolation, test_UpdateEscrow_NoopWhenBalanced, test_Reconcile_AutomaticallyThawsExcess, test_UpdateEscrow_WithdrawsPartialWhenLiquidCoversMin, test_UpdateEscrow_PartialCancelAndWithdrawInOneCall, _checkFrac, test_UpdateEscrow_ThawTargetEdgeCases
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\allocator\construction.t.sol`

- Contracts: IssuanceAllocatorConstructionTest
- Tags: governor, graphtoken, token
- Functions: test_Revert_ZeroGraphTokenAddress, test_Revert_ZeroGovernorAddress, test_Init_GovernorRoleSet, test_Init_DefaultTargetCount, test_Init_DefaultTargetIsZeroAddress, test_Init_IssuancePerBlockIsZero, test_Init_LastDistributionBlockIsCurrentBlock, test_Revert_DoubleInitialization
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\allocator\defensiveChecks.t.sol`

- Contracts: IssuanceAllocatorDefensiveChecksTest
- Tags: graphtoken, token
- Functions: setUp, test_DistributePendingProportionally_AllocatedRateZero, test_DistributePendingProportionally_AvailableZero, test_DistributePendingProportionally_BothZero
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\allocator\distribution.t.sol`

- Contracts: IssuanceAllocatorDistributionTest
- Tags: governor, token
- Functions: test_DistributeIssuance_MintsTokensToTarget, test_DistributeIssuance_UpdatesLastDistributionBlock, test_DistributeIssuance_NoOpSameBlock, test_DistributeIssuance_ZeroIssuance, test_DistributeIssuance_NotPausedWhenDistributing, test_SetIssuancePerBlock, test_SetIssuancePerBlock_NotifiesDefaultTarget, test_Revert_DecreaseRateBelowAllocated, test_Revert_NonGovernorCannotSetIssuanceRate, test_OnlyNotifyTargetOncePerBlock, test_NotifyTarget_NewBlock, test_Revert_NotifyNonExistentTarget, test_Revert_NotificationFailsOnRevertingTarget, test_ForceTargetNoChangeNotificationBlock, test_ForceTargetNoChangeNotificationBlock_PastBlock, test_GetTargetIssuancePerBlock, test_GetTargetCount, test_GetTargetAddress, test_GetDistributionState, test_GetIssuancePerBlock, test_SetSelfMintingEventMode, test_DistributePendingIssuance_WithSelfMinting, test_Revert_NonGovernorCannotCallDistributePendingIssuance, test_Revert_ToBlockOutOfRange_Future, test_UnpauseResumeDistribution
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\allocator\distributionAccounting.t.sol`

- Contracts: IssuanceAllocatorDistributionAccountingTest, MockSimpleTarget3
- Tags: accounting, token
- Functions: setUp, test_InitializesWithDefaultTargetAtIndex0, test_DefaultTargetGets100PercentAllocation, test_TotalAllocation_ZeroWhenDefaultIsZeroAddress, test_AutoAdjustDefaultWhenSettingTarget, test_InvariantWithMultipleTargets, test_ZeroDefaultWhenFullyAllocated, test_AdjustDefaultWhenRemovingTarget, test_SelfMintingInInvariant, test_NoMintToZeroAddressDefault, test_MintToDefaultWhenSet, test_MultiTargetDistributionAccounting, test_DistributionWhenDefaultIsZeroPercent, test_DefaultTargetMaintainsAllocationAfterChange, test_TotalAllocation100PercentWithRealDefault, test_TotalMintedEqualsBlocksTimesRate
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\allocator\interfaceIdStability.t.sol`

- Contracts: AllocateInterfaceIdStabilityTest
- Tags: token
- Functions: test_InterfaceId_IIssuanceAllocationDistribution, test_InterfaceId_IIssuanceAllocationAdministration, test_InterfaceId_IIssuanceAllocationStatus, test_InterfaceId_IIssuanceAllocationData, test_InterfaceId_IIssuanceTarget, test_InterfaceId_ISendTokens, test_InterfaceId_IPausableControl, test_InterfaceId_IAccessControl
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\allocator\shared.t.sol`

- Contracts: IssuanceAllocatorSharedTest
- Tags: governor, graphtoken, token
- Functions: setUp, _addTarget, _addTargetWithSelfMinting, _setIssuanceRate
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\allocator\targetManagement.t.sol`

- Contracts: IssuanceAllocatorTargetManagementTest
- Tags: governor
- Functions: test_AddTarget_SupportsIIssuanceTarget, test_Revert_AddEOATarget, test_Revert_AddNonIIssuanceTargetContract, test_Revert_AddRevertingTarget, test_AddTarget_ReAddExistingTarget, test_RemoveTarget_SetAllocationToZero, test_RemoveTarget_WhenMultipleExist, test_RemoveTarget_SecondNonDefault_CoversLoopIncrement, test_Revert_AllocationExceedsBudget, test_AllocationExactlyEqualsBudget, test_SelfMintingTarget_NotMintedByAllocator, test_SelfMintingTarget_UpdateFlag, test_Revert_NonGovernorCannotSetAllocation, test_NonGovernorCanDistributeIssuance, test_Idempotent_OperateOnNonExistentTarget, test_Revert_CannotSetAllocationForDefaultTarget, test_SetDefaultTarget_CannotSetAllocatedTarget, test_SetDefaultTarget_WithMinDistributedBlock, test_SetTargetAllocation_4Param, test_GetTargets, test_GetTargetData, test_GetTotalAllocation, test_GetTotalAllocation_WithRealDefaultTarget, test_SetDefaultTarget_SameAddress_NoOp, test_SetDefaultTarget_ReturnsFalse_WhenPaused
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\direct-allocation\DirectAllocation.t.sol`

- Contracts: StubIssuanceAllocator, DirectAllocationTest, MockFalseTransferToken
- Tags: governor, graphtoken, token
- Functions: distributeIssuance, getTargetIssuancePerBlock, supportsInterface, setUp, test_Revert_ZeroGraphTokenAddress, test_Revert_ZeroGovernorAddress, test_Revert_DoubleInitialization, test_Init_GovernorRoleSet, test_Init_OperatorNotSet, test_SendTokens_Success, test_Revert_SendTokens_NonOperator, test_Revert_SendTokens_WhenPaused, test_Revert_SendTokens_InsufficientBalance, test_BeforeIssuanceAllocationChange_NoOp, test_GetIssuanceAllocator_InitiallyZero, test_SetIssuanceAllocator_UpdatesGetter, test_SetIssuanceAllocator_EmitsEvent, test_SetIssuanceAllocator_EmitsEventWithOldValue, test_SetIssuanceAllocator_SkipsWhenSameValue, test_SetIssuanceAllocator_AllowsZeroAddress, test_Revert_SetIssuanceAllocator_WhenEOA, test_Revert_SetIssuanceAllocator_WhenWrongInterface, test_Revert_SetIssuanceAllocator_NonGovernor, test_SupportsInterface_IERC165, test_SupportsInterface_IIssuanceTarget
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\accessControl.t.sol`

- Contracts: RewardsEligibilityOracleAccessControlTest
- Tags: governor, rewards
- Functions: test_OperatorCanGrantOracleRole, test_OperatorCanRevokeOracleRole, test_Revert_UnauthorizedCannotGrantOracleRole, test_Revert_UnauthorizedCannotRevokeOracleRole, test_Revert_NonOracleCannotRenew, test_PauseRoleCanPauseAndUnpause, test_Revert_NonPauseRoleCannotPause, test_Revert_NonPauseRoleCannotUnpause, test_Revert_NonOperatorCannotSetEligibilityPeriod, test_Revert_NonOperatorCannotSetOracleUpdateTimeout, test_Revert_NonOperatorCannotSetEligibilityValidation, test_GovernorRoleAdminOfItself, test_GovernorIsAdminOfPauseRole, test_GovernorIsAdminOfOperatorRole, test_OperatorIsAdminOfOracleRole, test_RoleMemberCount, test_EnumerateRoleMembers, test_Revert_OutOfBoundsIndex
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\construction.t.sol`

- Contracts: RewardsEligibilityOracleConstructionTest
- Tags: governor, graphtoken, rewards, token
- Functions: test_Revert_ZeroGraphTokenAddress, test_Revert_ZeroGovernorAddress, test_Init_GovernorRoleSet, test_Init_OracleRoleNotSetInitially, test_Init_DefaultEligibilityPeriod, test_Init_EligibilityValidationDisabled, test_Init_DefaultOracleUpdateTimeout, test_Init_LastOracleUpdateTimeIsZero, test_Revert_DoubleInitialization
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\eligibility.t.sol`

- Contracts: RewardsEligibilityOracleEligibilityTest
- Tags: rewards
- Functions: setUp, test_AllEligible_WhenValidationDisabled, test_AllEligible_WhenOracleTimeoutExceeded, test_IneligibleBeforeRenewal, test_EligibleAfterRenewal, test_IneligibleAfterPeriodExpires, test_EligibleAfterReRenewal, test_NeverRegisteredIndexerEligible_WhenPeriodExceedsTimestamp, test_RenewalTimeZero_ForNeverRenewedIndexer, test_RenewalTimeCorrect_AfterRenewal
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\helper.t.sol`

- Contracts: RewardsEligibilityHelperTest
- Tags: rewards
- Functions: setUp, test_Constructor_SetsOracle, test_Constructor_Revert_ZeroAddress, test_RemoveExpiredIndexers_List_AllExpired, test_RemoveExpiredIndexers_List_MixedExpiry, test_RemoveExpiredIndexers_List_IncludesUntracked, test_RemoveExpiredIndexers_List_Empty, test_RemoveExpiredIndexers_All_AllExpired, test_RemoveExpiredIndexers_All_MixedExpiry, test_RemoveExpiredIndexers_All_NoneTracked, test_RemoveExpiredIndexers_Scan_AllExpired, test_RemoveExpiredIndexers_Scan_MixedExpiry, test_RemoveExpiredIndexers_Scan_OffsetPastEnd, test_RemoveExpiredIndexers_Scan_PartialPage
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\indexerManagement.t.sol`

- Contracts: RewardsEligibilityOracleIndexerManagementTest
- Tags: rewards
- Functions: setUp, test_RenewSingleIndexer, test_RenewMultipleIndexers, test_RenewSameBlock_ReturnsZero, test_RenewNewBlock_ReturnsOne, test_Revert_NonOracleCannotRenew, test_ReturnCount_EmptyArray, test_ReturnCount_SkipsZeroAddresses, test_ReturnCount_SkipsDuplicatesInSameBlock, test_EmitsEvents, test_UpdatesLastOracleUpdateTime
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\indexerTracking.t.sol`

- Contracts: RewardsEligibilityOracleIndexerTrackingTest
- Tags: rewards
- Functions: setUp, test_Renewal_AddsToTrackedSet, test_Renewal_SecondIndexerIncreasesCount, test_Renewal_SameIndexerNoDuplicate, test_Renewal_EmitsTrackingEvent_OnlyFirstTime, test_GetIndexers_Paginated, test_GetIndexers_OffsetPastEnd_ReturnsEmpty, test_GetIndexers_CountClamped, test_DefaultIndexerRetentionPeriod, test_SetIndexerRetentionPeriod, test_SetIndexerRetentionPeriod_SameValue_NoEvent, test_Revert_SetIndexerRetentionPeriod_Unauthorized, test_RemoveExpiredIndexer_ReturnsFalse_WhenNotExpired, test_RemoveExpiredIndexer_ReturnsTrue_WhenExpired, test_RemoveExpiredIndexer_ReturnsTrue_WhenNotTracked, test_RemoveExpiredIndexer_DeletesTimestamp, test_RemoveExpiredIndexer_EmitsEvent, test_RemoveExpiredIndexer_ReAddAfterRemoval, test_RemoveExpiredIndexer_Permissionless
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\interfaceCompliance.t.sol`

- Contracts: RewardsEligibilityOracleInterfaceTest
- Tags: rewards
- Functions: test_SupportsERC165, test_SupportsIProviderEligibility, test_SupportsIRewardsEligibilityAdministration, test_SupportsIRewardsEligibilityMaintenance, test_SupportsIRewardsEligibilityReporting, test_SupportsIRewardsEligibilityStatus, test_SupportsIPausableControl, test_SupportsIAccessControl, test_DoesNotSupportRandomInterface, test_InterfaceId_IProviderEligibility, test_InterfaceId_IRewardsEligibilityAdministration, test_InterfaceId_IRewardsEligibilityMaintenance, test_InterfaceId_IRewardsEligibilityReporting, test_InterfaceId_IRewardsEligibilityStatus
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\operatorFunctions.t.sol`

- Contracts: RewardsEligibilityOracleOperatorFunctionsTest
- Tags: rewards
- Functions: setUp, test_SetEligibilityPeriod, test_SetEligibilityPeriod_EmitsEvent, test_SetEligibilityPeriod_Idempotent_NoEvent, test_SetOracleUpdateTimeout, test_SetOracleUpdateTimeout_EmitsEvent, test_SetOracleUpdateTimeout_Idempotent_NoEvent, test_EnableEligibilityValidation, test_DisableEligibilityValidation, test_SetEligibilityValidation_EmitsEvent_OnChange, test_SetEligibilityValidation_Idempotent_NoEvent
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\eligibility\shared.t.sol`

- Contracts: RewardsEligibilityOracleSharedTest
- Tags: governor, graphtoken, rewards, token
- Functions: setUp, _setupOracleRole, _setupOperatorRole, _enableValidation, _renewEligibility
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\mocks\MockGraphToken.sol`

- Contracts: MockGraphToken
- Tags: graphtoken, token
- Functions: mint
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\DisputeManager.sol`

- Contracts: DisputeManager
- Tags: disputemanager, disputes, graphtoken, permission, staking, token, dispute
- Functions: initialize, createIndexingDispute, createIndexingFeeDisputeV1, createQueryDispute, createQueryDisputeConflict, acceptDispute, acceptDisputeConflict, rejectDispute, drawDispute, cancelDispute, setArbitrator, setDisputePeriod, setDisputeDeposit, setFishermanRewardCut, setMaxSlashingCut, setSubgraphService, encodeReceipt, getFishermanRewardCut, getDisputePeriod, getStakeSnapshot, areConflictingAttestations, getAttestationIndexer, isDisputeCreated, _createQueryDisputeWithAttestation, _createIndexingDisputeWithAllocation
- Modifiers: onlyArbitrator, onlyPendingDispute, onlyFisherman
- Events: none

## `packages\subgraph-service\contracts\DisputeManagerStorage.sol`

- Contracts: DisputeManagerV1Storage
- Tags: disputemanager, disputes, slashing, dispute
- Functions: none
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\libraries\Allocation.sol`

- Contracts: Allocation
- Tags: rewards, token
- Functions: create, presentPOI, snapshotRewards, clearPendingRewards, close, get, isStale, exists, isOpen, isAltruistic, _get
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\libraries\AllocationHandler.sol`

- Contracts: AllocationHandler
- Tags: delegation, graphtoken, rewards, rewardsmanager, staking, token
- Functions: allocate, presentPOI, closeAllocation, resizeAllocation, _resizeAllocation, isOverAllocated, _closeAllocation, _distributeIndexingRewards, _isOverAllocated, _verifyAllocationProof
- Modifiers: none
- Events: AllocationCreated, IndexingRewardsCollected, AllocationResized, AllocationClosed, LegacyAllocationMigrated, MaxPOIStalenessSet, POIPresented

## `packages\subgraph-service\contracts\libraries\IndexingAgreement.sol`

- Contracts: IndexingAgreement
- Tags: token
- Functions: accept, update, cancel, onCloseAllocation, cancelByPayer, collect, get, _getStorageManager, _setTermsV1, _cancel, _requireValidAllocation, _tokensToCollect, _isActive, _isValid, _directory, _get, _validateTermsAgainstRCA
- Modifiers: none
- Events: IndexingFeesCollectedV1, IndexingAgreementCanceled, IndexingAgreementAccepted, IndexingAgreementUpdated

## `packages\subgraph-service\contracts\libraries\LegacyAllocation.sol`

- Contracts: LegacyAllocation
- Tags: staking
- Functions: revertIfExists, exists
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\SubgraphService.sol`

- Contracts: SubgraphService
- Tags: graphtoken, rewards, token
- Functions: initialize, register, acceptProvisionPendingParameters, startService, stopService, collect, slash, closeStaleAllocation, resizeAllocation, setPauseGuardian, setPaymentsDestination, setMinimumProvisionTokens, setDelegationRatio, setStakeToFeesRatio, setMaxPOIStaleness, setCurationCut, setIndexingFeesCut, setBlockClosingAllocationWithActiveAgreement, acceptIndexingAgreement, updateIndexingAgreement, cancelIndexingAgreement, cancelIndexingAgreementByPayer, getIndexingAgreement, getAllocation, getAllocationData
- Modifiers: enforceService
- Events: none

## `packages\subgraph-service\contracts\SubgraphServiceStorage.sol`

- Contracts: SubgraphServiceV1Storage, SubgraphServiceV2Storage
- Tags: curation, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\utilities\AllocationManager.sol`

- Contracts: AllocationManager
- Tags: delegation, graphtoken, rewards, token
- Functions: __AllocationManager_init, __AllocationManager_init_unchained, _allocate, _presentPoi, _resizeAllocation, _closeAllocation, _setMaxPoiStaleness, _encodeAllocationProof, _isOverAllocated
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\utilities\AllocationManagerStorage.sol`

- Contracts: AllocationManagerV1Storage
- Tags: rewards, token
- Functions: none
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\utilities\Directory.sol`

- Contracts: Directory
- Tags: curation, disputemanager, dispute
- Functions: recurringCollector, _subgraphService, _disputeManager, _graphTallyCollector, _curation
- Modifiers: onlyDisputeManager
- Events: SubgraphServiceDirectoryInitialized

## `packages\subgraph-service\test\unit\disputeManager\constructor\constructor.t.sol`

- Contracts: DisputeManagerConstructorTest
- Tags: disputemanager, governor, slashing, dispute
- Functions: _initializeDisputeManager, test_DisputeManager_Constructor, test_DisputeManager_Constructor_RevertIf_ControllerAddressIsZero, test_DisputeManager_Constructor_RevertIf_ArbitratorAddressIsZero, test_DisputeManager_Constructor_RevertIf_InvalidDisputePeriod, test_DisputeManager_Constructor_RevertIf_InvalidDisputeDeposit, test_DisputeManager_Constructor_RevertIf_InvalidFishermanRewardPercentage, test_DisputeManager_Constructor_RevertIf_InvalidMaxSlashingPercentage
- Modifiers: useDeployer
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\DisputeManager.t.sol`

- Contracts: DisputeManagerTest
- Tags: disputemanager, governor, slashing, token, dispute
- Functions: _setArbitrator, _setFishermanRewardCut, _setMaxSlashingCut, _setDisputeDeposit, _setSubgraphService, _createIndexingDispute, _createQueryDispute, _createQueryDisputeConflict, _acceptDispute, _acceptDisputeConflict, _acceptDisputeConflictExpectEmit, _verifyFishermanBalance, _verifyIndexerSlashing, _verifyDisputeStatus, _drawDispute, _rejectDispute, _cancelDispute, _createAttestationReceipt, _createConflictingAttestations, _createAtestationData, _getDispute, _setStorageSubgraphService
- Modifiers: useGovernor, useFisherman
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\disputes.t.sol`

- Contracts: DisputeManagerDisputeTest
- Tags: disputemanager, disputes, slashing, token, dispute
- Functions: test_Dispute_Accept_RevertIf_DisputeDoesNotExist, test_Dispute_Accept_RevertIf_SlashZeroTokens, test_Dispute_Reject_RevertIf_DisputeDoesNotExist, test_Dispute_Draw_RevertIf_DisputeDoesNotExist, test_Dispute_Cancel_RevertIf_DisputeDoesNotExist, test_Dispute_Accept_RevertIf_DisputeNotPending, test_Dispute_Reject_RevertIf_DisputeNotPending, test_Dispute_Draw_RevertIf_DisputeNotPending, test_Dispute_Cancel_RevertIf_DisputeNotPending, test_Dispute_AreConflictingAttestations, test_Dispute_GetAttestationIndexer_RevertIf_MismatchedSubgraph
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\indexing\accept.t.sol`

- Contracts: DisputeManagerIndexingAcceptDisputeTest
- Tags: disputemanager, disputes, slashing, token, dispute
- Functions: test_Indexing_Accept_Dispute, test_Indexing_Accept_Dispute_RevertWhen_SubgraphServiceNotSet, test_Indexing_Accept_Dispute_OptParam, test_Indexing_Accept_RevertIf_CallerIsNotArbitrator, test_Indexing_Accept_RevertWhen_SlashingOverMaxSlashPercentage
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\indexing\cancel.t.sol`

- Contracts: DisputeManagerIndexingCancelDisputeTest
- Tags: disputemanager, disputes, governor, token, dispute
- Functions: test_Indexing_Cancel_Dispute, test_Indexing_Cancel_RevertIf_CallerIsNotFisherman, test_Indexing_Cancel_RevertIf_DisputePeriodNotOver, test_Indexing_Cancel_After_DisputePeriodIncreased, test_Indexing_Cancel_After_DisputePeriodDecreased
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\indexing\create.t.sol`

- Contracts: DisputeManagerIndexingCreateDisputeTest
- Tags: delegation, disputemanager, disputes, staking, token, dispute
- Functions: test_Indexing_Create_Dispute, test_Indexing_Create_Dispute_WithDelegation, test_Indexing_Create_Dispute_RevertWhen_SubgraphServiceNotSet, test_Indexing_Create_MultipleDisputes, test_Indexing_Create_RevertWhen_DisputeAlreadyCreated, test_Indexing_Create_DisputesSamePOIAndAllo, test_Indexing_Create_RevertIf_DepositUnderMinimum, test_Indexing_Create_RevertIf_AllocationDoesNotExist, test_Indexing_Create_RevertIf_IndexerIsBelowStake, test_Indexing_Create_DontRevertIf_IndexerIsBelowStake_WithDelegation
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\indexing\draw.t.sol`

- Contracts: DisputeManagerIndexingDrawDisputeTest
- Tags: disputemanager, disputes, token, dispute
- Functions: test_Indexing_Draw_Dispute, test_Indexing_Draw_RevertIf_CallerIsNotArbitrator
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\indexing\reject.t.sol`

- Contracts: DisputeManagerIndexingRejectDisputeTest
- Tags: disputemanager, disputes, token, dispute
- Functions: test_Indexing_Reject_Dispute, test_Indexing_Reject_RevertIf_CallerIsNotArbitrator
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\indexingFee\create.t.sol`

- Contracts: DisputeManagerIndexingFeeCreateDisputeTest
- Tags: disputemanager, disputes, staking, token, dispute
- Functions: _setupCollectedAgreement, test_IndexingFee_Create_Dispute, test_IndexingFee_Create_Dispute_RevertWhen_NotCollected, test_IndexingFee_Create_Dispute_EmitsEvent, test_IndexingFee_Create_Dispute_RevertWhen_ZeroStake, test_IndexingFee_Create_Dispute_RevertWhen_AlreadyCreated, test_IndexingFee_Accept_Dispute_RevertWhen_InvalidDisputeId, test_IndexingFee_Accept_Dispute_RevertWhen_NotPending
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\query\accept.t.sol`

- Contracts: DisputeManagerQueryAcceptDisputeTest
- Tags: disputemanager, disputes, slashing, token, dispute
- Functions: test_Query_Accept_Dispute, test_Query_Accept_Dispute_RevertWhen_SubgraphServiceNotSet, test_Query_Accept_Dispute_OptParam, test_Query_Accept_RevertIf_CallerIsNotArbitrator, test_Query_Accept_RevertWhen_SlashingOverMaxSlashPercentage, test_Query_Accept_RevertWhen_UsingConflictAccept, test_Query_Accept_RevertWhen_SlashingOverMaxSlashPercentage_WithDelegation, test_Query_Accept_RevertWhen_SlashingOverMaxSlashPercentage_WithDelegation_DelegationSlashing, test_Query_Accept_Dispute_AfterFishermanRewardCutIncreased
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\query\cancel.t.sol`

- Contracts: DisputeManagerQueryCancelDisputeTest
- Tags: disputemanager, disputes, governor, token, dispute
- Functions: test_Query_Cancel_Dispute, test_Query_Cancel_RevertIf_CallerIsNotFisherman, test_Query_Cancel_RevertIf_DisputePeriodNotOver, test_Query_Cancel_After_DisputePeriodIncreased, test_Query_Cancel_After_DisputePeriodDecreased
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\query\create.t.sol`

- Contracts: DisputeManagerQueryCreateDisputeTest
- Tags: disputemanager, disputes, token, dispute
- Functions: test_Query_Create_Dispute_Only, test_Query_Create_Dispute_RevertWhen_SubgraphServiceNotSet, test_Query_Create_MultipleDisputes_DifferentFisherman, test_Query_Create_MultipleDisputes_DifferentIndexer, test_Query_Create_RevertIf_Duplicate, test_Query_Create_RevertIf_DepositUnderMinimum, test_Query_Create_RevertIf_AllocationDoesNotExist, test_Query_Create_RevertIf_IndexerIsBelowStake, test_Query_Create_RevertIf_InvalidAttestationLength, test_Query_Create_DontRevertIf_IndexerIsBelowStake_WithDelegation
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\query\draw.t.sol`

- Contracts: DisputeManagerQueryDrawDisputeTest
- Tags: disputemanager, disputes, token, dispute
- Functions: test_Query_Draw_Dispute, test_Query_Draw_RevertIf_CallerIsNotArbitrator
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\query\reject.t.sol`

- Contracts: DisputeManagerQueryRejectDisputeTest
- Tags: disputemanager, disputes, token, dispute
- Functions: test_Query_Reject_Dispute, test_Query_Reject_RevertIf_CallerIsNotArbitrator
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\queryConflict\accept.t.sol`

- Contracts: DisputeManagerQueryConflictAcceptDisputeTest
- Tags: disputemanager, disputes, slashing, token, dispute
- Functions: test_Query_Conflict_Accept_Dispute_Draw_Other, test_Query_Conflict_Accept_Dispute_Accept_Other, test_Query_Conflict_Accept_RevertIf_CallerIsNotArbitrator, test_Query_Conflict_Accept_RevertWhen_SlashingOverMaxSlashPercentage, test_Query_Conflict_Accept_AcceptRelated_DifferentIndexer, test_Query_Conflict_Accept_RevertWhen_UsingSingleAccept
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\queryConflict\cancel.t.sol`

- Contracts: DisputeManagerQueryConflictCancelDisputeTest
- Tags: disputemanager, disputes, governor, token, dispute
- Functions: test_Query_Conflict_Cancel_Dispute, test_Query_Conflict_Cancel_RevertIf_CallerIsNotFisherman, test_Query_Conflict_Cancel_RevertIf_DisputePeriodNotOver, test_Query_Conflict_Cancel_After_DisputePeriodIncreased, test_Query_Cancel_After_DisputePeriodDecreased
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\queryConflict\create.t.sol`

- Contracts: DisputeManagerQueryConflictCreateDisputeTest
- Tags: disputemanager, disputes, token, dispute
- Functions: test_Query_Conflict_Create_DisputeAttestation, test_Query_Conflict_Create_DisputeAttestationDifferentIndexers, test_Query_Conflict_Create_RevertIf_AttestationsResponsesAreTheSame, test_Query_Conflict_Create_RevertIf_AttestationsHaveDifferentSubgraph
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\queryConflict\draw.t.sol`

- Contracts: DisputeManagerQueryConflictDrawDisputeTest
- Tags: disputemanager, disputes, token, dispute
- Functions: test_Query_Conflict_Draw_Dispute, test_Query_Conflict_Draw_RevertIf_CallerIsNotArbitrator
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\disputes\queryConflict\reject.t.sol`

- Contracts: DisputeManagerQueryConflictRejectDisputeTest
- Tags: disputemanager, disputes, token, dispute
- Functions: test_Query_Conflict_Reject_Revert
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\governance\arbitrator.t.sol`

- Contracts: DisputeManagerGovernanceArbitratorTest
- Tags: disputemanager, governance, governor, dispute
- Functions: test_Governance_SetArbitrator, test_Governance_RevertWhen_ZeroAddress, test_Governance_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\governance\disputeDeposit.t.sol`

- Contracts: DisputeManagerGovernanceDisputeDepositTest
- Tags: disputemanager, governance, governor, dispute
- Functions: test_Governance_SetDisputeDeposit, test_Governance_RevertWhen_DepositTooLow, test_Governance_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\governance\fishermanRewardCut.t.sol`

- Contracts: DisputeManagerGovernanceFishermanRewardCutTest
- Tags: disputemanager, governance, governor, dispute
- Functions: test_Governance_SetFishermanRewardCut, test_Governance_RevertWhen_OverMaximumValue, test_Governance_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\governance\maxSlashingCut.t.sol`

- Contracts: DisputeManagerGovernanceMaxSlashingCutTest
- Tags: disputemanager, governance, governor, slashing, dispute
- Functions: test_Governance_SetMaxSlashingCut, test_Governance_RevertWhen_NotPPM, test_Governance_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\disputeManager\governance\subgraphService.t.sol`

- Contracts: DisputeManagerGovernanceSubgraphService
- Tags: disputemanager, governance, governor, dispute
- Functions: test_Governance_SetSubgraphService, test_Governance_SetSubgraphService_RevertWhenZero
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\libraries\AllocationLibrary.t.sol`

- Contracts: AllocationLibraryTest
- Tags: rewards
- Functions: setUp, test_Allocation_PresentPOI_RevertWhen_Closed, test_Allocation_ClearPendingRewards_RevertWhen_Closed, test_Allocation_Close_RevertWhen_AlreadyClosed, test_Allocation_Get_RevertWhen_NotExists
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\mocks\AllocationHarness.sol`

- Contracts: AllocationHarness
- Tags: rewards, token
- Functions: create, presentPOI, clearPendingRewards, close, get
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\mocks\MockCuration.sol`

- Contracts: MockCuration
- Tags: curation
- Functions: isCurated, collect
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\mocks\MockGRTToken.sol`

- Contracts: MockGRTToken
- Tags: graphtoken, token
- Functions: burn, burnFrom, mint, addMinter, removeMinter, renounceMinter, isMinter, permit, increaseAllowance, decreaseAllowance
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\mocks\MockRewardsManager.sol`

- Contracts: MockRewardsManager
- Tags: rewards, rewardsmanager, token
- Functions: setIssuancePerBlock, setMinimumSubgraphSignal, setSubgraphService, setSubgraphAvailabilityOracle, setDenied, setDeniedMany, isDenied, setSubgraphDeniedReclaimAddress, setIndexerEligibilityReclaimAddress, setReclaimAddress, setDefaultReclaimAddress, setRevertOnIneligible, getRevertOnIneligible, reclaimRewards, getIssuanceAllocator, getReclaimAddress, getDefaultReclaimAddress, getNewRewardsPerSignal, getAccRewardsPerSignal, getAccRewardsForSubgraph, getAccRewardsPerAllocatedToken, getRewards, calcRewards, getAllocatedIssuancePerBlock, getRawIssuancePerBlock
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\shared\HorizonStakingShared.t.sol`

- Contracts: HorizonStakingSharedTest
- Tags: delegation, slashing, staking, token, dispute
- Functions: _provision, _createProvision, _addToProvision, _removeFromProvision, _delegate, _undelegate, _setDelegationFeeCut, _thawDeprovisionAndUnstake, _setProvisionParameters, _stakeTo, _stake
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\shared\SubgraphServiceShared.t.sol`

- Contracts: SubgraphServiceSharedTest
- Tags: delegation, rewards, rewardsmanager, staking, token, dispute
- Functions: setUp, _register, _startService, _stopService, _createSubgraphAllocationData, _delegate, _calculateStakeSnapshot, _getIndexer
- Modifiers: useIndexer, useAllocation, useDelegation
- Events: none

## `packages\subgraph-service\test\unit\SubgraphBaseTest.t.sol`

- Contracts: SubgraphBaseTest
- Tags: curation, disputemanager, escrow, governance, governor, rewards, rewardsmanager, staking, token, dispute
- Functions: setUp, deployProtocolContracts, setupProtocol, unpauseProtocol, createUser, mint, burn
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\allocation\forceClose.t.sol`

- Contracts: SubgraphServiceAllocationForceCloseTest
- Tags: permission, rewards, token, dispute
- Functions: test_SubgraphService_Allocation_ForceClose_Stale, test_SubgraphService_Allocation_ForceClose_Stale_AfterCollecting, test_SubgraphService_Allocation_ForceClose_RevertIf_NotStale, test_SubgraphService_Allocation_ForceClose_RevertIf_Altruistic, test_SubgraphService_Allocation_ForceClose_RevertIf_Paused
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\allocation\overDelegated.t.sol`

- Contracts: SubgraphServiceAllocationOverDelegatedTest
- Tags: delegation, staking, token, dispute
- Functions: test_SubgraphService_Allocation_OverDelegated_NotOverAllocatedAfterUndelegation
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\allocation\resize.t.sol`

- Contracts: SubgraphServiceAllocationResizeTest
- Tags: rewards, token
- Functions: test_SubgraphService_Allocation_Resize, test_SubgraphService_Allocation_Resize_AfterCollectingIndexingRewards, test_SubgraphService_Allocation_Resize_SecondTime, test_SubgraphService_Allocation_Resize_RevertWhen_NotAuthorized, test_SubgraphService_Allocation_Resize_RevertWhen_SameSize, test_SubgraphService_Allocation_Resize_RevertIf_AllocationIsClosed, test_SubgraphService_Allocation_Resize_StaleAllocation_ReclaimsPending, test_SubgraphService_Allocation_Resize_NotStale_PreservesPending
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\allocation\start.t.sol`

- Contracts: SubgraphServiceAllocationStartTest
- Tags: token, dispute
- Functions: test_SubgraphService_Allocation_Start, test_SubgraphService_Allocation_Start_AllowsZeroTokens, test_SubgraphService_Allocation_Start_ByOperator, test_SubgraphService_Allocation_Start_RevertWhen_NotAuthorized, test_SubgraphService_Allocation_Start_RevertWhen_NoValidProvision, test_SubgraphService_Allocation_Start_RevertWhen_NotRegistered, test_SubgraphService_Allocation_Start_RevertWhen_ZeroAllocationId, test_SubgraphService_Allocation_Start_RevertWhen_InvalidSignature, test_SubgraphService_Allocation_Start_RevertWhen_InvalidData, test_SubgraphService_Allocation_Start_RevertWhen_AlreadyExists_SubgraphService, test_SubgraphService_Allocation_Start_RevertWhen_AlreadyExists_Migrated, test_SubgraphService_Allocation_Start_RevertWhen_AlreadyExists_Staking, test_SubgraphService_Allocation_Start_RevertWhen_NotEnoughTokens, _generateData, _generateRandomHexBytes
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\allocation\stop.t.sol`

- Contracts: SubgraphServiceAllocationStopTest
- Tags: token
- Functions: test_SubgraphService_Allocation_Stop, test_SubgraphService_Allocation_Stop_RevertWhen_IndexerIsNotTheAllocationOwner, test_SubgraphService_Allocation_Stop_RevertWhen_NotAuthorized, test_SubgraphService_Allocation_Stop_RevertWhen_NotRegistered, test_SubgraphService_Allocation_Stop_RevertWhen_NotOpen
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\collect\collect.t.sol`

- Contracts: SubgraphServiceCollectTest
- Tags: token
- Functions: test_SubgraphService_Collect_RevertWhen_InvalidPayment
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\collect\indexing\indexing.t.sol`

- Contracts: SubgraphServiceCollectIndexingTest
- Tags: delegation, rewards, rewardsmanager, staking, token
- Functions: test_SubgraphService_Collect_Indexing, test_SubgraphService_Collect_Indexing_WithDelegation, test_SubgraphService_Collect_Indexing_AfterUndelegate, test_SubgraphService_Collect_Indexing_RewardsDestination, test_subgraphService_Collect_Indexing_MultipleOverTime, test_subgraphService_Collect_Indexing_MultipleOverTime_WithDelegation, test_SubgraphService_Collect_Indexing_OverAllocated, test_SubgraphService_Collect_Indexing_RevertWhen_IndexerIsNotAllocationOwner, test_SubgraphService_Collect_Indexing_ZeroRewards, test_SubgraphService_Collect_Indexing_ZeroPOI, test_SubgraphService_Collect_Indexing_StalePOI, test_SubgraphService_Collect_Indexing_DeniedSubgraph, test_SubgraphService_Collect_Indexing_AltruisticAllocation, test_SubgraphService_Collect_Indexing_RevertWhen_AllocationClosed
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\collect\query\query.t.sol`

- Contracts: SubgraphServiceRegisterTest
- Tags: escrow, token
- Functions: _getSignerProof, _getQueryFeeEncodedData, _getRav, _deposit, _authorizeSigner, setUp, testCollect_QueryFees, testCollect_QueryFees_WithRewardsDestination, testCollect_MultipleQueryFees, testCollect_RevertWhen_NotAuthorized, testCollect_QueryFees_RevertWhen_IndexerIsNotAllocationOwner, testCollect_QueryFees_RevertWhen_CollectingOtherIndexersFees, testCollect_QueryFees_RevertWhen_CollectionIdTooLarge, testCollect_QueryFees_PartialCollect
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\getters.t.sol`

- Contracts: SubgraphServiceGettersTest
- Tags: curation, disputemanager, rewards, token, dispute
- Functions: test_GetDisputeManager, test_GetGraphTallyCollector, test_GetCuration, test_GetRecurringCollector, test_GetAllocationData, test_GetAllocationData_NonExistent, test_GetProvisionTokensRange, test_GetThawingPeriodRange, test_GetVerifierCutRange
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\governance\blockClosingAllocationWithActiveAgreement.t.sol`

- Contracts: SubgraphServiceGovernanceBlockClosingAllocationTest
- Tags: governance, governor
- Functions: test_Governance_SetBlockClosingAllocationWithActiveAgreement_Enable, test_Governance_SetBlockClosingAllocationWithActiveAgreement_Disable, test_Governance_SetBlockClosingAllocationWithActiveAgreement_NoopWhenSameValue, test_Governance_SetBlockClosingAllocationWithActiveAgreement_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\governance\curationCut.t.sol`

- Contracts: SubgraphServiceGovernanceCurationCutTest
- Tags: curation, governance, governor
- Functions: test_Governance_SetCurationCut, test_Governance_SetCurationCut_RevertWhen_InvalidPPM, test_Governance_SetCurationCut_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\governance\indexingFeesCut.t.sol`

- Contracts: SubgraphServiceGovernanceIndexingFeesCutTest
- Tags: governance, governor
- Functions: test_Governance_SetIndexingFeesCut, test_Governance_SetIndexingFeesCut_RevertWhen_InvalidPPM, test_Governance_SetIndexingFeesCut_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\governance\maxPOIStaleness.t.sol`

- Contracts: SubgraphServiceGovernanceMaxPOIStalenessTest
- Tags: governance, governor
- Functions: test_Governance_SetMaxPOIStaleness, test_Governance_SetMaxPOIStaleness_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\governance\pause.t.sol`

- Contracts: SubgraphServiceGovernancePauseTest
- Tags: governance
- Functions: test_Governance_Pause, test_Governance_Unpause, test_Governance_Pause_RevertWhen_NotPauseGuardian, test_Governance_Unpause_RevertWhen_NotPauseGuardian, test_Governance_Pause_RevertWhen_AlreadyPaused, test_Governance_Unpause_RevertWhen_NotPaused
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\governance\pauseGuardian.t.sol`

- Contracts: SubgraphServiceGovernancePauseGuardianTest
- Tags: governance, governor
- Functions: test_Governance_SetPauseGuardian, test_Governance_SetPauseGuardian_Remove, test_Governance_SetPauseGuardian_RevertWhen_NoChange, test_Governance_SetPauseGuardian_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\governance\provisionParameters.t.sol`

- Contracts: SubgraphServiceGovernanceProvisionParametersTest
- Tags: delegation, governance, governor, token
- Functions: test_Governance_SetMinimumProvisionTokens, test_Governance_SetMinimumProvisionTokens_RevertWhen_NotGovernor, test_Governance_SetDelegationRatio, test_Governance_SetDelegationRatio_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\governance\stakeToFeesRatio.t.sol`

- Contracts: DisputeManagerGovernanceArbitratorTest
- Tags: disputemanager, governance, governor, dispute
- Functions: _setStakeToFeesRatio, test_Governance_SetStakeToFeesRatio, test_Governance_RevertWhen_ZeroValue, test_Governance_RevertWhen_NotGovernor
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\indexing-agreement\accept.t.sol`

- Contracts: SubgraphServiceIndexingAgreementAcceptTest
- Tags: token, dispute
- Functions: test_SubgraphService_AcceptIndexingAgreement_Revert_WhenPaused, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenNotAuthorized, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenInvalidProvision, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenIndexerNotRegistered, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenNotDataService, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenInvalidMetadata, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenInvalidAllocation, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenAllocationNotAuthorized, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenAllocationClosed, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenDeploymentIdMismatch, test_SubgraphService_AcceptIndexingAgreement_Idempotent_WhenAlreadyAcceptedSameAllocation, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenAgreementAlreadyAllocated, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenInvalidTermsData, test_SubgraphService_AcceptIndexingAgreement_Revert_WhenTermsExceedRCALimit, test_SubgraphService_AcceptIndexingAgreement, test_SubgraphService_AcceptIndexingAgreement_Rebinds_WhenDifferentAllocation, test_SubgraphService_AcceptIndexingAgreement_Rebinds_AfterRcaDeadline
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\indexing-agreement\base.t.sol`

- Contracts: SubgraphServiceIndexingAgreementBaseTest
- Tags: staking, token, dispute
- Functions: test_SubgraphService_GetIndexingAgreement, test_SubgraphService_Revert_WhenUnsafeAddress_WhenProxyAdmin, test_SubgraphService_Revert_WhenUnsafeAddress_WhenGraphProxyAdmin
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\indexing-agreement\collect.t.sol`

- Contracts: SubgraphServiceIndexingAgreementCollectTest
- Tags: token
- Functions: test_SubgraphService_CollectIndexingFees_OK, test_SubgraphService_CollectIndexingFees_Revert_WhenPaused, test_SubgraphService_CollectIndexingFees_Revert_WhenNotAuthorized, test_SubgraphService_CollectIndexingFees_Revert_WhenInvalidProvision, test_SubgraphService_CollectIndexingFees_Revert_WhenIndexerNotRegistered, test_SubgraphService_CollectIndexingFees_Revert_WhenInvalidData, test_SubgraphService_CollectIndexingFees_Revert_WhenInvalidAgreement, test_SubgraphService_CollectIndexingFees_Reverts_WhenInvalidNestedData, test_SubgraphService_CollectIndexingFees_Reverts_WhenIndexingAgreementNotAuthorized, test_SubgraphService_CollectIndexingFees_Reverts_WhenStopService, test_SubgraphService_CollectIndexingFees_AfterCloseStaleAllocation_ResizesToZero, test_SubgraphService_CollectIndexingFees_Revert_WhenNotCollectable, _expectCollectCallAndEmit
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\indexing-agreement\integration.t.sol`

- Contracts: SubgraphServiceIndexingAgreementIntegrationTest
- Tags: escrow, token
- Functions: test_SubgraphService_CollectIndexingFee_Integration, test_SubgraphService_CollectIndexingFee_WhenCanceledByPayer_Integration, test_SubgraphService_ScopedCancelActive_ViaRecurringCollector_Integration, test_SubgraphService_ScopedCancelActive_PayerEqualsProxyAdmin_Regression, test_SubgraphService_CollectIndexingRewards_ResizesToZeroWhenOverAllocated_Integration, _sharedSetup, _newExpectedTokens, _sharedAssert, _addTokensToProvision, _removeTokensFromProvision, _setupPayerWithEscrow, _escrow, _getState
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\indexing-agreement\shared.t.sol`

- Contracts: SubgraphServiceIndexingAgreementSharedTest
- Tags: token
- Functions: setUp, _subgraphServiceSafePrank, _stopOrResetPrank, _cancelAgreement, _withIndexer, _setupIndexer, _withAcceptedIndexingAgreement, _newCtx, _generateAcceptableSignedRCA, _generateAcceptableRecurringCollectionAgreement, _generateAcceptableSignedRCAU, _generateAcceptableRecurringCollectionAgreementUpdate, _requireIndexer, _getIndexer, _isTestUser, _isSafeSubgraphServiceCaller, _transparentUpgradeableProxyAdmin, _newAcceptIndexingAgreementMetadataV1, _newAcceptIndexingAgreementMetadataV1Terms, _newUpdateIndexingAgreementMetadataV1, _encodeCollectDataV1, _encodeCollectData, _encodeV1Data, _encodeAcceptIndexingAgreementMetadataV1, _encodeUpdateIndexingAgreementMetadataV1
- Modifiers: withSafeIndexerOrOperator
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\indexing-agreement\update.t.sol`

- Contracts: SubgraphServiceIndexingAgreementUpgradeTest
- Tags: token, dispute
- Functions: test_SubgraphService_UpdateIndexingAgreementIndexingAgreement_Revert_WhenPaused, test_SubgraphService_UpdateIndexingAgreement_Revert_WhenNotAuthorized, test_SubgraphService_UpdateIndexingAgreement_Revert_WhenInvalidProvision, test_SubgraphService_UpdateIndexingAgreement_Revert_WhenIndexerNotRegistered, test_SubgraphService_UpdateIndexingAgreement_Revert_WhenNotAccepted, test_SubgraphService_UpdateIndexingAgreement_Revert_WhenNotAuthorizedForAgreement, test_SubgraphService_UpdateIndexingAgreement_Revert_WhenInvalidMetadata, test_SubgraphService_UpdateIndexingAgreement_Revert_WhenTermsExceedRCALimit, test_SubgraphService_UpdateIndexingAgreement_OK, test_SubgraphService_UpdateIndexingAgreement_Idempotent_WhenAlreadyAtActiveHash
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\provider\register.t.sol`

- Contracts: SubgraphServiceProviderRegisterTest
- Tags: rewards, token, dispute
- Functions: test_SubgraphService_Provider_Register, test_SubgraphService_Provider_Register_MultipleTimes, test_SubgraphService_Provider_Register_RevertWhen_InvalidProvision, test_SubgraphService_Provider_Register_RevertWhen_NotAuthorized, test_SubgraphService_Provider_Register_RevertWhen_InvalidProvisionValues, test_SubgraphService_Provider_Register_RevertIf_EmptyUrl, test_SubgraphService_Provider_Register_RevertIf_EmptyGeohash
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\provider\rewardsDestination.t.sol`

- Contracts: SubgraphServiceProviderRewardsDestinationTest
- Tags: rewards, token
- Functions: test_SubgraphService_Provider_RewardsDestination_Set
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\provision\accept.t.sol`

- Contracts: SubgraphServiceProvisionAcceptTest
- Tags: disputemanager, governor, token, dispute
- Functions: test_SubgraphService_Provision_Accept, test_SubgraphService_Provision_Accept_When_NotRegistered, test_SubgraphService_Provision_Accept_RevertWhen_NotAuthorized, test_SubgraphService_Provision_Accept_RevertIf_InvalidVerifierCut, test_SubgraphService_Provision_Accept_RevertIf_InvalidDisputePeriod
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\slash.t.sol`

- Contracts: SubgraphServiceSlashTest
- Tags: disputemanager, staking, token, dispute
- Functions: test_SubgraphService_Slash, test_SubgraphService_Slash_ZeroReward, test_SubgraphService_Slash_RevertWhen_RewardExceedsMax, test_SubgraphService_Slash_RevertWhen_NotDisputeManager
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\SubgraphService.t.sol`

- Contracts: SubgraphServiceTest
- Tags: governor, rewards, staking
- Functions: setUp, _setRewardsDestination, _acceptProvision, _resizeAllocation, _closeStaleAllocation, _collect, _collectPaymentData, _handleQueryFeeCollection, _queryFeeData, _handleIndexingRewardsCollection, _verifyQueryFeeCollection, _verifyIndexingRewardsCollection, _migrateLegacyAllocation, _setLegacyAllocationInStaking, _createAndStartAllocation, _recoverRavSigner, _getClaimList, _buildStakeClaimId, _getStakeClaim, _getHardcodedPoiMetadata
- Modifiers: useGovernor, useOperator, useRewardsDestination
- Events: none

## `packages\subgraph-service\test\unit\utils\Constants.sol`

- Contracts: Constants
- Tags: curation, delegation, escrow, rewards, slashing, staking, token, dispute
- Functions: none
- Modifiers: none
- Events: none

## `packages\testing\test\gas\CallbackGas.t.sol`

- Contracts: CallbackGasTest
- Tags: escrow, graphtoken, staking, token
- Functions: test_BeforeCollection_GasWithinBudget_JitDeposit, test_BeforeCollection_GasWithinBudget_EscrowSufficient, test_AfterCollection_GasWithinBudget_FullReconcile, test_BeforeCollection_GasWithinBudget_ColdDiscoveryJit, test_AfterCollection_GasWithinBudget_WithdrawAndDeposit, test_AfterCollection_GasWithinBudget_DeletionCascade
- Modifiers: none
- Events: none

## `packages\testing\test\harness\FullStackHarness.t.sol`

- Contracts: FullStackHarness
- Tags: curation, delegation, disputemanager, escrow, governance, graphtoken, rewards, rewardsmanager, staking, token, dispute
- Functions: setUp, _deployProtocol, _deployRAMStack, _configureProtocol, _setupIndexer, _buildRCA, _buildRCAEx, _addProvisionTokens, _ramOffer, _ssAccept, _offerAndAccept, _collectIndexingFees, _mintTokens, resetPrank
- Modifiers: none
- Events: none

## `packages\testing\test\harness\RealStackHarness.t.sol`

- Contracts: RealStackHarness
- Tags: escrow, governor, graphtoken, registry, staking, token
- Functions: setUp, _makeRCA, _offerAgreement, _offerAndAccept, _setUpProvider
- Modifiers: none
- Events: none

## `packages\testing\test\integration\AgreementLifecycle.t.sol`

- Contracts: AgreementLifecycleTest
- Tags: escrow, token
- Functions: setUp, test_Scenario1_OfferAcceptCollectReconcile, test_Scenario2_UpdateFlow, test_Scenario3_CancelByIndexerAndCleanup, test_Scenario4_ScopedCancelByPayer, test_Scenario5_JITTopUp
- Modifiers: none
- Events: none

## `packages\testing\test\integration\AgreementLifecycleAdvanced.t.sol`

- Contracts: AgreementLifecycleAdvancedTest, MockEligibilityOracle
- Tags: escrow, rewards, staking, token
- Functions: setUp, test_Scenario11_RewardsAndFeesCoexist, test_Scenario12_RewardDenialFeesContinue, test_Scenario6_EscrowBasisTransitions, test_Scenario10_StakeLocking, test_Scenario7_MultiAgreementIsolation, test_Scenario8_ExpiredOfferCleanup, test_Scenario9_EligibilityCheck_Eligible, test_Scenario9_EligibilityCheck_NotEligible, test_Scenario13_CloseAllocationCancelsAgreement, test_Scenario13_CloseAllocationBlockedByActiveAgreement, test_Scenario14_CancelWithBelowMinimumProvision, test_Scenario15_RebindAfterCancellation_Reverts, _getHardcodedPoiMetadata, _openSecondAllocationForIndexer, setEligible, isEligible, supportsInterface
- Modifiers: none
- Events: none

## `packages\testing\test\mocks\ControllerStub.sol`

- Contracts: ControllerStub
- Tags: governance, governor, registry
- Functions: register, getContractProxy, getGovernor, paused, partialPaused, setContractProxy, unsetContractProxy, updateController, setPartialPaused, setPaused, setPauseGuardian
- Modifiers: none
- Events: none

## `packages\testing\test\mocks\GraphTokenMock.sol`

- Contracts: GraphTokenMock
- Tags: graphtoken, token
- Functions: mint, burnFrom
- Modifiers: none
- Events: none

## `packages\testing\test\mocks\HorizonStakingStub.sol`

- Contracts: HorizonStakingStub
- Tags: staking, token
- Functions: setProvision, getProvision, getProviderTokensAvailable, isAuthorized
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\GraphTokenDistributor.sol`

- Contracts: GraphTokenDistributor
- Tags: graphtoken, token
- Functions: deposit, addBeneficiaryTokens, addBeneficiaryTokensMulti, subBeneficiaryTokens, subBeneficiaryTokensMulti, _setBeneficiaryTokens, setLocked, withdraw, claim, claimTo
- Modifiers: whenNotLocked
- Events: BeneficiaryUpdated, TokensDeposited, TokensWithdrawn, TokensClaimed, LockUpdated

## `packages\token-distribution\contracts\GraphTokenLock.sol`

- Contracts: GraphTokenLock
- Tags: graphtoken, token, vesting
- Functions: _initialize, changeBeneficiary, acceptLock, cancelLock, currentBalance, currentTime, duration, sinceStartTime, amountPerPeriod, periodDuration, currentPeriod, passedPeriods, availableAmount, vestedAmount, releasableAmount, totalOutstandingAmount, surplusAmount, release, withdrawSurplus, revoke
- Modifiers: onlyBeneficiary
- Events: TokensReleased, TokensWithdrawn, TokensRevoked, BeneficiaryChanged, LockAccepted, LockCanceled

## `packages\token-distribution\contracts\GraphTokenLockManager.sol`

- Contracts: GraphTokenLockManager
- Tags: graphtoken, graphtokenlockwallet, token, vesting
- Functions: setMasterCopy, createTokenLockWallet, token, deposit, withdraw, addTokenDestination, removeTokenDestination, isTokenDestination, getTokenDestinations, setAuthFunctionCall, unsetAuthFunctionCall, setAuthFunctionCallMany, _setAuthFunctionCall, getAuthFunctionCallTarget, isAuthFunctionCall, _toFunctionSigHash, _convertToBytes4
- Modifiers: none
- Events: MasterCopyUpdated, TokenLockCreated, TokensDeposited, TokensWithdrawn, FunctionCallAuth, TokenDestinationAllowed

## `packages\token-distribution\contracts\GraphTokenLockSimple.sol`

- Contracts: GraphTokenLockSimple
- Tags: graphtoken, token, vesting
- Functions: initialize
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\GraphTokenLockWallet.sol`

- Contracts: GraphTokenLockWallet
- Tags: graphtoken, graphtokenlockwallet, token, vesting
- Functions: initialize, setManager, _setManager, approveProtocol, revokeProtocol
- Modifiers: none
- Events: ManagerUpdated, TokenDestinationsApproved, TokenDestinationsRevoked

## `packages\token-distribution\contracts\IGraphTokenLock.sol`

- Contracts: IGraphTokenLock
- Tags: graphtoken, token
- Functions: currentBalance, currentTime, duration, sinceStartTime, amountPerPeriod, periodDuration, currentPeriod, passedPeriods, availableAmount, vestedAmount, releasableAmount, totalOutstandingAmount, surplusAmount, release, withdrawSurplus, revoke
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\IGraphTokenLockManager.sol`

- Contracts: IGraphTokenLockManager
- Tags: graphtoken, token, vesting
- Functions: setMasterCopy, createTokenLockWallet, token, deposit, withdraw, addTokenDestination, removeTokenDestination, isTokenDestination, getTokenDestinations, setAuthFunctionCall, unsetAuthFunctionCall, setAuthFunctionCallMany, getAuthFunctionCallTarget, isAuthFunctionCall
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\L1GraphTokenLockTransferTool.sol`

- Contracts: L1GraphTokenLockTransferTool
- Tags: graphtoken, graphtokenlockwallet, staking, token, vesting
- Functions: initialize, setL2LockManager, setL2WalletOwner, depositETH, withdrawETH, pullETH, depositToL2Locked, setL2WalletAddressManually
- Modifiers: none
- Events: L2LockManagerSet, L2WalletOwnerSet, LockedFundsSentToL2, L2WalletAddressSet, ETHDeposited, ETHWithdrawn, ETHPulled, L2BeneficiarySet

## `packages\token-distribution\contracts\L2GraphTokenLockManager.sol`

- Contracts: L2GraphTokenLockManager
- Tags: bridge, graphtoken, graphtokenlockwallet, token, vesting
- Functions: onTokenTransfer, _deployFromL1, _encodeInitializer
- Modifiers: onlyL2Gateway
- Events: TokenLockCreatedFromL1, LockedTokensReceivedFromL1

## `packages\token-distribution\contracts\L2GraphTokenLockTransferTool.sol`

- Contracts: L2GraphTokenLockTransferTool
- Tags: graphtoken, graphtokenlockwallet, token
- Functions: withdrawToL1Locked
- Modifiers: none
- Events: LockedFundsSentToL1

## `packages\token-distribution\contracts\L2GraphTokenLockWallet.sol`

- Contracts: L2GraphTokenLockWallet
- Tags: graphtoken, graphtokenlockwallet, token, vesting
- Functions: initializeFromL1
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\MathUtils.sol`

- Contracts: MathUtils
- Tags: token
- Functions: min
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\MinimalProxyFactory.sol`

- Contracts: MinimalProxyFactory
- Tags: token
- Functions: getDeploymentAddress, getDeploymentAddress, _deployProxy2, _getContractCreationCode
- Modifiers: none
- Events: ProxyCreated

## `packages\token-distribution\contracts\Ownable.sol`

- Contracts: Ownable
- Tags: token
- Functions: _initialize, owner, renounceOwnership, transferOwnership
- Modifiers: onlyOwner
- Events: OwnershipTransferred

## `packages\token-distribution\contracts\tests\arbitrum\AddressAliasHelper.sol`

- Contracts: AddressAliasHelper
- Tags: bridge, permission, token
- Functions: applyL1ToL2Alias, undoL1ToL2Alias
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\tests\arbitrum\IBridge.sol`

- Contracts: IBridge
- Tags: bridge, permission, token
- Functions: deliverMessageToInbox, executeCall, setInbox, setOutbox, activeOutbox, allowedInboxes, allowedOutboxes, inboxAccs, messageCount
- Modifiers: none
- Events: MessageDelivered, BridgeCallTriggered, InboxToggle, OutboxToggle

## `packages\token-distribution\contracts\tests\arbitrum\IInbox.sol`

- Contracts: IInbox
- Tags: bridge, permission, token
- Functions: sendL2Message, sendUnsignedTransaction, sendContractTransaction, sendL1FundedUnsignedTransaction, sendL1FundedContractTransaction, createRetryableTicket, depositEth, bridge, pauseCreateRetryables, unpauseCreateRetryables, startRewriteAddress, stopRewriteAddress
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\tests\arbitrum\IMessageProvider.sol`

- Contracts: IMessageProvider
- Tags: bridge, permission, token
- Functions: none
- Modifiers: none
- Events: InboxMessageDelivered, InboxMessageDeliveredFromOrigin

## `packages\token-distribution\contracts\tests\BridgeMock.sol`

- Contracts: BridgeMock
- Tags: bridge, token
- Functions: deliverMessageToInbox, executeCall, setInbox, setOutbox, activeOutbox, allowedInboxes, allowedOutboxes, messageCount
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\tests\GraphTokenMock.sol`

- Contracts: GraphTokenMock
- Tags: bridge, graphtoken, token
- Functions: bridgeMint, bridgeBurn
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\tests\InboxMock.sol`

- Contracts: InboxMock
- Tags: bridge, token
- Functions: sendL2Message, setBridge, sendUnsignedTransaction, sendContractTransaction, sendL1FundedUnsignedTransaction, sendL1FundedContractTransaction, createRetryableTicket, depositEth, pauseCreateRetryables, unpauseCreateRetryables, startRewriteAddress, stopRewriteAddress, _deliverMessage, deliverToBridge
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\tests\L1TokenGatewayMock.sol`

- Contracts: L1TokenGatewayMock
- Tags: escrow, graphtoken, token
- Functions: outboundTransfer, finalizeInboundTransfer, getOutboundCalldata, _parseOutboundData
- Modifiers: none
- Events: FakeTxToL2, DepositInitiated

## `packages\token-distribution\contracts\tests\L2TokenGatewayMock.sol`

- Contracts: L2TokenGatewayMock
- Tags: bridge, escrow, graphtoken, token
- Functions: outboundTransfer, finalizeInboundTransfer, calculateL2TokenAddress, getOutboundCalldata, _parseOutboundData
- Modifiers: none
- Events: FakeTxToL1, DepositFinalized, WithdrawalInitiated

## `packages\token-distribution\contracts\tests\Stakes.sol`

- Contracts: Stakes
- Tags: token
- Functions: deposit, release, allocate, unallocate, lockTokens, unlockTokens, withdrawTokens, getLockingPeriod, hasTokens, tokensUsed, tokensSecureStake, tokensAvailable, tokensAvailableWithDelegation, tokensWithdrawable
- Modifiers: none
- Events: none

## `packages\token-distribution\contracts\tests\StakingMock.sol`

- Contracts: StakingMock
- Tags: staking, token
- Functions: stake, stakeTo, unstake, withdraw, _stake, _withdraw
- Modifiers: none
- Events: StakeDeposited, StakeLocked, StakeWithdrawn

## `packages\token-distribution\contracts\tests\WalletMock.sol`

- Contracts: WalletMock
- Tags: token
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\base\Multicall.sol`

- Contracts: Multicall
- Tags: none
- Functions: multicall
- Modifiers: none
- Events: none

## `packages\contracts\contracts\l2\discovery\L2GNSStorage.sol`

- Contracts: L2GNSV1Storage
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\contracts\contracts\libraries\Base58Encoder.sol`

- Contracts: Base58Encoder
- Tags: none
- Functions: encode, truncate, reverse, toAlphabet
- Modifiers: none
- Events: none

## `packages\contracts\contracts\libraries\HexStrings.sol`

- Contracts: HexStrings
- Tags: none
- Functions: toString, toHexString
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\ens\IPublicResolver.sol`

- Contracts: IPublicResolver
- Tags: none
- Functions: text, setText
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\ens\ITestRegistrar.sol`

- Contracts: ITestRegistrar
- Tags: none
- Functions: register
- Modifiers: none
- Events: none

## `packages\contracts\contracts\tests\MockERC165.sol`

- Contracts: MockERC165
- Tags: none
- Functions: supportsInterface
- Modifiers: none
- Events: none

## `packages\contracts\contracts\upgrades\GraphProxy.sol`

- Contracts: GraphProxy
- Tags: none
- Functions: admin, implementation, pendingImplementation, setAdmin, upgradeTo, acceptUpgrade, acceptUpgradeAndCall, _acceptUpgrade, _fallback
- Modifiers: ifAdmin, ifAdminOrPendingImpl
- Events: none

## `packages\contracts\contracts\upgrades\GraphProxyStorage.sol`

- Contracts: GraphProxyStorage
- Tags: none
- Functions: _getAdmin, _setAdmin, _getImplementation, _getPendingImplementation, _setImplementation, _setPendingImplementation
- Modifiers: onlyAdmin
- Events: PendingImplementationUpdated, ImplementationUpdated, AdminUpdated

## `packages\contracts\contracts\upgrades\GraphUpgradeable.sol`

- Contracts: GraphUpgradeable
- Tags: none
- Functions: _implementation, acceptProxy, acceptProxyAndCall
- Modifiers: onlyProxyAdmin, onlyImpl
- Events: none

## `packages\data-edge\contracts\DataEdge.sol`

- Contracts: DataEdge
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\data-edge\contracts\EventfulDataEdge.sol`

- Contracts: EventfulDataEdge
- Tags: none
- Functions: none
- Modifiers: none
- Events: Log

## `packages\horizon\contracts\data-service\DataServiceStorage.sol`

- Contracts: DataServiceV1Storage
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\horizon\contracts\data-service\extensions\DataServicePausable.sol`

- Contracts: DataServicePausable
- Tags: none
- Functions: pause, unpause, _setPauseGuardian
- Modifiers: onlyPauseGuardian
- Events: none

## `packages\horizon\contracts\data-service\extensions\DataServicePausableUpgradeable.sol`

- Contracts: DataServicePausableUpgradeable
- Tags: none
- Functions: pause, unpause, __DataServicePausable_init, __DataServicePausable_init_unchained, _setPauseGuardian
- Modifiers: onlyPauseGuardian
- Events: none

## `packages\horizon\contracts\libraries\LinkedList.sol`

- Contracts: LinkedList
- Tags: none
- Functions: addTail, removeHead, traverse
- Modifiers: none
- Events: none

## `packages\horizon\contracts\libraries\PPMMath.sol`

- Contracts: PPMMath
- Tags: none
- Functions: mulPPM, mulPPMRoundUp, isValidPPM
- Modifiers: none
- Events: none

## `packages\horizon\contracts\libraries\UintRange.sol`

- Contracts: UintRange
- Tags: none
- Functions: isInRange
- Modifiers: none
- Events: none

## `packages\horizon\contracts\mocks\CallbackGasProbe.sol`

- Contracts: CallbackGasProbe
- Tags: none
- Functions: probeEligibility, probeAfterCollection
- Modifiers: none
- Events: none

## `packages\horizon\contracts\mocks\Dummy.sol`

- Contracts: Dummy
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\horizon\contracts\mocks\EpochManagerMock.sol`

- Contracts: EpochManagerMock
- Tags: none
- Functions: setEpochLength, runEpoch, isCurrentEpochRun, blockNum, blockHash, currentEpoch, currentEpochBlock, currentEpochBlockSinceStart, epochsSince, epochsSinceUpdate
- Modifiers: none
- Events: none

## `packages\horizon\contracts\mocks\GasReportingEligibilityMock.sol`

- Contracts: GasReportingEligibilityMock
- Tags: none
- Functions: isEligible, supportsInterface
- Modifiers: none
- Events: none

## `packages\horizon\contracts\utilities\Authorizable.sol`

- Contracts: Authorizable
- Tags: none
- Functions: _getAuthorizableStorage, authorizations, authorizeSigner, thawSigner, cancelThawSigner, revokeAuthorizedSigner, getThawEnd, isAuthorized, _isAuthorized, _requireAuthorized, _verifyAuthorizationProof
- Modifiers: onlyAuthorized
- Events: none

## `packages\horizon\test\unit\data-service\implementations\DataServiceBaseUpgradeable.sol`

- Contracts: DataServiceBaseUpgradeable
- Tags: none
- Functions: initialize, register, acceptProvisionPendingParameters, startService, stopService, collect, slash, controller
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\implementations\DataServiceImpFees.sol`

- Contracts: DataServiceImpFees
- Tags: none
- Functions: register, acceptProvisionPendingParameters, startService, stopService, collect, lockStake, slash
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\implementations\DataServiceImpPausableUpgradeable.sol`

- Contracts: DataServiceImpPausableUpgradeable
- Tags: none
- Functions: initialize, register, acceptProvisionPendingParameters, startService, stopService, collect, slash, setPauseGuardian, controller
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\libraries\ProvisionTrackerImplementation.sol`

- Contracts: ProvisionTrackerImplementation
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\data-service\utilities\ProvisionManagerImpl.t.sol`

- Contracts: ProvisionManagerImpl
- Tags: none
- Functions: requireValidProvision_, requireAuthorizedForProvision_
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\libraries\LinkedList.t.sol`

- Contracts: LinkedListTest
- Tags: none
- Functions: setUp, test_Add_RevertGiven_TheItemIdIsZero, test_Add_GivenTheListIsEmpty, test_Add_GivenTheListIsNotEmpty, test_Add_RevertGiven_TheListIsAtMaxSize, test_Remove_RevertGiven_TheListIsEmpty, test_Remove_GivenTheListIsNotEmpty, test_TraverseGivenTheListIsEmpty, test_TraverseWhenIterationsAreNotSpecified, test_TraverseWhenIterationsAreSpecified, test_TraverseWhenIterationsAreInvalid, _assertAddItem, _assertRemoveItem, _assertTraverseList
- Modifiers: givenTheListIsNotEmpty
- Events: none

## `packages\horizon\test\unit\libraries\ListImplementation.sol`

- Contracts: ListImplementation
- Tags: none
- Functions: _addItemToList, _deleteItem, _getNextItem, _processItemAddition, _buildItemId
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\libraries\PPMMath.t.sol`

- Contracts: PPMMathTest
- Tags: none
- Functions: test_mulPPM, test_mulPPMRoundUp, test_isValidPPM, test_mullPPM_RevertWhen_InvalidPPM, test_mullPPMRoundUp_RevertWhen_InvalidPPM
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\libraries\StakeClaims.t.sol`

- Contracts: StakeClaimsTest
- Tags: none
- Functions: test_BuildStakeClaimId
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\mocks\InvalidControllerMock.t.sol`

- Contracts: InvalidControllerMock
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\mocks\PartialControllerMock.t.sol`

- Contracts: PartialControllerMock
- Tags: none
- Functions: getContractProxy
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\graph-tally-collector\signer\authorizeSigner.t.sol`

- Contracts: GraphTallyAuthorizeSignerTest
- Tags: none
- Functions: testGraphTally_AuthorizeSigner, testGraphTally_AuthorizeSigner_RevertWhen_Invalid, testGraphTally_AuthorizeSigner_RevertWhen_AlreadyAuthroized, testGraphTally_AuthorizeSigner_RevertWhen_AlreadyAuthroizedAfterRevoking, testGraphTally_AuthorizeSigner_RevertWhen_ProofExpired
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\graph-tally-collector\signer\cancelThawSigner.t.sol`

- Contracts: GraphTallyCancelThawSignerTest
- Tags: none
- Functions: testGraphTally_CancelThawSigner, testGraphTally_CancelThawSigner_RevertWhen_NotAuthorized, testGraphTally_CancelThawSigner_RevertWhen_NotThawing
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\graph-tally-collector\signer\revokeSigner.t.sol`

- Contracts: GraphTallyRevokeAuthorizedSignerTest
- Tags: none
- Functions: testGraphTally_RevokeAuthorizedSigner, testGraphTally_RevokeAuthorizedSigner_RevertWhen_NotAuthorized, testGraphTally_RevokeAuthorizedSigner_RevertWhen_NotThawing, testGraphTally_RevokeAuthorizedSigner_RevertWhen_StillThawing
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\graph-tally-collector\signer\thawSigner.t.sol`

- Contracts: GraphTallyThawSignerTest
- Tags: none
- Functions: testGraphTally_ThawSigner, testGraphTally_ThawSigner_RevertWhen_NotAuthorized, testGraphTally_ThawSigner_RevertWhen_AlreadyRevoked, testGraphTally_ThawSigner_AlreadyThawing
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\accept.t.sol`

- Contracts: RecurringCollectorAcceptTest
- Tags: none
- Functions: test_Accept, test_Accept_Revert_WhenAcceptanceDeadlineElapsed, test_Accept_Idempotent_WhenAlreadyAccepted, test_Accept_Idempotent_AfterDeadline_SameHash, test_Accept_EmitsOfferStored_WhenFreshTerms, test_Accept_Revert_WhenDifferentHashSameAgreementId, test_Accept_Revert_AfterCancellation_SameHash
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\BareAgreementOwner.t.sol`

- Contracts: BareAgreementOwner
- Tags: none
- Functions: beforeCollection, afterCollection
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\base.t.sol`

- Contracts: RecurringCollectorBaseTest
- Tags: none
- Functions: test_RecoverRCASigner, test_RecoverRCAUSigner
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\cancel.t.sol`

- Contracts: RecurringCollectorCancelTest
- Tags: none
- Functions: test_Cancel, test_Cancel_Revert_WhenNotAccepted, test_Cancel_Revert_WhenNotDataService
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\cancelSignature.t.sol`

- Contracts: RecurringCollectorCancelSignedOfferTest
- Tags: none
- Functions: test_CancelSigned_BlocksAccept, test_CancelSigned_EmitsEvent, test_CancelSigned_BlocksUpdate, test_CancelSigned_Idempotent, test_CancelSigned_DoesNotAffectDifferentSigner, test_CancelSigned_SelfAuthenticating, test_CancelSigned_CombinedWithActiveDoesNotRevert, test_CancelSigned_CombinedWithPendingDoesNotRevert, test_CancelSigned_UndoWithZero
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\coverageGaps.t.sol`

- Contracts: MalformedEligibilityPayer, RecurringCollectorCoverageGapsTest, MockDataServiceForCancel
- Tags: none
- Functions: setReturnMalformed, beforeCollection, afterCollection, supportsInterface, _offer, _offerAndAccept, test_Offer_Revert_WhenOfferTypeInvalid_Two, test_Offer_Revert_WhenOfferTypeInvalid_MaxUint8, test_GetAgreementDetails_Index0_Accepted, test_GetAgreementOfferAt_PendingUpdateExists, test_GetAgreementOfferAt_Index0, test_GetAgreementOfferAt_Index1_WithPending, test_GetMaxNextClaim_ScopeActiveOnly, test_GetMaxNextClaim_ScopePendingOnly, test_GetMaxNextClaim_ScopePendingOnly_WithPending, test_Collect_EmitsPayerCallbackFailed_WhenEligibilityReturnsMalformed, test_Update_OverwritesOffer_WhenNotYetAccepted, test_GetCollectionInfo_ZeroCollectionSeconds, test_GetMaxNextClaim_OfferedButNotAccepted, test_Cancel_PendingUpdate_ClearsPendingTerms, test_Cancel_ActiveTerms_WhenPendingExists, test_Cancel_NoOp_WhenHashMatchesNeither, test_GetAgreementOfferAt_Index2_ReturnsEmpty, test_GetAgreementOfferAt_EmptyAgreement, test_GetAgreementOfferAt_Index1_NoPending
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\MalformedERC165Payer.t.sol`

- Contracts: MalformedERC165Payer
- Tags: none
- Functions: beforeCollection, afterCollection
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\RecurringCollectorAuthorizableTest.t.sol`

- Contracts: RecurringCollectorAuthorizableTest
- Tags: none
- Functions: newAuthorizable, assumeValidFuzzAddress
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\RecurringCollectorHelper.t.sol`

- Contracts: RecurringCollectorHelper
- Tags: none
- Functions: generateSignedRCA, generateSignedRCAU, generateSignedRCAUForAgreement, generateSignedRCAUWithCorrectNonce, generateSignedRCAWithCalculatedId, withElapsedAcceptDeadline, withOKAcceptDeadline, sensibleRCA, sensibleRCAU, _sensibleDeadline, _sensibleEndsAt, _sensibleMaxSecondsPerCollection, _sensibleMaxInitialTokens, _sensibleMaxOngoingTokensPerSecond, _sensibleMinSecondsPerCollection
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\update.t.sol`

- Contracts: RecurringCollectorUpdateTest
- Tags: none
- Functions: test_Update_Revert_WhenUpdateElapsed, test_Update_Revert_WhenNeverAccepted, test_Update_Revert_WhenDataServiceNotAuthorized, test_Update_Revert_WhenInvalidSigner, test_Update_OK, test_Update_Revert_WhenInvalidNonce_TooLow, test_Update_Revert_WhenInvalidNonce_TooHigh, test_Update_Revert_WhenReplayAttack, test_Update_OK_NonceIncrementsCorrectly, test_Update_Idempotent_WhenAlreadyAtActiveHash, test_Update_EmitsOfferStored_WhenDirectApplyFreshTerms
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\payments\recurring-collector\viewFunctions.t.sol`

- Contracts: RecurringCollectorViewFunctionsTest
- Tags: none
- Functions: test_GetCollectionInfo_Accepted_AfterTime, test_GetCollectionInfo_CanceledBySP, test_GetCollectionInfo_NotAccepted, test_GetCollectionInfo_CanceledByPayer_SameBlock, test_GetCollectionInfo_CanceledByPayer_WithWindow, test_GetAgreement_FieldsMatch
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\utilities\Authorizable.t.sol`

- Contracts: AuthorizableImp, AuthorizableTest, AuthorizableHelper
- Tags: none
- Functions: setUp, setupAuthorizable, newAuthorizable, assumeValidFuzzAddress, test_AuthorizeSigner, test_AuthorizeSigner_Revert_WhenAlreadyAuthorized, test_AuthorizeSigner_Revert_WhenInvalidProofDeadline, test_AuthorizeSigner_Revert_WhenAuthorizableInvalidSignerProof, test_ThawSigner, test_ThawSigner_Revert_WhenNotAuthorized, test_ThawSigner_Revert_WhenAuthorizationRevoked, test_CancelThawSigner, test_CancelThawSigner_Revert_When_NotAuthorized, test_CancelThawSigner_Revert_WhenAuthorizationRevoked, test_CancelThawSigner_Revert_When_NotThawing, test_RevokeAuthorizedSigner, test_RevokeAuthorizedSigner_Revert_WhenNotAuthorized, test_RevokeAuthorizedSigner_Revert_WhenAuthorizationRevoked, test_RevokeAuthorizedSigner_Revert_WhenNotThawing, test_RevokeAuthorizedSigner_Revert_WhenStillThawing, test_IsAuthorized_Revert_WhenZero, authorizeAndThawSignerWithChecks, authorizeAndRevokeSignerWithChecks, authorizeSignerWithChecks, assertNotAuthorized
- Modifiers: withFuzzyThaw
- Events: none

## `packages\horizon\test\unit\utils\Bounder.t.sol`

- Contracts: Bounder
- Tags: none
- Functions: boundKeyAndAddr, boundAddrAndKey, boundAddr, boundKey, boundChainId, boundTimestampMin, boundSkipFloor, boundSkipCeil, boundSkip, orTillEndOfTime
- Modifiers: none
- Events: none

## `packages\horizon\test\unit\utils\Utils.sol`

- Contracts: Utils
- Tags: none
- Functions: resetPrank
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\base\IMulticall.sol`

- Contracts: IMulticall
- Tags: none
- Functions: multicall
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\epochs\IEpochManager.sol`

- Contracts: IEpochManager
- Tags: none
- Functions: setEpochLength, runEpoch, isCurrentEpochRun, blockNum, blockHash, currentEpoch, currentEpochBlock, currentEpochBlockSinceStart, epochsSince, epochsSinceUpdate
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\contracts\upgrades\IGraphProxy.sol`

- Contracts: IGraphProxy
- Tags: none
- Functions: admin, setAdmin, implementation, pendingImplementation, upgradeTo, acceptUpgrade, acceptUpgradeAndCall
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\data-service\IDataServiceAgreements.sol`

- Contracts: IDataServiceAgreements
- Tags: none
- Functions: cancelIndexingAgreementByPayer
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\data-service\IDataServicePausable.sol`

- Contracts: IDataServicePausable
- Tags: none
- Functions: pause, unpause, pauseGuardians
- Modifiers: none
- Events: PauseGuardianSet

## `packages\interfaces\contracts\horizon\IAgreementCollector.sol`

- Contracts: IAgreementCollector
- Tags: none
- Functions: offer, cancel, getAgreementDetails, getMaxNextClaim, getMaxNextClaim, getAgreementOfferAt
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\horizon\IAuthorizable.sol`

- Contracts: IAuthorizable
- Tags: none
- Functions: REVOKE_AUTHORIZATION_THAWING_PERIOD, authorizeSigner, thawSigner, cancelThawSigner, revokeAuthorizedSigner, getThawEnd, isAuthorized
- Modifiers: none
- Events: SignerAuthorized, SignerThawing, SignerThawCanceled, SignerRevoked

## `packages\interfaces\contracts\horizon\internal\ILinkedList.sol`

- Contracts: ILinkedList
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\allocate\IIssuanceAllocationData.sol`

- Contracts: IIssuanceAllocationData
- Tags: none
- Functions: getTargetData
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\allocate\IIssuanceAllocationStatus.sol`

- Contracts: IIssuanceAllocationStatus
- Tags: none
- Functions: getTargetAllocation, getTotalAllocation, getTargets, getTargetAt, getTargetCount, getIssuancePerBlock, getDistributionState
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\issuance\allocate\IIssuanceTarget.sol`

- Contracts: IIssuanceTarget
- Tags: none
- Functions: beforeIssuanceAllocationChange, getIssuanceAllocator, setIssuanceAllocator
- Modifiers: none
- Events: IssuanceAllocatorSet, BeforeIssuanceAllocationChange

## `packages\interfaces\contracts\issuance\common\IPausableControl.sol`

- Contracts: IPausableControl
- Tags: none
- Functions: pause, unpause, paused
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\subgraph-service\internal\IAttestation.sol`

- Contracts: IAttestation
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\subgraph-service\internal\IIndexingAgreement.sol`

- Contracts: IIndexingAgreement
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\subgraph-service\internal\ILegacyAllocation.sol`

- Contracts: ILegacyAllocation
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IEpochManagerToolshed.sol`

- Contracts: IEpochManagerToolshed
- Tags: none
- Functions: epochLength
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\IL2GNSToolshed.sol`

- Contracts: IL2GNSToolshed
- Tags: none
- Functions: nextAccountSeqID, subgraphNFT
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\internal\IOwnable.sol`

- Contracts: IOwnable
- Tags: none
- Functions: owner, renounceOwnership, transferOwnership
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\internal\IPausable.sol`

- Contracts: IPausable
- Tags: none
- Functions: paused
- Modifiers: none
- Events: none

## `packages\interfaces\contracts\toolshed\ISubgraphServiceToolshed.sol`

- Contracts: ISubgraphServiceToolshed
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\issuance\contracts\common\EnumerableSetUtil.sol`

- Contracts: EnumerableSetUtil
- Tags: none
- Functions: getPage, getPageBytes16
- Modifiers: none
- Events: none

## `packages\issuance\contracts\test\allocate\MockERC165.sol`

- Contracts: MockERC165
- Tags: none
- Functions: supportsInterface
- Modifiers: none
- Events: none

## `packages\issuance\contracts\test\allocate\MockNotificationTracker.sol`

- Contracts: MockNotificationTracker
- Tags: none
- Functions: beforeIssuanceAllocationChange, getIssuanceAllocator, setIssuanceAllocator, supportsInterface, resetNotificationCount
- Modifiers: none
- Events: NotificationReceived

## `packages\issuance\contracts\test\allocate\MockReentrantTarget.sol`

- Contracts: MockReentrantTarget
- Tags: none
- Functions: setReentrantAction, beforeIssuanceAllocationChange, getIssuanceAllocator, setIssuanceAllocator, supportsInterface
- Modifiers: none
- Events: none

## `packages\issuance\contracts\test\allocate\MockRevertingTarget.sol`

- Contracts: MockRevertingTarget
- Tags: none
- Functions: beforeIssuanceAllocationChange, getIssuanceAllocator, setIssuanceAllocator, supportsInterface
- Modifiers: none
- Events: none

## `packages\issuance\contracts\test\allocate\MockSimpleTarget.sol`

- Contracts: MockSimpleTarget
- Tags: none
- Functions: beforeIssuanceAllocationChange, getIssuanceAllocator, setIssuanceAllocator, supportsInterface
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\mocks\MockEligibilityOracle.sol`

- Contracts: MockEligibilityOracle
- Tags: none
- Functions: setEligible, setDefaultEligible, isEligible
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\mocks\MockSubgraphService.sol`

- Contracts: MockSubgraphService
- Tags: none
- Functions: cancelIndexingAgreementByPayer, setRevert
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\revokeAgreementUpdate.t.sol`

- Contracts: RecurringAgreementManagerCancelPendingUpdateTest
- Tags: none
- Functions: test_CancelPendingUpdate_ClearsPendingState, test_CancelPendingUpdate_EmitsEvent, test_CancelPendingUpdate_CanOfferNewUpdateAfterCancel, test_CancelPendingUpdate_RejectsUnknown_WhenNotOffered, test_CancelPendingUpdate_Revert_WhenNotOperator, test_CancelPendingUpdate_Succeeds_WhenPaused
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\agreement-manager\revokeOffer.t.sol`

- Contracts: RecurringAgreementManagerCancelOfferedTest
- Tags: none
- Functions: test_CancelOffered_ClearsAgreement, test_CancelOffered_FullyRemovesTracking, test_CancelOffered_ClearsPendingUpdate, test_CancelOffered_EmitsEvent, test_CancelOffered_RejectsUnknown_WhenNotOffered, test_CancelOffered_Revert_WhenNotOperator, test_CancelOffered_Succeeds_WhenPaused
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\common\enumerableSetUtil.t.sol`

- Contracts: EnumerableSetUtilTest
- Tags: none
- Functions: setUp, test_GetPage_EmptySet_ReturnsEmpty, test_GetPage_ReturnsAllElements, test_GetPage_WithOffset, test_GetPage_WithCount, test_GetPage_OffsetAndCount, test_GetPage_OffsetAtEnd_ReturnsEmpty, test_GetPage_OffsetPastEnd_ReturnsEmpty, test_GetPage_CountClamped, test_GetPage_ZeroCount_ReturnsEmpty, test_GetPageBytes16_EmptySet_ReturnsEmpty, test_GetPageBytes16_ReturnsAllElements, test_GetPageBytes16_TruncatesBytes32ToBytes16, test_GetPageBytes16_WithOffset, test_GetPageBytes16_WithCount, test_GetPageBytes16_OffsetPastEnd_ReturnsEmpty, test_GetPageBytes16_CountClamped, test_GetPageBytes16_ZeroCount_ReturnsEmpty
- Modifiers: none
- Events: none

## `packages\issuance\test\unit\mocks\EnumerableSetUtilHarness.sol`

- Contracts: EnumerableSetUtilHarness
- Tags: none
- Functions: addAddress, addressSetLength, getPage, addBytes32, bytes32SetLength, getPageBytes16
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\libraries\Attestation.sol`

- Contracts: Attestation
- Tags: none
- Functions: areConflicting, parse, _toUint8, _toBytes32
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\libraries\IndexingAgreementDecoder.sol`

- Contracts: IndexingAgreementDecoder
- Tags: none
- Functions: decodeCollectData, decodeRCAMetadata, decodeRCAUMetadata, decodeCollectIndexingFeeDataV1, decodeIndexingAgreementTermsV1
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\libraries\IndexingAgreementDecoderRaw.sol`

- Contracts: IndexingAgreementDecoderRaw
- Tags: none
- Functions: decodeCollectData, decodeRCAMetadata, decodeRCAUMetadata, decodeCollectIndexingFeeDataV1, decodeIndexingAgreementTermsV1
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\utilities\AttestationManager.sol`

- Contracts: AttestationManager
- Tags: none
- Functions: __AttestationManager_init, __AttestationManager_init_unchained, _recoverSigner, _encodeReceipt
- Modifiers: none
- Events: none

## `packages\subgraph-service\contracts\utilities\AttestationManagerStorage.sol`

- Contracts: AttestationManagerV1Storage
- Tags: none
- Functions: none
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\libraries\IndexingAgreement.t.sol`

- Contracts: IndexingAgreementTest
- Tags: none
- Functions: setUp, test_IndexingAgreement_Get, test_IndexingAgreement_OnCloseAllocation_NoAgreement, test_IndexingAgreement_OnCloseAllocation_InactiveAgreement, test_IndexingAgreement_OnCloseAllocation_RevertsWhenActiveAndBlocked, test_IndexingAgreement_OnCloseAllocation_CancelsWhenActiveAndNotBlocked, test_IndexingAgreement_StorageManagerLocation
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\mocks\MockEpochManager.sol`

- Contracts: MockEpochManager
- Tags: none
- Functions: setEpochLength, runEpoch, isCurrentEpochRun, blockNum, blockHash, currentEpoch, currentEpochBlock, currentEpochBlockSinceStart, epochsSince, epochsSinceUpdate
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\subgraphService\indexing-agreement\cancel.t.sol`

- Contracts: SubgraphServiceIndexingAgreementCancelTest
- Tags: none
- Functions: test_SubgraphService_CancelIndexingAgreementByPayer_Revert_WhenPaused, test_SubgraphService_CancelIndexingAgreementByPayer_Revert_WhenNotAuthorized, test_SubgraphService_CancelIndexingAgreementByPayer_Revert_WhenNotAccepted, test_SubgraphService_CancelIndexingAgreementByPayer_Revert_WhenCanceled, test_SubgraphService_CancelIndexingAgreementByPayer, test_SubgraphService_CancelIndexingAgreement_Revert_WhenPaused, test_SubgraphService_CancelIndexingAgreement_Revert_WhenNotAuthorized, test_SubgraphService_CancelIndexingAgreement_Revert_WhenNotActive_WithInvalidProvision, test_SubgraphService_CancelIndexingAgreement_Revert_WhenNotActive_WithoutRegistration, test_SubgraphService_CancelIndexingAgreement_Revert_WhenNotAccepted, test_SubgraphService_CancelIndexingAgreement_Revert_WhenCanceled, test_SubgraphService_CancelIndexingAgreement_Revert_WhenWrongIndexer, test_SubgraphService_CancelIndexingAgreement_OK, test_SubgraphService_CancelIndexingAgreement_OK_WhenProvisionBelowMinimum
- Modifiers: none
- Events: none

## `packages\subgraph-service\test\unit\utils\Utils.sol`

- Contracts: Utils
- Tags: none
- Functions: resetPrank
- Modifiers: none
- Events: none
