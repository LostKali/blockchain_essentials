import hashlib
import time

# define the block header fields
version = 1
previous_block_hash = "00000000000000000007d28e1a9ac3b37760e3b3fbbd3df2b8f7670a434f18a6"
merkle_root = "9d7d1c2fa42e7f520d33de8e7bb28132586d30ef7c6d9b9e446e6c12d1f7cf25"
timestamp = int(time.time())
difficulty = 4 # number of leading zeros required in the hash
nonce = 0

# combine the header fields into a single string
header = str(version) + previous_block_hash + merkle_root + str(timestamp) + str(difficulty) + str(nonce)

# loop until a valid hash is found
while True:
    # add the nonce value to the header
    header_with_nonce = header + str(nonce)

    # compute the SHA-256 hash of the header with nonce
    hash = hashlib.sha256(header_with_nonce.encode()).hexdigest()

    # check if the hash meets the difficulty target
    if hash[:difficulty] == "0" * difficulty:
        print("Block mined successfully!")
        print("Nonce:", nonce)
        print("Hash:", hash)
        break

    # increment the nonce and try again
    nonce += 1

