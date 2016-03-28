def distpow(alow, ahigh, blow, bhigh):
    nlist=[]
    for a in xrange(alow, ahigh+1):
        for b in xrange(blow, bhigh+1):
            n = a**b
            if n not in nlist:
                nlist.append(n)
    return len(nlist)

assert(distpow(2,5,2,5)==15)
print distpow(2,100,2,100)
