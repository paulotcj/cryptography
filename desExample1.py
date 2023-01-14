from pyDes import *


message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0]*8)

#the following paramaters (ECB) will produce the same output for blocks with the same
# data
k = des(key = key, mode = ECB, iv = iv, pad=None, padmode=PAD_PKCS5)

#the following parameters (CBC) will produce different outputs for blocks with the same
# data. It will will XOR the iv array of bytes, working as a seed, and then the encrypted
# data will be used as a source to be XORed into the next block. Check block cipher: https://en.wikipedia.org/wiki/Block_cipher
k = des(key = key, mode = CBC, iv = iv, pad=None, padmode=PAD_PKCS5)

cipher = k.encrypt(message)

print("Length of message: ", len(message))
print("Length of cipher text: ", len(cipher))
print("Encrypted block 1: ", cipher[0:8])
print("Encrypted block 2: ", cipher[8:16])
print("Encrypted block 3: ", cipher[16:])
message2 = k.decrypt(cipher)
print("Decrypted: ", message2)

