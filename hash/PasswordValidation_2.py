import hashlib
import base64

print("\n\nThe effects of using salt in hashing functions")

iterations = 45454
# salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
salt = "".encode()
# SALTED-SHA512-PBKDF2
password = "password".encode()
# Insert code here
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
hash_generated = base64.b64encode(value)
#---------------------------
another_password = "password".encode()
value_2 = hashlib.pbkdf2_hmac("sha512", another_password, salt, iterations, dklen=128)
hash_generated_2 = base64.b64encode(value_2)
#---------------------------

print("password        : ", password)
print("another_password: ", another_password)
print("hash_generated  :", hash_generated)
print("hash_generated_2:", hash_generated_2)

print("\nhash_generated == hash_generated_2: ", (hash_generated == hash_generated_2))

#If the same salt, or no salt is used across all users, if 2 or more users have the same password, the output of their
# hash function will be the same. And considering that people might use the same password such as:
# [password, admin, 123456, love, pwd]
# One could exploit this by keying in a random password, seeing the output and checking the hash output of any given
#  user in order to guess user's password

