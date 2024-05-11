import hashlib

# Define the message to be hashed
message = b"Hello, world!"

# Create a SHA-3 hash object with a 256-bit output size
sha3_256 = hashlib.sha3_256()

# Update the hash object with the message
sha3_256.update(message)

# Get the hash digest as a byte string
digest = sha3_256.digest()

# Convert the digest to a hexadecimal string for display
hexdigest = digest.hex()

# Print the hash digest in hexadecimal format
print(hexdigest)

