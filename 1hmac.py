# HMAC is somewhat a similar principle to message signature, but while message signature
# there is no shared key, with HMAC both parties have prior knowledge of a common secret
# shared key
# So if Alice wants to send a message to Bob, she will use her private secret key and her
#  message to hash out a MAC signature, then send the message to Bob. Bob in his turn
#  will use the message and the MAC to authenticate the message using the shared secret key

import hashlib

# Alice and Bob share a secret key
secret_key = "secret key".encode()
secret_key_alice = secret_key
secret_key_bob = secret_key
#-----------------------------

# Alice wants to compute a MAC
m_alice = "Hey Bob. You are awesome".encode()

sha256_alice = hashlib.sha256()
sha256_alice.update(secret_key_alice)
sha256_alice.update(m_alice)

hmac_alice = sha256_alice.digest()

print("Message:", m_alice, ", hmac_alice:", hmac_alice)

#Bob receives the message and validate the HMAC
sha256_bob = hashlib.sha256()
sha256_bob.update(secret_key_bob)
sha256_bob.update(m_alice)
hmac_bob = sha256_bob.digest()

print("Message:", m_alice, ", hmac_bob  :", hmac_bob)
