# a**2 + b**2 = c**2
# a + b + c = 1000
# a < b < c

import time

class BreakOut(Exception):pass

"""start = time.time()

try:
    for a in xrange(1,1000):
        for b in xrange(1, 1000):
            for c in xrange(1,1000):
                if (a+b+c==1000):
                    if (a**2+b**2==c**2):
                        print "Product = %d"%(a*b*c)
                        print "A: %d B: %d C: %d"%(a,b,c)
                        raise BreakOut
except BreakOut:
    pass

# Product = 31875000
# A: 200 B: 375 C: 425
# Sol 1 takes: 16.16309380531311

elapsed = time.time()
print "Sol 1 takes: %r" % (elapsed - start)

start2 = time.time()
try:
    for r in xrange(1,1000):
        for s in xrange(1, 1000):
            for t in xrange(1,1000):
                if r**2 == 2*s*t:
                    x = r+s
                    y = r+t
                    z = r+s+t  
                    if x+y+z == 1000:
                        print "Answer found!"
                        print "Product= %d"%(x*y*z)
                        print " x: %d, y: %d, z: %d " % (x, y, z)
                        raise BreakOut
except BreakOut:
    pass

elapsed2 = time.time()
print "Sol 2 takes: %r" % (elapsed2 - start2)"""
# Answer found!
# Product= 31875000
# x: 200, y: 375, z: 425 
# Sol 2 takes: 23.333422899246216

# Euclid's formula
# M&N
# A = M**2 - N**2
# B = (M*N)*2
# C = M**2 + N**2

start3 = time.time()

m = 0
notfound = True
while notfound:
    n = 0
    while n<m:
        if (m>n):
            a = (m**2) - (n**2)
            b = (m*n)*2
            c = (m**2) + (n**2)
            if (a+b+c == 1000):
                print "Product = %d"%(a*b*c)
                print "A: %d B: %d C: %d"%(a,b,c)
                notfound = False
                break
        n+=1
    m+=1
elapsed3 = time.time()
print "Sol 3 takes: %r" % (elapsed3 - start3)

# Product = 31875000
# A: 375 B: 200 C: 425
# Sol takes: 0.0003540515899658203
# daaaaaamn son where'd ya find this
