import hashlib
import base64

print("\n\nThe effects of using salt in hashing functions")

iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
# SALTED-SHA512-PBKDF2
password = "password".encode()
# Insert code here
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
hash_generated = base64.b64encode(value)


