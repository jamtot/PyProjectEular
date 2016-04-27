#-----first attempt-----------------------------------------------------
from itertools import permutations
def is_perfect_cube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x

def findcubicperms(n=3):
    i=1
    cubicperms=0
    while cubicperms<n:
        i+=1
        #gets caught up on 1000, because permutations involve 1000 6 times
        cubicperms=sum([1 for p in permutations(str(i)) 
                if is_perfect_cube(int("".join(list(p))))])
    return i
#-----------------------------------------------------------------------

from collections import defaultdict
def makecubedict(n=3):
    cubedict = defaultdict(list)
    i,result,newentry = 1,0,0
    while result < n:
        newentry = int("".join(sorted(list(str(i**3)), reverse=True)))
        cubedict[newentry]+=[i]
        i+=1
        result = len(cubedict[newentry])
    return cubedict[newentry][0]**3

if __name__ == "__main__":
    assert makecubedict() == 41063625
    print makecubedict(5) # 127035954683
