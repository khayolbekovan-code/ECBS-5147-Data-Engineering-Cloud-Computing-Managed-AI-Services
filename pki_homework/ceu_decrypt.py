from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Load CEU's private key
with open("ceu_key", "r", encoding="utf8") as f:
    private_key = RSA.import_key(f.read())

# Load the encrypted message the visitor sent
with open("encrypted_message.bin", "rb") as f:
    encrypted = f.read()

# Decrypt it and print it
decrypted = PKCS1_OAEP.new(private_key).decrypt(encrypted)
print("Decrypted message:", decrypted.decode("utf-8"))
