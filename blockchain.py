import hashlib
import datetime as date



class Block:
    def __init__(self, timestamp, data):
        self.timestamp = timestamp
        self.data = data

    def __str__(self):
        s += "Timestamp: " + str(self.timestamp) + "\n"
        s += "Data: " + self.data + "\n"
        return s        

class InnerBlock: 
    def __init__(self, index, block, previoushash):
        self.index = index
        self.timestamp = block.timestamp
        self.data = block.data
        self.previous_hash = previoushash
        self.hash = ""

    def calculate_hash(self):
        hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def __str__(self):
        s = "Block #" + str(self.index) + "\n"
        s += "Timestamp: " + str(self.timestamp) + "\n"
        s += "Data: " + self.data + "\n"
        s += "Hash: " + self.hash + "\n"
        s += "Previous Hash: " + self.previous_hash + "\n"
        return s        

class Blockchain:
    def __init__(self, time):
        self.chain = [self.create_genesis_block(time)]

    def create_genesis_block(self, time):
        return InnerBlock(0, Block(time, "Genesis Block"), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block):
        new_block = InnerBlock(len(self.chain)+1, block, self.get_latest_block().hash)
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        return self

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
    
    def length(self):
        return len(self.chain)-1
    
    def __str__(self):
        s ='BLOCKCHAIN:\n'
        for b in self.chain:
            s += str(b)
        return s

