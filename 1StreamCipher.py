import random

#-------------------------------------------------
class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        #x(n+1) = (a*xn + c) mod m
        self.next = (1103515245 * self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        #"Another flaw specific to LCGs is the short period of the low-order bits when m is chosen to be a power of 2. 
        # This can be mitigated by using a modulus larger than the required output, and using the most significant bits of the state."
        return (self.rand()>>(23)) #% 256

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

def brute_force(plain, cipher):
    for k in range(2**31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
            else:
                return k

    return False




print("\n------------------------------------------")

secret_key = random.randrange(0,2*31)
#Alice
alice_key = KeyStream(secret_key)
alice_header = "MESSAGE: "
alice_message = alice_header + "My secret message to Bob"
alice_message = alice_message.encode()
alice_cipher = encrypt(alice_key, alice_message )

#Bob
bob_key = KeyStream(secret_key)
bob_message = encrypt(bob_key, alice_cipher)

#Eve
eve_bruteforce_key = brute_force(alice_header.encode(), alice_cipher )
eve_key = KeyStream(eve_bruteforce_key)
eve_message = encrypt(eve_key, alice_cipher)

print("secret_key: ", secret_key)
print("eve_bruteforce_key: ", eve_bruteforce_key)
print("alice original message: ",alice_message)
print("eve cracked the message: ", eve_message)

# print("alice_key.rand() % 256")
# for i in range(1000):
#     var_rand = alice_key.rand()
#     print('{: >14}'.format(var_rand), ", ", '{: >14}'.format(  (var_rand % 256) ), "|" )

# print("alice_key.rand() >> 23 % 256")
# for i in range(10_000):
#     var_rand = alice_key.rand()
#     var_rand_shiftted = var_rand >> 23
#     print(
#         '{: >14}'.format(var_rand), ", ", 
#         '{: >14}'.format(var_rand_shiftted), "$, ", 
#         '{: >14}'.format(  (var_rand_shiftted % 256) ), "|" 
#         )


# print("alice_key.rand()")
# for i in range(1000):
#     print(alice_key.rand()) 