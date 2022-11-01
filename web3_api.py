from web3 import Web3
from hexbytes import HexBytes

# Connect to Infura endpoint using web3 API
# 'API-KEY' is your Infura API Key

# Ethereum mainnet
# provider_url = 'https://mainnet.infura.io/v3/API-KEY'
# Arbitrum mainnet
provider_url = 'https://arbitrum-mainnet.infura.io/v3/API-KEY'
# Optimism mainet
# provider_url = 'https://optimism-mainnet.infura.io/v3/API-KEY'

w3 = Web3(Web3.HTTPProvider(provider_url))
w3.isConnected()

# Function for retrieving transaction receipt
def get_tx_receipt(txhash):
    assert(type(txhash)==HexBytes)
    receipt = w3.eth.getTransactionReceipt(txhash)
    return receipt

# Function for retrieving block information
# detail=True gives detailed information about each transaction included in the block
# detail=False lists transactions included in the block wihtout transaction details
def get_block_info(blockno, detail=True):
    info = w3.eth.getBlock(blockno, detail)
    return info

# Retrieve transaction information
def get_tx_info(txhash):
    assert(type(txhash)==HexBytes)
    info = w3.eth.getTransaction(txhash)
    return info

# This function converts a random string to a HexBytes.
def sha3(s:str):
    return Web3.sha3(text=s)