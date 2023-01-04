import random


def generate_key_stream(n):
    return bytes( [random.randrange(0, 256) for i in range(n)] )


def xor_bytes(key_stream, message):
    minLength = min( len(key_stream), len(message) )
    return bytes( [ key_stream[i] ^ message[i] for i in range(minLength) ] )

#-------------------------------------

# this is done by your enemy
message = "DO ATTACK"
message = message.encode()
#---
key_stream = generate_key_stream(len(message)) #creates a random key stream
cipher = xor_bytes(key_stream, message)

print("message: ", message)
print("key_stream: ", key_stream)
print("cipher: ",cipher)
print("decripted message: ", xor_bytes(key_stream=key_stream, message=cipher)  )
#-------------------------------------

print("\n\n")
#let's try to create an arbitraty key_stream that could translate "DO ATTACK" to "NO ATTACK"
message2 = "NO ATTACK"
message2 = message2.encode()
#---
#gets the XOR 'guess stream' based on the string 'NO ATTACK' - remember this is incorrect and we
# are forcing a wrong outcome here by using the wrong key stream [b'\x1fUX\xf2\r\xf2<\x01\xfd']
guess_key_stream = xor_bytes(message2, cipher) 
print("guess_key_stream:", guess_key_stream)

#remember cipher is the encrypted message, which originally was 'DO ATTACK'
print("guess of the decripted message: ", xor_bytes(key_stream=guess_key_stream, message=cipher)  )

