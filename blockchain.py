#!/usr/bin/env python
import hashlib as h


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        string_data = ", ".join(
            [
                str(self.index),
                str(self.timestamp),
                str(self.data),
                str(self.previous_hash),
            ]
        )

        sha = h.sha256()
        sha.update(string_data.encode('utf-8'))

        return sha.hexdigest()
