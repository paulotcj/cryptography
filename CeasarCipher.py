def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        #                  0    n  %     26       -> this will be (0+n), (1+n), (2+n), ...
        key[c] = letters[(cnt + n) % len(letters)] 
        # and eventually we might have: 25 % 26 = 15, 26 % 26 = 0, 27 % 26 = 1, 28 % 26 = 2 , 

        cnt += 1
    return key


def get_decryption_key(key):
    dkey = {}

    for c in key:
        # suppose c = 'A' and key['A'] = 'D' , then -> dkey[key[c]] = c -> dkey[ 'D' ] = 'A'
        dkey[key[c]] = c 

    return dkey

    
def encrypt(key, message):
    cipher = ""
    
    for c in message:
        if c in key:
            cipher += key[c] #get the mapped char
        else: #other characters
            cipher += c
    
    return cipher


# script tests - start
key = generate_key(3)
print(key)
message = "HELLO WORLD ENCRYPT THIS STRING"
cipher = encrypt(key, message)
print(cipher)
dkey = get_decryption_key(key)
print(dkey)

#try to break the encryption by brute force
# one of the outputs below is the answer
for i in range(26):
     dkey = generate_key(i)
     message = encrypt(dkey, cipher)
     print(message)


