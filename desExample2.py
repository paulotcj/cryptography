from pyDes import *


alice_message = "Give Bob:   10$"
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


#this is the bank decrypting the message
bank_k = des(key = alice_key, mode = ECB, IV = alice_iv, pad=None, padmode=PAD_PKCS5)
bank_message = bank_k.decrypt(alice_cipher)
print("Decrypted (bank): ", bank_message)

