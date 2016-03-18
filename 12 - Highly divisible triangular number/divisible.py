import math

def get_divisors(divisor_needed):
    divisors = 0
    count = 2
    num = 1
    while divisors<divisor_needed:
        divisors = 0
        for i in xrange(1,int(math.ceil(math.sqrt(num)))+1):
            if num%i == 0:
                divisors+=2
            if i*i==num:
                # in case of perfect square
                divisors-=1
        if divisors<divisor_needed:
            num+=count
            count+=1
    return num, divisors

print get_divisors(500)
# (76576500, 576)
