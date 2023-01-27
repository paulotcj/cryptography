import hashlib
import base64

import time

def guess_password(salt, iterations, entropy):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c1 in alphabet:
        for c2 in alphabet:
            password = str.encode(c1 + c2)
            value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
            if value == entropy:
                return password




#-----------------------------------

print("\n\n-----------------------------------")
print("Testing for the effect changing the parameter: iterations")

iterations = 1 #45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
# SALTED-SHA512-PBKDF2
password = "JJ".encode()
# Insert code here
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
hash_generated = base64.b64encode(value)


print("password        :", password)
print("hash_generated  :", hash_generated)


t0 = time.monotonic()
guessed_password = guess_password(salt, iterations, value)
print("guessed_password:", guessed_password)
t1 = time.monotonic()
print("Time elapsed (s):",t1 - t0)

# If left with the usual iteractions at 45454 this routine will take 8.6s
#  if iteractions is reduced to 1, then it takes 0.014999999999417923s to break the password













