import time
import hashlib

from coin_mint_prototype import generate_coin, generate_phrase


class ChaddleBlock:
    def __init__(self, index, proof_no, prev_hash, data, block_name, timestamp=None):
        # First block or something
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.block_name = block_name
        self.timestamp = timestamp or time.time()


    @property
    def calculate_hash(self):
        # Calculate the hash of each block
        block_of_string = f"{self.index} {self.proof_no} {self.prev_hash} {self.data} {self.block_name} {self.timestamp}"

        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return f"""================================\nMining: {self.block_name}\n{self.index}\n{self.proof_no}\n
        {self.prev_hash}\n{self.data}\n{self.timestamp}\n================================"""


class ChaddleChain:

    def __init__(self):
        # Constructor
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()

    def construct_genesis(self):
        # Construct init block
        self.construct_block(proof_no=0, prev_hash=0, block_name="ChaddleOriginBlock")

    def construct_block(self, proof_no, prev_hash, block_name):
        # Construct new block to add to chaddle chain
        cblock = ChaddleBlock(index=len(self.chain), proof_no=proof_no, prev_hash=prev_hash, data=self.current_data, block_name=block_name)
        self.current_data = []

        self.chain.append(cblock)

        return cblock

    @staticmethod
    def check_validity(cblock, prev_block):
        # Check if cc is valid
        if prev_block.index + 1 != cblock.index:
            return False

        elif prev_block.calculate_hash != cblock.prev_hash:
            return False

        elif not ChaddleChain.verifying_proof(cblock.proof_no, prev_block.proof_no):
            return False

        elif cblock.timestamp <= prev_block.timestamp:
            return False

        return True

    def new_data(self, sender, recipient, quantity):
        # New transaction to data of transactions
        self.current_data.append({"sender": sender, "recipient": recipient, "quantity": quantity})
        return True

    @staticmethod
    def proof_of_work(last_proof):
        proof_no = 0
        while ChaddleChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        # Check if there are 4 zeros leading the block

        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latest_block(self):
        return self.chain[-1]

    def block_mining(self, details_miner):

        self.new_data(
            sender="0",  # it implies that this node has created a new block
            recipient=details_miner,
            quantity=
            1,  # creating a new block (or identifying the proof number) is awarded with 1
        )

        l_block = self.latest_block

        l_proof_no = l_block.proof_no
        c_proof_no = self.proof_of_work(l_proof_no)
        
        block_name = l_block.block_name

        l_hash = l_block.calculate_hash
        c_block = self.construct_block(c_proof_no, l_hash, block_name)

        return vars(c_block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):
        # obtains block object from the block data

        return ChaddleBlock(
            block_data["index"],
            block_data["proof_no"],
            block_data["prev_hash"],
            block_data["data"],
            block_name=block_data["block_name"],
            timestamp=block_data["timestamp"])


blockchain = ChaddleChain()

for a in range(1):
    print("***Mining Chaddle Coin about to start***")
    print(blockchain.chain[0])

    last_block = blockchain.latest_block
    last_proof_no = last_block.proof_no
    proof_no = blockchain.proof_of_work(last_proof_no)

    blockchain.new_data(sender="0", recipient="Big Guy", quantity=1,)

    phrase = generate_phrase()

    last_hash = last_block.calculate_hash
    block = blockchain.construct_block(proof_no, last_hash, phrase)

    print("***Mining Chaddle Coin has been successful***")

    print(blockchain.chain)
    generate_coin(last_hash, phrase)
