"""
3 7 17 41 99 239 577 1393   n = 2n(i-1(previous)) + n(i-2(num before previous))
- - -- -- -- --- --- ----
2 5 12 29 70 169 408 985    (same as above, next number is 2 times previous plus
                            the number before that)
"""

def nextexp(expansions):
    expansions.append(expansions[-1]*2+expansions[-2])

def thousandexps(expans):
    while len(expans) < 1000:
        nextexp(expans)

if __name__ == "__main__":
    numerator_expansions = [3, 7, 17, 41, 99, 239, 577, 1393]
    denominator_expansions = [2, 5, 12, 29, 70, 169, 408, 985]

    thousandexps(numerator_expansions)
    thousandexps(denominator_expansions)

    numerators_with_more_digits = 0
    for i in xrange(len(numerator_expansions)):
        if (len(str(numerator_expansions[i])) > len(str(denominator_expansions[i]))):
            numerators_with_more_digits+=1
    
    print numerators_with_more_digits
