import hashlib
import math
import random

def is_prime(num):
    if num == 2: return True
    looped = False
    squareroot = math.isqrt(num) + 2
    for i in range(2,  squareroot ):
        looped = True
        if num % i == 0:
            return False

    returnval = (True if looped == True else False)
    return returnval

       

def get_prime(min, max):
    while True:
        randNum = random.randrange(min, max)
        if is_prime(randNum):
            return randNum

def lcm(a, b):
    return a*b//math.gcd(a, b)


def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False    


def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False


def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n//p


def modify_message(message):
    l = list(message)
    l[0] = l[0] ^ 1
    return bytes(l)



#---------------------------------------------------------------            

print("\n\n------------------------------------------------")


#-------------
min_value = 300
p = get_prime(min_value, min_value*2)
q = p
while q == p:
    q = get_prime(min_value, min_value*2)

# p = 433
# q = 577
print("   p:", p,", q:", q)
#-------------
n = p*q
print("   n:",n)
#-------------
lambda_n = lcm(p-1, q-1)
print("   lambda_n:", lambda_n)
#-------------
e = get_e(lambda_n)
print("   e:", e)
#-------------
d = get_d(e, lambda_n)
print("   d:", d)
#-------------
print("   Public Keys:  (e,n) -> (", e, "," , n , ")")
print("   Private Keys: (d)   -> (", d, ")")
#-------------

#---------------------------------------------------------------  

#override for our example
n = 170171
e = 5
d = 9677

#This is a message Alice wants to sign and send
m = "Bob you are awesome".encode()

print("Step 1: hash the message")
sha256 = hashlib.sha256()
sha256.update(m)
h = sha256.digest()
h = int.from_bytes(h,"big") % n # (mod n), so we can have a number easier to read and understand
print("h:", h)

print("Step 2: Decrypt the hash value")
sign = h**d % n
print("Step 3: Send message with signature")
print("message:", m, ",  sign:", sign)

print("Step 4: Verifying the signature")
sha256_bob = hashlib.sha256()
sha256_bob.update(m)
h_bob = sha256_bob.digest()
h_bob = int.from_bytes(h_bob, "big") % n
verification = sign**e % n
print(" Bob verifying the signature: verification:", verification, ",   h_bob:",h_bob)



print("\nNow Eve wants to change the message")
m_mod = modify_message(m)
print("m    :", m)
print("m_mod:", m_mod)


print("Verifying the signature of a fake/changed message")
sha256_bob2 = hashlib.sha256()
sha256_bob2.update(m_mod)
h_bob2 = sha256_bob2.digest()
h_bob2 = int.from_bytes(h_bob2, "big") % n
verification2 = sign**e % n
print(" Bob verifying the signature: verification:", verification2, ",   h_bob:",h_bob2)