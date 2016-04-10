def primegen():
    primes = [2,3]
    yield 2
    yield 3
    num = 3
    while True:
        prime = True
        num+=2
        for p in primes:
            if num%p == 0:
                prime = False
            
        if prime:
            primes.append(num)
            yield num 

if __name__ == "__main__":
    pg = primegen()
    for i in xrange(1000):
        print pg.next()
