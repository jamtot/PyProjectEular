import math

# using https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_and_variants
def primesieve(ceiling):
    is_prime = [True for i in range(ceiling)]
    for i in xrange(2,int(math.sqrt(ceiling))+1):
        if is_prime[i] is True:
            j,k = i**2, 1
            for j in xrange(i*i, ceiling, i):
                is_prime[j] = False
    return [i for i in xrange(2,ceiling) if is_prime[i] == True]

def findconsec(primes, ceiling):
    seq = []
    for i in xrange(4):#len(primes)): # same answer for both...?
        curseq = primes[i:]
        total, j = 0, 0
        for p in curseq:
            total+=p
            if total > ceiling:
                break
            j+=1
            if total in primes:
                newseq = curseq[:j]
                if len(newseq) > len(seq):
                    seq = newseq
    return sum(seq)
            
            

if __name__ == "__main__":
    assert findconsec(primesieve(100), 100) == 41
    assert findconsec(primesieve(1000), 1000) == 953
    ceil = 1000000
    print findconsec(primesieve(ceil), ceil) # 997651
    
