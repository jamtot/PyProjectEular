#from problem 21
def factors(n):
    if n%2==1:
        return ([i for i in xrange(1,int(n/2)+1,2) if n % i == 0])
    else:
        return ([i for i in xrange(1,int(n/2)+1) if n % i == 0])

def get_abundants(limit):
    return [x for x in xrange(1,limit) if sum(factors(x))>x]

def get_nums(limit, abunds):
    nums = range(limit)
    for x in abunds:
        for y in abunds:
            if x+y>limit-1:
                break
            nums[x+y]=0
    return nums

limit=28123
print sum(get_nums(limit,get_abundants(limit)))
