#--- Miller-Rabin primality test----------------------------------------------------------------

import random
def miller_rabin(n):
    """
    Check n for primalty:  Example:

    >miller_rabin(162259276829213363391578010288127)    #Mersenne prime #11
    True

    Algorithm & Python source:
    http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)
    # above site now defunct
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
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

#------------------------------------------------------------------------------------------

# tried generating primes, took way too long
# tried a primesieve, couldn't generate high enough
# had to find something to test if a number was prime, found 
# the miller rabin function online

def newlayer(diagonals, primes):
    last = diagonals[-1]
    newgap = (last-diagonals[-2])+2
    for i in xrange(4):
        if miller_rabin(last+newgap):
            primes+=1
        diagonals.append(last+newgap)
        diagonals=diagonals[-4:]
        last = diagonals[-1]
    return diagonals, primes
    
def getsidelen(diags):
    return (diagonals[-1] - diagonals[-2]) + 1

def primecentage(primes, dlen):
    return float(primes)/float(dlen)

if __name__ == "__main__":
    diagonals = [1,3,5,7,9]
    primes=3
    diaglen = len(diagonals)
    while primecentage(primes, diaglen) > .10:
        diagonals, primes = newlayer(diagonals, primes)
        diaglen+=4
    print getsidelen(diagonals) # 26241


    
