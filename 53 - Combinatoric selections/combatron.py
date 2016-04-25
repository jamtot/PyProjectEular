def fac(n):
    if n == 1:
        return 1
    return n*fac(n-1)

def ifac(n):
    if n==0: return 1
    for i in xrange(n-1,0,-1):
        n*=i
    return n

def C(n, r):
    if r > n:
        return False
    return (ifac(n)) / (ifac(r) * ifac(n - r))

def greaterthanamil():
    greater=0
    for n in xrange(1,101):
        for r in xrange(1,n+1):
            if C(n,r)>1000000:
                greater+=1
    return greater

if __name__ == "__main__":
    print greaterthanamil() # 4075
            
