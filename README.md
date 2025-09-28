# ML-Blockchain Fraud Detection System

A fraud detection system that combines Machine Learning with Blockchain Technology to predict fraudulent transactions and store them immutably for audit trails and transparency.

## Overview

This system demonstrates the integration of machine learning fraud detection with blockchain storage, providing:
- Synthetic transaction data generation with fraud patterns
- Decision Tree classifier for fraud prediction  
- Smart contract deployment and interaction
- Immutable storage of ML predictions on blockchain

## Architecture

```
Data Generation → ML Model Training → Fraud Prediction → Blockchain Storage
```

## Tech Stack

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms
- **Web3.py**: Ethereum blockchain interaction
- **Solidity**: Smart contract development
- **Ganache**: Local blockchain development

## Project Structure

```
MLBC/
├── generate_data.py               # Transaction data generator
├── ml_model.py                   # ML model training and prediction
├── blockchain_interact.py        # Blockchain deployment and interaction
├── TransactionStorage.sol        # Smart contract for data storage
├── transactions.csv              # Generated transaction data
├── transactions_with_predictions.csv  # ML predictions output
└── README.md                     # Documentation
```

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ml-blockchain-fraud-detection.git
cd ml-blockchain-fraud-detection
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install pandas scikit-learn web3 py-solc-x numpy
```

4. **Set up Ganache**
- Download and install [Ganache](https://trufflesuite.com/ganache/)
- Launch Ganache (default: http://127.0.0.1:7545)
- Note an account address and private key for deployment

## Usage

1. **Generate transaction data**
```bash
python generate_data.py
```

2. **Train ML model and predict fraud**
```bash
python ml_model.py
```

3. **Deploy to blockchain**
```bash
python blockchain_interact.py
```
*Note: Update the `private_key` variable with your Ganache account key*

## Smart Contract

### TransactionStorage.sol
- `addTransaction()`: Stores transaction with fraud prediction
- `getTransaction()`: Retrieves transaction by index  
- `getTransactionCount()`: Returns total stored transactions

### Performance Metrics
- **Processing Speed**: 100 transactions in ~10 seconds
- **Gas Efficiency**: Average 117K gas per transaction
- **Success Rate**: 99% blockchain storage success

## Data Schema

### Input Format
```csv
TransactionID,Amount,Location,Fraud
0,245.67,US,0
1,1200.50,UK,1
```

### Output Format
```csv
TransactionID,Amount,Location,Fraud,Predicted_Fraud
0,245.67,US,0,0
1,1200.50,UK,1,1
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

Project Link: [https://github.com/yourusername/ml-blockchain-fraud-detection](https://github.com/yourusername/ml-blockchain-fraud-detection)
