from decouple import config
from web3 import Web3
import random
import string
import json

web3 = Web3(Web3.HTTPProvider(config('infura_url')))
contract_address = web3.toChecksumAddress(config('contract_address'))
abi = json.loads(config('ABI'))
unicorn = web3.eth.contract(address=contract_address, abi=abi)


def random_md5like_hash():
    available_chars= string.hexdigits[:16]
    return ''.join(
        random.choice(available_chars)
        for dummy in range(20))


def totalSupply():
    return unicorn.functions.totalSupply().call()


def change_contract_state(owner_address, uniq_string, media_url):
    nonce_value = web3.eth.getTransactionCount(owner_address)
    unicorn_txn = unicorn.functions.mint(owner_address, uniq_string, media_url).buildTransaction({
        'chainId': 4,
        'gas': 7000000,
        'maxFeePerGas': web3.toWei('2', 'gwei'),
        'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
        'nonce': nonce_value,
    })
    signed_txn = web3.eth.account.sign_transaction(unicorn_txn, private_key=config('private_key'))
    tx = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx)
    return web3.toHex(web3.keccak(signed_txn.rawTransaction))
