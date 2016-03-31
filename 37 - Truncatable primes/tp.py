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


def checkTruncation(n, is_prime):
    nstr = str(n)
    ln = len(nstr)
    chks = (ln*2)-2
    hchks = chks/2
    for i in xrange(chks):
        index = i%(hchks)
        if i < hchks:
            if is_prime[int(nstr[index+1:])] == False:
                break
        else:
            if is_prime[int(nstr[:-(index+1)])] == False:
                break
    else:
        return True
    return False

def truncCheck(primes, is_prime):
    tprimes = []
    for p in primes:
        if p>9:
            if checkTruncation(p, is_prime):
                 tprimes.append(p)
    print tprimes
    return sum(tprimes)



#----------------------------------------
# attempt at generating up to the 11th to avoid
# arbitrary number as a limit
#----------------------------------------
def generate_truncated_primes():
    # starting with 2 as it's the only even prime
    primes = [2]
    trunprimes = []
    primedict={}
    primedict[2] = False
    # starting with 3
    current = 3
    while len(trunprimes) < 11:
        # make a list of bools for whether nunmbers are prime or not
        # by dividing them by previous primes
        prime_test = [current for i in primes if current%i == 0]
        # for every False (non divisible by previous primes) add to primes
        primes+= [] if prime_test else [current]
        # incrementing in 2s, as only odds should be tested
        primedict[current] = prime_test
        if not prime_test:
            if checkTruncationDict(current, primedict):
                trunprimes.append(current)
        current+= 2
    return trunprimes

def checkTruncationDict(n, primedict):
    if n > 9:
        nstr = str(n)
        ln = len(nstr)
        chks = (ln*2)-2
        hchks = chks/2
        for i in xrange(chks):
            index = i%(hchks)
            if i < hchks:
                if (int(nstr[index+1:])) in primedict:
                    if primedict[int(nstr[index+1:])]:
                        break
                else: break
            else:
                if (int(nstr[:-(index+1)])) in primedict:
                    if primedict[int(nstr[:-(index+1)])]:
                        break
                else: break
        else:
            return True
    return False

#---------------------------------------------


if __name__ == "__main__":

    # arbitrarily picked 1000000 as a ceiling
    # it worked, but I realise I should be
    # generating primes until I reach the desired
    # number
    primes, is_prime = atkin(1000000)

    assert checkTruncation(3797,is_prime)==True
    assert checkTruncation(1234,is_prime)==False

    print truncCheck(primes, is_prime)# 748317
    

    #print generate_truncated_primes()# never seems to stop running
    # okay just finished, took upwards of 10 minutes
