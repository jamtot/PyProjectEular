def fac(n):
    if n == 1:
        return 1
    return n*fac(n-1)

def ifac(n):
    for i in xrange(n-1,0,-1):
        n*=i
    return n

def C(n, r):
    if r > n:
        return False
    return (ifac(n)) / (ifac(r) * ifac(n - r))

if __name__ == "__main__":
    print ifac(10)
    print C(5,3)
