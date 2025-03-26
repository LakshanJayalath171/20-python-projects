import random
import string

chars = " "+string.punctuation+string.digits+string.ascii_letters
chars  = list(chars)
keys = chars.copy()


random.shuffle(keys)


print(f"chars : {chars}")
print(f"keys  : {keys}")

#ENCRYPTION

plain_text = input("Enter A Message For Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"Original  Message : {plain_text}")
print(f"Encrypted Message : {cipher_text}")

#DECRYPTION

cipher_text = input("Enter A Message For Decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message: {cipher_text}")
print(f"Decrypted Message: {plain_text}")