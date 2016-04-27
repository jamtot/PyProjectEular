def tri(n):
    return (n*(n+1))/2

def sqr(n):
    return n*n

def pen(n):
    return (n*((3*n)-1))/2

def hexa(n):
    return n*((2*n)-1)

def hept(n):
    return (n*((5*n)-3))/2

def octa(n):
    return n*((3*n)-2)

def polygonal(poly, lower=999, upper=10000):
    #141 brings tri (smallest gaps) up to 10000
    return [poly(i) for i in xrange(141) if poly(i) > lower and poly(i) < upper]

def permcheck(i, perm, polys, cyclist=[]):
    if len(cyclist) == 6:
        found = (str(cyclist[-1])[-2:] == str(cyclist[0])[:2])
        if found:
            print sum(cyclist), cyclist
            return sum(cyclist)
    elif len(cyclist) < 1:
        for pnum in polys[perm[i]]:
            permcheck(i+1, perm, polys, cyclist+[pnum])
    elif len(cyclist)>0 and len(cyclist)<6:
        for pnum in polys[perm[i]]:
            if str(cyclist[-1])[-2:] == str(pnum)[:2]:
                permcheck(i+1, perm, polys, cyclist+[pnum])
    return

from itertools import permutations
def findcyclics():
    perms = [list(p) for p in permutations(range(6))]
    polys = [polygonal(tri),polygonal(sqr),polygonal(pen),
        polygonal(hexa),polygonal(hept),polygonal(octa)]

    for p in perms:
        permcheck(0, p, polys)

if __name__ == "__main__":
    findcyclics() # 28684
    
