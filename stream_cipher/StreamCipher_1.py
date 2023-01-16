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






print("\n------------------------------------------")


corruptedMessage()



# Alice end
key = KeyStream(10)
message = "Send Bob:   10$".encode()
print("message: ", message, "|", list(message))
cipher = encrypt(key, message)
print("cipher: ", cipher, "|", list(cipher))
print("key bytes: ", list( getKeyBytes(10,len(message)) ) )


# This is the poor transmission
# print( transmit(message,  5) )

# Bob end
cipher = modification(cipher)

# Bank
bank_key = KeyStream(10)
bank_message = encrypt(bank_key, cipher)
print("bank message: ", bank_message)

