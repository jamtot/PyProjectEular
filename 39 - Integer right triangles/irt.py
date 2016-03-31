# a^2 + b^2 = c^2
# a + b + c = p(erimeter)
# c = p-a-b
# a^2 + b^2 = (p-a-b)^2
# b = p(p-2a) / 2(p-a)

def checkValidTri(a,b,c):
    if (a**2 + b**2) == c**2:
        return True
    else: return False

def checkValidAns(a,b,c,p):
    if (a+b+c)==p:
        return True
    else: return False

def getC(a,b):
    return (a**2+b**2)**0.5


def genTri(p):
    sides = []
    for i in xrange(p):
        i = float(i)
        s = (p*(p-(2.*i))) / (2.*(p-i))
        if s.is_integer() and s > 0:
            sides.append(s)
    return sides

def findTris(sides, p):
    tris = []
    for val in sides:
        for valeile in sides:
            if val is not valeile:
                if chkVal(val, valeile, p):
                    tri = sorted([ val,valeile,getC(val,valeile) ])
                    if tri not in tris:
                        tris.append(tri)                    
    return len(tris)
                
def chkVal(a,b,p):
    c = (a**2+b**2)**0.5
    if (a+b+c) == p:
        return True
    else: return False
            
def findMax(limit):
    biggest = 0
    biggestP = 0
    for i in xrange(1, limit+1):
        cur = findTris(genTri(i), i)
        if cur > biggest:
            biggest = cur
            biggestP = i
    return biggestP #, biggest
        

if __name__ == "__main__":
    assert findTris(genTri(120), 120) == 3
    print findMax(1000) # 840, 8 combinations
