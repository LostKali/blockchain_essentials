import hashlib

string = "Hello, World!"

# Create a hash object using the SHA-256 algorithm
hash_object = hashlib.sha256()

# Update the hash object with the string’s bytes
hash_object.update(string.encode('utf-8'))

# Get the hash value as a hex string
hex_dig = hash_object.hexdigest()

print("String: {}".format(string))
print("Hash value (SHA-256): {}".format(hex_dig))

