import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

# ENCRYPTION
plaintext = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plaintext:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message : {plaintext}")
print(f"Encrypted message: {cipher_text}")

# DECRYPTION
cipher_text = input("Enter a message to decrypt: ")
plaintext = ""

for letter in cipher_text:
    index = key.index(letter)
    plaintext += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message : {plaintext}")
