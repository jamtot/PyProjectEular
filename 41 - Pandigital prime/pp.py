import math

#sieve of atkin
def atkin(ceiling):
    is_prime = dict([(i, False) for i in range(5, ceiling+1)])
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

def check_pan(primes):
    panprimes = []
    pandigit = "123456789"
    pandigit = sorted(pandigit)
    for p in primes:
        #print sorted(str(p))
        #print pandigit[:len(str(p))]
        if sorted(str(p)) == pandigit[:len(str(p))]:
            panprimes.append(p)
    return panprimes
            

if __name__ == "__main__":
    # not going to 8 or 9 digit pandigitals
    # because 1+2+3...8+9 = 45 (divisible by 3)
    # and 1+2+3...7+8 = 36 (divisible by 3)
    # so there exists no prime 8 or 9 digit pandigital
    # numbers
    primes, is_prime = atkin(7654321)
    pprimes = check_pan(primes)
    print pprimes # 7652413
