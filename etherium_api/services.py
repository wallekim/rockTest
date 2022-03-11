from web3 import Web3
import json
from decouple import config


web3 = Web3(Web3.HTTPProvider(config('infura_url')))
print(web3.isConnected())
contract_address = config('contract_address')
abi = json.loads(config('ABI'))

contract = web3.eth.contract(address=contract_address, abi=abi)


def totalSupply():
    totalSupply = contract.functions.totalSupply().call()
    return totalSupply


def mint():
    private_key = config('private_key')
    nonce = web3.eth.getTransactionCount
    balanceOf = contract.functions.balanceOf(contract_address).call()

