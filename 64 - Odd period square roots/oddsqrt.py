import math

def contfrac(n):
    # using https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
    a0 = int(math.sqrt(n)) # floored srqt of n
    if a0*a0==n:
        return 0 # perfect square

    period = 0
    m=0
    d=1 
    a=a0

    while True:
        m = d*a-m
        d = (n-m*m)/d
        a = int((a0+m)/d)
        period+=1 # each run extends the repeated period
        if a == 2*a0: break

    if period%2==1: return 1 # odd
    return 0 # even

if __name__ == "__main__":
    assert sum([contfrac(n) for n in xrange(14)]) == 4
    print sum([contfrac(n) for n in xrange(10001)])
    
