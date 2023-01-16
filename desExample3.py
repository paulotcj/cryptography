from pyDes import *

def modify(cipher):
    mod = [0]*len(cipher)
    mod[8] = 1

    return bytes( [ mod[i] ^ cipher[i] for i in range(len(cipher)) ] )



alice_message = "Give Bob:   10$ and then add some extra text here for experimenting purposes"
alice_key = "DESCRYPT"
alice_iv = bytes([0]*8)
alice_k = des(key = alice_key, mode = ECB, IV = alice_iv, pad=None, padmode=PAD_PKCS5)

#Alice sending the encrypted message
alice_cipher = alice_k.encrypt(alice_message)

print("\n\n-------------------------------------------------")
print("Length of message (Alice): ", len(alice_message))
print("Length of cipher text (Alice): ", len(alice_cipher))
print("Message (Alice):", alice_message)
print("Encrypted (Alice): ", alice_cipher)


#Bob modifying the cipher text
alice_cipher = modify(alice_cipher)


#this is the bank decrypting the message
bank_k = des(key = alice_key, mode = ECB, IV = alice_iv, pad=None, padmode=PAD_PKCS5)
bank_message = bank_k.decrypt(alice_cipher)
print("Decrypted (bank): ", bank_message)

