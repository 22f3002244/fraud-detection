// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransactionStorage {
    struct Transaction {
        uint id;
        uint amount;
        string location;
        bool fraud;
    }

    Transaction[] public transactions;

    // Add a transaction
    function addTransaction(uint _id, uint _amount, string memory _location, bool _fraud) public {
        transactions.push(Transaction(_id, _amount, _location, _fraud));
    }

    // Get a transaction
    function getTransaction(uint index) public view returns (uint, uint, string memory, bool) {
        Transaction memory t = transactions[index];
        return (t.id, t.amount, t.location, t.fraud);
    }

    // Get total transactions
    function getTransactionCount() public view returns (uint) {
        return transactions.length;
    }
}
