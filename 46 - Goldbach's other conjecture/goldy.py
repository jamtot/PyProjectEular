def primecompgen(composites = True):
    primes = [2,3]
    composites = []
    if composites == False:
        yield 2
        yield 3
    num = 3
    while True:
        prime = True
        num+=2
        for p in primes:
            if num%p == 0:
                composites.append(num)
                prime = False
            
        if prime:
            primes.append(num)
            if composites == False: yield num 
        else: 
            if composites: yield num, primes

def sqrdubgen():
    num = 1
    while True:
        sqrdub = (num*num)*2
        yield sqrdub
        num+=1


if __name__ == "__main__":
    pg = primecompgen()
    sbgen = sqrdubgen()
    sqrdubs = [sbgen.next()]
    while True:
        comp,primes = pg.next()
        breakme = False
        while sqrdubs[-1] < comp:
            sqrdubs.append(sbgen.next())
        for p in primes:
            for sd in sqrdubs:
                if p+sd == comp:
                    breakme = True
                    break
            if breakme:
                break
        if breakme:
            continue
        break
    print "Non-conforming number found. It is %d." % comp # it's 5777
        
        
