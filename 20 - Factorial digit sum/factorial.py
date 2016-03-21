def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

def sum_digits(n):
    digits=[int(x) for x in str(n)]
    return sum(digits)

print fac(10)
print fac(100)

print sum_digits(fac(10))
print sum_digits(fac(100))#648
