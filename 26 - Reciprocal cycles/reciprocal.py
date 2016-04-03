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


# found a comment online that states...
""" if you want to know how many repeating digits there are in 1/243, compute 999/243, 9999/243, 99999/243 until you get an integer result. In practice, this takes much longer (and for many cases, like 1/243, your calculator will run out of digits before you reach the answer)"""

# works for some, hitches on numbers like 6 and 12 with 1 number recurring infinitely
def method9(demoninator):
    num = 0
    nines = '9'
    while int(nines)%demoninator!=0.0:
        #num=int(nines)/demoninator
        nines=nines+"9"
    num = int(nines)/demoninator
    return num

# removes trailing 0s because ints
#print method9(43)
#print (len(str(method9(43))))

"""largest=-1
l_numa=-1
for num in infinidict:
    print "NUM:",num
    len9 = len(str(method9(num)))
    if  len9 > largest:
        num = method9(num)
        largest = len9
print "largest",largest
print "numba",l_numa"""

def cycle_length(d):
    # this lists the remainders, as it goes, and once it hits the
    # same remainder, its about to start recurring over again
    cycle_list = []
    remainder_list = []
    list_len = 0
    remainder = 1
    # just used to get the cyclic numbers (not needed for problem)
    c=0
    r2=1
    c=r2 / d
    r2=r2%d
    r2*=10
    while remainder:
        #print "REMAINDER",remainder
        c=r2 / d
        remainder = remainder % d
        r2%= d
        if remainder in remainder_list:
            #print cycle_list
            #print remainder_list
            return list_len - remainder_list.index(remainder)
        cycle_list.append(c)
        remainder_list.append(remainder)
        remainder *= 10
        r2*=10
        list_len+=1

    return 0

largest = -1
numba = -1
for num in infinidict:

    if cycle_length(num) > largest:
        largest=cycle_length(num)
        numba = num
print "Number %d is the largest with %d recurring digits."%(numba,largest)
    

        
    
