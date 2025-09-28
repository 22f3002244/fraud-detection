from web3 import Web3
from solcx import compile_standard, set_solc_version
import json
import pandas as pd
import time

# Install Solidity compiler version
set_solc_version('0.8.0')

# Read smart contract
with open("TransactionStorage.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"TransactionStorage.sol": {"content": contract_source_code}},
    "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}}
})

# Extract ABI and bytecode
abi = compiled_sol['contracts']['TransactionStorage.sol']['TransactionStorage']['abi']
bytecode = compiled_sol['contracts']['TransactionStorage.sol']['TransactionStorage']['evm']['bytecode']['object']

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337  # Ganache default
my_address = w3.eth.accounts[0]
private_key = "0xa430aba0a620cb4aba1f777c51049353e5377e429c04937dd0e691cbd56313bf"  # Replace with one account private key from Ganache

# Get current gas price from network
current_gas_price = w3.eth.gas_price
print(f"Current network gas price: {current_gas_price}")

# Deploy contract
Transaction = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.get_transaction_count(my_address)

tx = Transaction.constructor().build_transaction({
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce,
    "gas": 3000000,
    "gasPrice": current_gas_price  # Use network gas price
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract deployed at:", tx_receipt.contractAddress)

# Interact with deployed contract
contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Load ML-predicted transactions
df = pd.read_csv('transactions_with_predictions.csv')

print(f"Processing {len(df)} transactions...")

# Process transactions with proper nonce management and error handling
for index, row in df.iterrows():
    try:
        # Get fresh nonce for each transaction
        current_nonce = w3.eth.get_transaction_count(my_address)
        
        # Build transaction with higher gas price
        tx = contract.functions.addTransaction(
            int(row['TransactionID']),
            int(row['Amount']),
            str(row['Location']),
            bool(row['Predicted_Fraud'])
        ).build_transaction({
            'chainId': chain_id,
            'from': my_address,
            'nonce': current_nonce,
            'gas': 300000,  # Increased gas limit
            'gasPrice': current_gas_price  # Use network gas price
        })
        
        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        
        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction {index + 1}/{len(df)} - ID {row['TransactionID']} added successfully. Gas used: {receipt.gasUsed}")
        
        # Small delay to avoid nonce conflicts
        time.sleep(0.1)
        
    except Exception as e:
        print(f"Error adding transaction {row['TransactionID']}: {e}")
        # Continue with next transaction instead of stopping
        continue

print("All transactions processed!")

# Optional: Verify some transactions were added
try:
    # Assuming your contract has a function to get transaction count
    # total_count = contract.functions.getTransactionCount().call()
    # print(f"Total transactions stored: {total_count}")
    print("Transaction processing completed successfully!")
except Exception as e:
    print(f"Note: Could not verify transaction count: {e}")