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
#--------------------------------------------------------
#
# Another example.
# Define 'p' and 'q'
# p = 2  ,  q = 7
# Define n, where n = p*q
# n = 2*7 = 14
# Define φ(n) - see explanation above - where φ(n) = (p-1)*(q-1)
#  φ(n) = (2-1)*(7-1) = (1)*(6) = 6
# Define 'e'. Where 'e' must be less than φ(n), and be a co-prime with φ(n) and n (e.g.: co prime with 6 and 14)
#  meaning 'e' should not share any co-factor with φ(n) and n except for 1.
#  In this case we could have the numbers (2,3,4,5) - and then we eliminate the even numbers, we are left with
#  (3,5) - and 3 is a co-factor of 6. So our choice is 5
# e = 5
# Solve 'd' in the equation (e.d) mod φ(n) = 1. You can pick any 'd'
#  you could try loop though possible numbers and checking the ones that might solve the equation, e.g.:
#  (5*1) mod 6 => 5 mod 6 = 1 (OK)
#  (5*2) mod 6 => 10 mod 6 = 4 (WRONG)
#  (5*...) mod 6 => ...
#  (5*11) mod 6 => 55 mod 6 = 1 (OK)
#  (5*...) mod 6 => ...
#  (5*17) mod 6 => 85 mod 6 = 1 (OK)
#  (5*...) mod 6 => ...
# So in this example the viable options would be 'd' = [5,11,17]
# We will pick 11
# d = 11
# So far the data we have is:
#   p = 2    , q    = 7
#   n = 14   , φ(n) = 6
#   e = 5    , d    = 11
#
# Public Keys  (e,n) -> (5 , 14)
# Private Keys (d,n) -> (11, 14)
#
# Consider we want to send a message where A=1, B=2, C=3, ...
# And the first char is B=2
# we would calculate:
#  m^(e) mod n = c  -> 2^(5) mod 14 -> 32 mod 14 = 4 = 'D'
#
# And then decrypt using:
#  m = c^(d) mod n -> 4^(11) mod 14 = 4194304 mod 14 = 2 = 'B'


import math
import random
import sys

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


def get_e(phi_n , n):
    for e in range(2, phi_n):
        if (math.gcd(e, phi_n) == 1) and (math.gcd(e, n) == 1):
            return e
    return False


def get_d_min_d(e, phi_n, min_d = 2, max_d = sys.maxsize):
    for d in range(min_d, max_d):
        if d*e % phi_n == 1:
            return d
    return False    




#---------------------------------------------------------------            

print("\n\n------------------------------------------------")

print("Step 1: Get 'p' and 'q'")
min_value = 300
p = get_prime(min_value, min_value*2)
q = p
while q == p:
    q = get_prime(min_value, min_value*2)

# p = 2
# q = 7

print("   p:", p,", q:", q)

print("Step 2: Compute n = p*q")
n = p*q
print("   n:",n)

print("Step 3: Compute φ(n)")
phi_n = (p-1)*(q-1)
print("   phi_n:",phi_n)

print("Step 4: Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1 and gcd(e, n) = 1")
e = get_e(phi_n, n)
print("   Public exponent:", e)

print("Step 5: solve for d the equation (d*e) mod φ(n) ≡ 1")
d = get_d_min_d(e, phi_n, min_d = (e+1))
# d = get_d_min_d(e, phi_n)
print("   Secret exponent", d)

print("Step 6: Revise the data gathered so far")

print("   Public Keys:  (e,n) -> (", e, "," , n , ")")
print("   Private Keys: (d)   -> (", d, ")")


print("\nThis is Bob wanting to send a message:")
bob_m = 98
bob_c = (bob_m**e) % n

print("Bob's message:",bob_m,"Bob's cipher :", bob_c)

print("This is Alice decrypting the cipher")
alice_m = bob_c**d % n

print("Alice receives this message:", alice_m)