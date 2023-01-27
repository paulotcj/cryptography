import hashlib
import base64

iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
# SALTED-SHA512-PBKDF2

password = "password".encode()
# Insert code here
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)

hash_stored = '1meJW2W6Zugz3rKm/n0yysV+5kvTccA7EuGejmyIX8X/MFoPxmmbCf3BE62h6wGyWk/TXR7pvXKgjrWjZyI+Fc3aKfv1LNQ0/Qrod3lVJcWd9V6Ygt+MYU8Eptv3uwDcYf6Z5UuF+Hg67rpoDAWhJrC1PEfL3vcN7IoBqC5NkIU='.encode()
hash_generated = base64.b64encode(value)

print(value)
print("hash_stored   :", hash_stored)
print("hash_generated:", hash_generated)

print("\nhash_generated == hash_stored: ", (hash_generated == hash_stored))
