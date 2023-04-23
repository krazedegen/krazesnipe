"""
Written by @krazedegen

DISCLAIMER:

The use of this script comes with no guarantees or warranties, express or implied.
The user assumes all risk, including but not limited to the risk of financial loss,
associated with the use of this script. The author is not responsible for any losses
or damages, direct or indirect, that may result from the use of this script.

By using this script, you acknowledge that you have read and understood this disclaimer,
and you agree to indemnify and hold harmless the author for any liability or claims that
may arise from the use of this script.

"""


import json
import os
import time
import sys
from threading import Timer
from dotenv import load_dotenv
from pathlib import Path
from web3 import Web3

# Load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Import environment variables
bsc = os.getenv("NODE_URL")
sender_address = os.getenv("SENDER_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")

web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

factoryTestnet = web3.toChecksumAddress('0xb7926c0430afb07aa7defde6da862ae0bde767bc')
routerTestnet = web3.toChecksumAddress('0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3')

wbnbTestnet = web3.toChecksumAddress('0xae13d989dac2f0debff460ac112a837c89baa7cd')

tokenA = web3.toChecksumAddress('0x20e7256Db0e517E387b494457e4Df67A624f1968')
tokenB = wbnbTestnet

spend = wbnbTestnet

# Load ABIs from files
with open('uniswap_factory_abi.json') as f:
    uniswap_factory_abi = json.load(f)

with open('panabi.json') as f:
    panabi = json.load(f)

with open('lpabi.json') as f:
    lpabi = json.load(f)

uniswap_factory = factoryTestnet
contract = web3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)

panRouterContractAddress = routerTestnet
contractbuy = web3.eth.contract(address=panRouterContractAddress, abi=panabi)

tokenToBuy = tokenA

def buy():
    print('Lets Go')

    nonce = web3.eth.get_transaction_count(sender_address)

    pancakeswap2_txn = contractbuy.functions.swapExactETHForTokens(
        0, [spend, tokenToBuy], sender_address, (int(time.time()) + 10000)
    ).buildTransaction({
        'from': sender_address,
        'value': web3.toWei(0.01, 'ether'),
        'gas': 210000,
        'gasPrice': web3.toWei('5', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=private_key)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("You Hodl: " + web3.toHex(tx_token))
    exit()

def checkLp():
    print('checking balance')
    lp = pair
    lpcontract = web3.eth.contract(address=lp, abi=lpabi)
    balance = lpcontract.functions.getReserves().call()
    b = balance[0]
    print(b)
    if b > 0:
        print('balance detected')
        buy()
    else:
        print('no balance detected')
        test()

def address():
    print('check for address')
    global pair
    pair = contract.functions.getPair(tokenA, tokenB).call()
    print(pair)
    if pair != web3.toChecksumAddress('0x0000000000000000000000000000000000000000'):
        print('lp address detected')
        time.sleep(1)
        checkLp()

run = True
def test():
    global run
    address()
    if run:
        Timer(1, test).start()

test()
