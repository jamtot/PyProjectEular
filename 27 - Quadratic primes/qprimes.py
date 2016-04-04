import math

def atkin(pceiling, ispceiling):
    """a sieve of atkin representation that will return a list of
    primes to a certain number, and a dictionary listing whether a
    number is prime or not."""
    is_prime = dict([(i, False) for i in range(5, ispceiling+1)])
    is_prime[1] = False
    is_prime[2] = True
    is_prime[3] = True
    is_prime[4] = False
    for x in range(1, int(math.sqrt(ispceiling))+1):
        for y in range(1, int(math.sqrt(ispceiling))+1):
            n = 4*x**2 + y**2
            if (n <= ispceiling) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= ispceiling) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= ispceiling) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(ispceiling))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= ispceiling):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(pceiling + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes, is_prime

if __name__=="__main__":
    curmax = 0
    primes, is_prime = atkin(1000, 20000)
    
    #n^2 + an + b
    #n^2 + n + 41, works from 0 to 39, a = 1, b = 41
    #n^2 - 79n + 1601, works from 0 to 79, a = -79, b = 1601
    assert is_prime[41] == True
    assert is_prime[1601] == True
    # assuming b is prime and positive
    # b > a
    # a > -b

    for b in primes:
        for a in range(-b, b):
            # no need to start at n=0, as it will always be true
            # because b is prime
            n = 1 
            while is_prime[abs(n*n + a*n + b)]: 
                n += 1
            if n>curmax: 
                curmax = n
                p = a*b

    print "Product of a and b is %d"%p
    print "The sequence length is %d"%curmax
