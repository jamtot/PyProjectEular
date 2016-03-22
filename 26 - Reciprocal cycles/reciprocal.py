# need to get prime factors
# as any denominator with prime factors
# of only 2 and/or 5 will terminate
def prime_factors(n):
    i=2
    factors=[]
    while i*i<=n:
        if n%i:
            i+=1
        else:
            n/=i
            factors.append(i)
    if n>1:
        factors.append(n)
    return factors

def prime_dict(pfrom,pto):
    prime_fac_dict={}
    for i in xrange(pfrom,pto):
        prime_fac_dict[i] = prime_factors(i)
    return prime_fac_dict

def remove_finite(prime_dict, pfrom, pto):
    for i in xrange(pfrom,pto):
        if all((x==5 or x == 2) for x in prime_dict[i]):
            #print i
            del prime_dict[i]
    return prime_dict

prime_d = prime_dict(1,1000)
print len(prime_d)
infinidict = remove_finite(prime_d, 1, 1000)
print len(infinidict)

"""If a fraction is composed of repeating decimal digits, the number of digits that repeat will never be greater than one subtracted from the fraction's denominator: Either k = d - 1, or k < d - 1 (where k is the periodic length of the repeating decimal digits)."""

def flt(n):
    pass
