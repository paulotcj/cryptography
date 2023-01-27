import hashlib

m = "This is the hash value message".encode()

sha256 = hashlib.sha256()
sha256.update(m)
d = sha256.digest()

print("\n\n------------------------------------\nd         :",d)

m_new = "This is the hash value message".encode()
sha256_new = hashlib.sha256()
sha256_new.update(m_new)
d_new = sha256_new.digest()

print("d_new     :",d_new)


l = list(m)
l[0] = l[0] ^ 1
m_mod = bytes(l)
sha256_mod = hashlib.sha256()
sha256_mod.update(m_mod)
d_mod = sha256_mod.digest()

print("d_mod     :",d_mod)
print("m_mod     :",m_mod)
print("m         :",m)
