import math

#sieve of atkin
def atkin(ceiling):
    is_prime = dict([(i, False) for i in range(5, ceiling+1)])
    is_prime[1] = False
    is_prime[2] = True
    is_prime[3] = True
    is_prime[4] = False
    for x in range(1, int(math.sqrt(ceiling))+1):
        for y in range(1, int(math.sqrt(ceiling))+1):
            n = 4*x**2 + y**2
            if (n <= ceiling) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= ceiling) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= ceiling) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(ceiling))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= ceiling):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(ceiling + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes, is_prime

def cycleprimes(primes, is_prime):
    cps = []
    for prime in primes: 
        cyclical = True
        prime = str(prime)
        cprime = prime
        for x in xrange(len(prime)):
            cprime = cprime[1:]+cprime[0]
            if not is_prime[int(cprime)]:
                cyclical = False
        if cyclical: 
            cps.append(prime)
    return len(cps), cps

    
if __name__=="__main__":
    
    primes, is_prime = atkin(1000000)
    print cycleprimes(primes, is_prime) # 55 
