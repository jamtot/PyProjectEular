def sumsqrdif(n):
    num_list = [x for x in xrange(n+1)]
    sum_sqr = sum(map(lambda x: x**2, num_list))
    print sum_sqr

    sqr_sum = sum(num_list)**2
    print sqr_sum

    diff = abs(sum_sqr - sqr_sum)
    print diff

sumsqrdif(10)
sumsqrdif(100)
