import math 
import re

def primesieve(ceiling, floor=0):
    is_prime = [True for i in range(ceiling)]
    for i in xrange(2,int(math.sqrt(ceiling))+1):
        if is_prime[i] is True:
            j,k = i**2, 1
            for j in xrange(i*i, ceiling, i):
                is_prime[j] = False
    return [i for i in xrange(2,ceiling) if is_prime[i] == True and i >= floor]


def findfam(primes, matches=8, samesies=3):
    currprime=''
    numbers=''.join(map(str, range(10)))
    for prime in primes:
        matchingprimes=0
        for digit in prime:
            if prime.count(digit) == samesies:
                currprime=prime
                for num in numbers:
                    if (re.sub(digit,num,prime) in primes):
                        matchingprimes+=1
                if matchingprimes==matches:
                    return prime
                break

            
if __name__ == "__main__":
    print findfam(map(str,primesieve(1000000, 100000)))#121313
