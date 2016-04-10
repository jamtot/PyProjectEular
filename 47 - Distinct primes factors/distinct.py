def primegen():
    primes = [2,3]
    yield 2
    yield 3
    num = 3
    while True:
        prime = True
        num+=2
        for p in primes:
            if num%p==0:
                prime = False
                break
        if prime:
            primes.append(num)
            yield num

def primecompgen(composites = True):
    primes = [2,3]
    comps = []
    if not composites:
        yield 2
        yield 3
    num = 3
    while True:
        prime = True
        if composites: 
            num+=1
        else: 
            num+=2

        for p in primes:
            if num%p == 0:
                prime = False
                break
        if prime:
            primes.append(num)
            if not composites: 
                yield num 
        else: 
            comps.append(num)
            if composites:             
                yield num, primes
           
def factors(n, primes):
    factors = []
    if n < 1:
        factors
    while True:
        for p in primes:
            if p*p > n:
                if n == 1:
                    return factors
                else:
                    return factors + [(n, 1)]
            if n%p == 0:
                times = 1
                n=n/p
                while n%p == 0:
                    n = n/p
                    times += 1
                factors.append((p, times))
     
def findconsec(n):
    pcg = primecompgen()
    consecutive = 0
    prevcomp = 0
    while consecutive < n:
        comp, primes = pcg.next()
        if comp!=prevcomp+1: consecutive = 0 
        if len(factors(comp, primes))==n: 
            consecutive+=1
        else: consecutive = 0
        prevcomp = comp
    return (comp-n)+1
        

if __name__ == "__main__":
    assert findconsec(2) == 14
    assert findconsec(3) == 644
    print findconsec(4) # 134043


