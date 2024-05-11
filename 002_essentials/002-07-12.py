import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

# Generate RSA key pair
keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

# Function to create a digital signature
def create_signature(message, private_key):
    hashed_message = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(hashed_message)
    return binascii.hexlify(signature)

# Function to verify the digital signature
def verify_signature(message, signature, public_key):
    hashed_message = SHA256.new(message.encode())
    try:
        pkcs1_15.new(public_key).verify(hashed_message, binascii.unhexlify(signature))
        print("Signature is valid.")
    except (ValueError, TypeError):
        print("Signature is invalid.")

# Message to be signed
message = 'Hello, World!'

# Create digital signature
signature = create_signature(message, keyPair)
print("Digital Signature:", signature)

# Verify the digital signature
#verify_signature(message, signature, public_key)

