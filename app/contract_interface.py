from web3 import Web3
import os

# Configurações básicas (recomendado usar variáveis de ambiente)
WEB3_PROVIDER_URI = os.getenv("WEB3_PROVIDER_URI")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
CHAIN_ID = int(os.getenv("CHAIN_ID", "97"))

# ABI do contrato (simplificado, ajuste conforme seu deploy)
CONTRACT_ABI = [
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "bytes32",
				"name": "hash",
				"type": "bytes32"
			}
		],
		"name": "FaceRegistered",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "getMyFaceHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "user",
				"type": "address"
			}
		],
		"name": "hasFace",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "faceHash",
				"type": "bytes32"
			}
		],
		"name": "registerFace",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

# Instancia o contrato
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def register_face_onchain(face_hash: str) -> str:
    nonce = web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    hash_bytes = web3.to_bytes(hexstr=face_hash)

    txn = contract.functions.registerFace(hash_bytes).build_transaction({
        'from': ACCOUNT_ADDRESS,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': web3.to_wei('10', 'gwei'),
        'chainId': CHAIN_ID,
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)
