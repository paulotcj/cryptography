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

def find_primes(start, count):
    primes = []
    while count > 0:
        if is_prime(start):
            # print(start)
            primes.append(start)
            count-=1

        start+=1

    for i in range( len(primes) ):
        print(primes[i])
        

def get_prime(min, max):
    while True:
        randNum = random.randrange(min, max)
        if is_prime(randNum):
            return randNum

def is_generator(g, p):
    for i in range(1, p-1):
        if (g**i) % p == 1:
            return False

    return True

def get_all_generators(p):
    generators = []
    for g in range(2,p):
        if is_generator(g,p):
            generators.append(g)
            print("new generator: ",g)

    return generators

def get_generator(p):
    for g in range(2,p):
        if is_generator(g,p):
            return g

print("\n\n------------------------------------------------")
print("diffie-Hellman Key Exchange start")
floor = 10_000
# print( get_prime(floor, floor*2) )
p = get_prime(floor, floor*2)
g = get_generator(p)
print("p:", p , ", g: ", g)

#------------------------------------------------------------
#experimental area - start
# find all primes given a start and a count down
# find_primes(2,1_000)

#find all generators given the prime number P
# generators = get_all_generators(p)
# print(generators)
#experimental area - end
#------------------------------------------------------------



#Alice
a = random.randrange(0,p)
g_a = (g**a) % p
#Alice send this out in public
print("Alice g_a: ", g_a)

#Bob
b = random.randrange(0,p)
g_b = (g**b) % p
#Bob send this out in public
print("Bob g_b: ", g_b)

print("The numbers below should be the same, they are the shared key")
# Back to Alice
g_ab = (g_b**a) % p
print("Alice g_ab: ", g_ab)

#Back to Bob
g_ba = (g_a**b) % p
print("Bob g_ba: ", g_ab)
