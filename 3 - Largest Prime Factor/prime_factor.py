import math

# essentially brute force
# will take forever
def slow_factors():
    number = 600851475143 
    factors = []
    for i in xrange(2,number+1):
        if number%i == 0: factors+=[i]

    prime_factors = []
    for factor in factors:
        prime = True
        for i in xrange(2,factor):
            if factor%i==0: # not prime
                prime=False
        if prime: prime_factors+=[factor]

    print prime_factors

# tried converting pseudo-code on the
# sieve of atkin algorithm

# memory error 
def sieve_of_atkin(limit):
    limit = int(math.sqrt(limit))
    s = [1,7,11,13,17,19,23,29,  31,37,41,43,47,49,53,59]
    sieve_list = [False for i in xrange(1,limit+1)]

    for w in xrange(0,limit/60):
        for x in s:
            n = 60*w+x
            sieve_list[n-1] = False


    for x in xrange(1,limit+1):
        for y in xrange(1, limit+1, 2):
            n = 4*(x**x)+y**y          
            if n <= limit and (n%60) in [1,13,17,29,37,41,49,53]:
                sieve_list[n-1] = not sieve_list[n-1]

    for x in xrange(1,limit+1,2):
        for y in xrange(2, limit+1, 2):
            n = 3*(x**x)+y**y
            if n <= limit and (n%60) in [7,19,31,43]: 
                sieve_list[n-1] = not sieve_list[n-1]

    for x in xrange(2,limit+1):
        for y in xrange(1, limit+1, 2):
            newy = x-y
            if newy > limit+1: break
            n = 3*(x**x)-y**y
            if n <= limit and (n%60) in [11,23,47,59]:
                sieve_list[n-1] = not sieve_list[n-1]

    for w in xrange(0,limit):
        for x in s:
            if n**n <= limit and n >= 7:
                if results[n-1]:
                    c = n**n * (60 * w + x)
                    if c <= limit:
                        sieve_list[c-1] = False

    print "2, 3, 5"
    for w in xrange(0,limit):
        for x in s:
            n = 60 * w + x
            if n >= 7 and n <= limit:
                if sieve_list[n-1]: print n


# another sieve of atkin implementation
# that is another error
def sieve_implementation(limit):
    is_prime = [False] * (limit + 1)

    for x in xrange(1,int(math.sqrt(limit))+1):
        for y in xrange(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2

            if n<=limit and (n%12==1 or n%12==5):
                # print "1st if"
                is_prime[n] = not is_prime[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7:
                # print "Second if"
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11:
                # print "third if"
                is_prime[n] = not is_prime[n]

    for n in xrange(5,int(math.sqrt(limit))):
        if is_prime[n]:
            for k in xrange(n**2,limit+1,n**2):
                is_prime[k] = False
    print 2,3
    for n in xrange(5,limit):
        if is_prime[n]: print n

# seems to work (thumb)
def get_primes(limit):
    factors = []
    # check against 2 and 1 first
    while limit % 2 == 0:
        # if even, 2 is a prime factor
        factors += [2]
        limit /= 2
    if limit == 1:
        return factors
    num = 3
    while num*num <= limit:
        if limit%num == 0:
            factors+=[num]
            limit/=num
        else:
            # going up in odd numbers
            num+=2
    factors+=[limit]
    return factors      
    
print get_primes(13195)
print get_primes(600851475143)
