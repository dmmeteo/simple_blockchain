#!/usr/bin/env python
from datetime import datetime
from blockchain import Block


def create_genesis_block():
    return Block(0, datetime.now(), "My first block data", "0")


def next_block(last_block):
    index = last_block.index + 1
    timestamp = datetime.now()
    data = "Hey! I'm block %s" % index
    last_hash = last_block.hash

    return Block(index, timestamp, data, last_hash)


def main():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    num_of_blocks_to_add = 20

    for b in range(num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))


if __name__ == "__main__":
    main()
