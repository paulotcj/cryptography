from pyDes import *
import random

message = "01234567"
key_11 = random.randrange(0, 256)
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])
key_21 = random.randrange(0, 256)
key_2 = bytes([key_21, 0, 0, 0, 0, 0, 0, 0])
iv = bytes([0]*8)

k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)

# Alice sending the encrypted message
cipher = k1.encrypt(k2.encrypt(message))
print("\n\n-------------------------------------------------")
print("Key 11:", key_11)
print("Key 21:", key_21)
print("Encrypted", cipher)

# This is Bob
message = k2.decrypt(k1.decrypt(cipher))
print("Decrypted:", message)

# Eve's attack on Double DES
#------------------------------------------
# This attack method consists of trying both ends of the double DES and requires knowledge of the original message
# First we will encrypt the original message and create the first encrypted DES layer. Then
#  we will approach by the other end, and using the final cipher, we will try to defeat the second DES layer
#  by trying to decrypt and checking if this decryption matches anything in the lookup table. If it does
#  if means we found a combination that will decrypt the second layer matching to an encrypted first layer
#  and this first layer has a key mapped to it
#  This algorithm avoids trying n^2 combinations. By attacking both ends we reduce the complexity to 2n
#
# And based on this attack that's the reason to use 3DES, as it would make any attempts to guess the keys
#  much more difficult


print("\nChecking the state of the message: ", message)

# having access to the original message we loop through possible keys and map them to an encrypted message
lookup = {}
for i in range(256):
    key = bytes([i,0,0,0,0,0,0,0])
    k = des(key = key, mode=ECB, IV=iv, pad=None, padmode=PAD_PKCS5)
    lookup[k.encrypt(message)] = i

# now we attack from the other end. Using the cipher we want to go through possible
# keys and see which one will decrypt the cipher to the values we are looking for
for i in range(256):
    key = bytes([i,0,0,0,0,0,0,0])
    k = des(key = key, mode=ECB, IV=iv, pad=None, padmode=PAD_PKCS5)
    if k.decrypt(cipher) in lookup:
        print("    Note the least significant byte might be off, as it's often ignored by DES")
        print("Key 11: ", i)
        print("Key 21: ", lookup[ k.decrypt(cipher) ] )
        key_1 = bytes([i,0,0,0,0,0,0,0])
        key_2 = bytes([lookup[ k.decrypt(cipher) ],0,0,0,0,0,0,0])

        k1 = des(key = key_1, mode=ECB, IV=iv, pad=None, padmode=PAD_PKCS5)
        k2 = des(key = key_2, mode=ECB, IV=iv, pad=None, padmode=PAD_PKCS5)
        print("Eve break double DES", k2.decrypt( k1.decrypt(cipher)  )  )

        break