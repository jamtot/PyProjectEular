from itertools import permutations
import math
import random

def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1
# got from http://blog.dreamshire.com/common-functions-routines-project-euler/#miller_rabin

def primesieve(ceiling, floor=0):
    is_prime = [True for i in range(ceiling)]
    for i in xrange(2,int(math.sqrt(ceiling))+1):
        if is_prime[i] is True:
            j,k = i**2, 1
            for j in xrange(i*i, ceiling, i):
                is_prime[j] = False
    return [i for i in xrange(2,ceiling) if is_prime[i] == True and i >= floor]  
  
def check_all_prime(primelist):
    return all(miller_rabin(int(str(p[0]) + str(p[1]))) for p in permutations(primelist, 2))   

def make_list(primes, plist=[], list_size=5):
    if len(plist) == list_size:
        return plist
    for i in xrange(len(primes)):
        if (primes[i] > plist[-1]) and (check_all_prime(plist+[primes[i]])):
            new_plist = make_list(primes[i:], plist+[primes[i]], list_size)
            if new_plist:#if list is initialised
                return new_plist
    return False

if __name__ == "__main__":
    # arbitrarily chosen ceiling of 10k, generating primes on the go took up more time
    primes = primesieve(10000) 
    plist = []
    list_len = 5
    while not plist:#while plist is empty or false
        # stops at first answer found, which happens to be right
        # so this solution isn't the best, is too hacky for my liking
        plist = make_list(primes, [primes.pop(0)], list_len)
    print sum(plist) # 26033

