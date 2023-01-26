# In order to understand the RSA basics we need to understand some of the mathematical foundations behind it.
# Starting with the Phi function.
#  φ(n) -> Counts how many integers are less or equal to N that do not share any common factor with N
#  e.g.: φ(8) = [1], 2, [3], 4, [5], 6, [7], 8 ->  φ(8) = 4 , there are 4 numbers less or equal to 8 that
#  do not share a common factor with 8
#  
# The φ(n) function is hard to calculate, except in one case, when φ(n) is for a prime number, since prime
# numbers have no factor greater than 1.
# The φ(n) of any prime number is:
#  φ(p) = (p-1)
# 
# For instance: φ(7) = [1],[2],[3],[4],[5],[6],7 -> φ(7) = 6
#  another example: φ(21377) = 21376
#  
# Also, we can derive some properties such as: φ(a*b) = φ(a) * φ(b)
#  Consider the prime numbers p1 and p2, and n = p1*p2
# 
#  E.g.: p1=5  ,  p2=11  find φ(n) where n = p1*p2
#   n = 5 * 11 = 55
#   φ(5)  = (5-1)  = 4
#   φ(11) = (11-1) = 10
#   φ(55) = 4*10   = 40
#   ---------------
#   p1 = 7 , p2 = 11
#   p1*p2 = 11 * 7 = 77
#   φ(77) = 6 * 10 = 60
#   
# Now for the next part we need to determine some extra mathematical foundations:
# 
# i.   1 mod n  = 1
# 
# ii.  m^(φ(n)) = 1 mod n
# 
# iii. (1^k)    = 1
# 
# iv.  m^(φ(n)*k) = 1 mod n
# 
# v.   1*m = m
# 
# So... m*m^(φ(n)*k) = m*1 mod n   and this can be simplified as:
#       m^((φ(n)*k)+1) = m mod n -> m^(φ(n)*k+1) = m mod n
# 	  
# And m^(e*d) = m mod n
#     (e*d) = k*φ(n) + 1
# 	
# 	d = (k*φ(n) + 1) / e



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


# def factor(n):
#     for p in range(2, n):
#         if n % p == 0:
#             return p, n//p




#---------------------------------------------------------------            

print("\n\n------------------------------------------------")

print("Key generation done by Alice (secret)")
print("Step 1: Generate 2 distinct primes")
min_value = 300
p = get_prime(min_value, min_value*2)
q = p
while q == p:
    q = get_prime(min_value, min_value*2)

# p = 433
# q = 577

print("   p:", p,", q:", q)

print("Step 2: Compute n = p*q")
n = p*q
print("   n:",n)

print("Step 3: Compute lambda(n) (lcm(n) = λ(n) = lcm(λ(p),λ(q)), λ(p)=p-1, lcm(a,b) = |ab|/gcd(a,b))")
#   In the original RSA paper,[1] the Euler totient function φ(n) = (p − 1)(q − 1) is used instead 
#   of λ(n) for calculating the private exponent d. Since φ(n) is always divisible by λ(n), the 
#   algorithm works as well. The possibility of using Euler totient function results also from 
#   Lagrange's theorem applied to the multiplicative group of integers modulo pq. Thus any d 
#   satisfying d⋅e ≡ 1 (mod φ(n)) also satisfies d⋅e ≡ 1 (mod λ(n)). However, computing 
#   d modulo φ(n) will sometimes yield a result that is larger than necessary (i.e. d > λ(n)). 
#   Most of the implementations of RSA will accept exponents generated using either method (if they 
#   use the private exponent d at all, rather than using the optimized decryption method based on 
#   the Chinese remainder theorem described below), but some standards such as FIPS 186-4 may 
#   require that d < λ(n). Any "oversized" private exponents not meeting this criterion may always 
#   be reduced modulo λ(n) to obtain a smaller equivalent exponent.
lambda_n = lcm(p-1, q-1)
print("   Lambda n", lambda_n)

print("Step 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1")
e = get_e(lambda_n)
print("   Public exponent", e)

print("Step 5: solve for d the equation d⋅e ≡ 1 (mod λ(n))")
d = get_d(e, lambda_n)
print("   Secret exponent", d)

print("   Done with key generation.")
print("   Public Keys:  (e,n) -> (", e, "," , n , ")")
print("   Private Keys: (d)   -> (", d, ")")


print("\nThis is Bob wanting to send a message:")
bob_m = 117
bob_c = bob_m**e % n

print("Bob's message:",bob_m,"Bob sends:", bob_c)

print("This is Alice decrypting the cipher")
alice_m = bob_c**d % n

print("Alice receives this message:", alice_m)