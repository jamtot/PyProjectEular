# -*- coding: utf8 -*-
#Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
#Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

def triangulate(n):
    return (n*(n+1))/2

def pentagulate(n):
    return (n*((3*n)-1))/2

def hexagulate(n):
    return n*((2*n)-1)

def trigen(n=1):
    while True:
        yield triangulate(n)
        n+=1

def pengen(n=1):
    while True:
        yield pentagulate(n)
        n+=1

def hexgen(n=1):
    while True:
        yield hexagulate(n)
        n+=1

def findnum():
    # start from just after known number
    tgen = trigen(286)
    pgen = pengen(166)
    hgen = hexgen(143)

    pcache = [pgen.next()]
    hcache = [hgen.next()]

    while True:
        trinum = tgen.next()
        if checkpen(trinum, pcache, pgen):
            if checkhex(trinum, hcache, hgen):
                return trinum
        
        

def checkpen(num, pcache, pgen):
    while num > pcache[-1]:
        pcache.append(pgen.next())
    if num in pcache:
        return True
    else: return False

def checkhex(num, hcache, hgen):
    while num > hcache[-1]:
        hcache.append(hgen.next())
    if num in hcache:
        return True
    else: return False

if __name__=="__main__":
    assert [triangulate(n+1) for n in xrange(5)] == [1, 3, 6, 10, 15]
    assert [pentagulate(n+1) for n in xrange(5)] == [1, 5, 12, 22, 35]
    assert [hexagulate(n+1) for n in xrange(5)] == [1, 6, 15, 28, 45]

    print findnum()
