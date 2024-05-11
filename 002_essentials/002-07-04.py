import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time(), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(previous_block.index + 1, time(), data, previous_block.hash)
        # print("New block hash:", new_block.hash)
        # print("New block calculated hash:", new_block.calculate_hash())
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            # print("Current block hash:", current_block.hash)
            # print("Current block hash calculated:", current_block.calculate_hash())
            if current_block.hash != current_block.calculate_hash():
                return False

            # print("Previous block hash:", previous_block.hash)
            # print("Previous block hash saved in current:", current_block.previous_hash)
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

blockchain = Blockchain()

blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.add_block("Transaction 3")

print("Blockchain is valid: ", blockchain.is_chain_valid())

# Attempt to tamper with the second block
blockchain.chain[1].data = "Tampered Transaction"
print("Blockchain is valid: ", blockchain.is_chain_valid())

