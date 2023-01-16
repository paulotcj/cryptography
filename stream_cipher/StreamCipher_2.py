import random

#-------------------------------------------------
class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256

#-------------------------------------------------

def corruptedMessage():
    print("Corrupted message example")
    key_corr = KeyStream(10)
    message_corr = "Hello World - Stream Cipher corruption test".encode()
    print("message_corr: ",message_corr)
    cipher_corr = encrypt(key_corr, message_corr)

    cipher_corr = transmit(cipher_corr,  9)

    receiver_key_corr = KeyStream(10)
    receiver_message_corr = encrypt(receiver_key_corr, cipher_corr)
    print("received message corrupted: ", receiver_message_corr)
    print("-----")

def encrypt(key, message):
    returnbytes = bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])
    return returnbytes
    


def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2**random.randrange(0,8)

        b.append(c)

    return bytes(b)

def modification(cipher):
    mod = [0]*len(cipher)
    #ord -> Return the integer that represents the character "h": x = ord("h")
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')

    return bytes( [ mod[i] ^ cipher[i] for i in range(len(cipher)) ] )

def getKeyBytes(keySeed, length):
    key = KeyStream(keySeed)
    bytesresult = bytes( key.get_key_byte() for i in range(length) )

    return bytesresult

def get_key(message, cipher):
    return bytes([ message[i] ^ cipher[i] for i in range(len(cipher)) ])

def crack(key_stream, cipher):
    length = min( len(key_stream) , len(cipher) )

    return bytes( [ key_stream[i] ^ cipher[i] for i in range(length) ] )


print("\n------------------------------------------")


#Eve message to Alice
eve_message = "Eve message to Alice - secret info included in this message".encode()

#Alice
alice_key = KeyStream(10)
alice_message = eve_message
print("alice_message: ",alice_message)
alice_cipher = encrypt(alice_key, alice_message)
print("alice_cipher: ",alice_cipher)

#Bob
bob_key = KeyStream(10)
bob_message = encrypt(bob_key, alice_cipher)
print("bob_message: ", bob_message)

print("\n------------------------------------------")
#Eve 2
eves_key_stream = get_key(eve_message, alice_cipher)
print("eves_key_stream: ", eves_key_stream)
proof_keybytes1 = getKeyBytes(10, len(eve_message))
print("proof_keybytes1: " , proof_keybytes1)
print("--------")

#Alice 2
alice_message2 = "Alea jacta est Bob".encode()
alice_key2 = KeyStream(10)
alice_cipher2 = encrypt(alice_key2, alice_message2)

#Bob 2
bob_key2 = KeyStream(10)
bob_message2 = encrypt(bob_key2, alice_cipher2)
print("bob_message2: ", bob_message2)

#Eve 3
eve_cracked_message = crack(eves_key_stream, alice_cipher2)
print("eve_cracked_message: ", eve_cracked_message)
print("Eve has cracked alice_cipher2 sent to Bob")
