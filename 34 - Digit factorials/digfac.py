def fac(n):
    if n<0:
        n*=-1
    elif n == 0:
        return 1
    for i in xrange(n-1, 1, -1):
        n*=i
    return n

assert(fac(10) == 3628800)

def getnums(ceiling):
    digfacs = []
    for x in xrange(3, ceiling):
        nummy = str(x)
        summy = 0
        for num in nummy:
            summy+=fac(int(num))
        if summy == x:
            digfacs.append(x)

    return digfacs, sum(digfacs)

# we use 9!*7 as 9!*8 still results in 7 digits
print getnums(fac(9)*7) # ([145, 40585], 40730)
