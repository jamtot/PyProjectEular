# -*- coding: utf8 -*-
#Pn=n(3n−1)/2
import time

def pentagonal(n):
    return (n*(3*n-1)) / 2

def pengen(n=1):
    while True:
        yield pentagonal(n)
        n+=1

def checkpen(num, pencache, pgen):
    while num > pencache[-1]:
        pencache.append(pgen.next())

    if num in pencache:
        return True
    else: return False

def findD():
    start = time.time()
    pgen = pengen()
    pencache = [pgen.next(), pgen.next()]
    i = 0
    while True:
        curstop = len(pencache)
        for x in pencache:
            for y in pencache[i:]:
                if x is not y:
                    if checkpen(abs(x-y), pencache, pgen):
                        if checkpen(x+y, pencache, pgen):
                            print "This took %r secs."% (time.time() - start)
                            return abs(x-y)
        i = curstop
        pencache.append(pgen.next())

if __name__=="__main__":
    pen10 = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    assert [(pentagonal(i+1)==pen10[i]) for i in xrange(len(pen10))] == [True]*len(pen10)
    #This took 17.158409118652344 secs.
    print findD()#5482660
                 

