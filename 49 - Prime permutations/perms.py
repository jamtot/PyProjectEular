from collections import defaultdict

def primelist(lowest = 999, highest = 10000):
    primes = [2,3]
    n=3
    primes_limit = []
    while n<highest:
        prime = True
        n+=2
        for p in primes:
            if n%p==0:
                prime = False
                break
        if prime:
            primes.append(n)
            if n > lowest:
                primes_limit.append(n)
    return primes_limit

def findperms(numbers):
    matches = defaultdict(list)
    for i in xrange(len(numbers)):
        for j in xrange(len(numbers)):
            if i != j:
                num1, num2 = ''.join(sorted(str(numbers[i]))), ''.join(sorted(str(numbers[j])))
                if num1 == num2:
                    if numbers[i] not in matches[num1]:
                        matches[num1].append(numbers[i])
                    if numbers[j] not in matches[num1]:
                        matches[num1].append(numbers[j])
    return matches

def checkmatches(matches):
    found_values = []
    for m in matches:
        if len(matches[m]) > 2:
            values = [val for val in sorted(matches[m])]
            for i in xrange(len(values)):
                for j in xrange(len(values)):
                    for k in xrange(len(values)):
                        if i != j and j != k and i != k:
                            if abs(values[i] - values[j]) == abs(values[k] - values[j]):
                                found = sorted([values[i], values[j], values[k]])
                                if found not in found_values:
                                    found_values.append(found)
    return found_values

def concat(vals):
    for i in xrange(len(vals)):
        vals[i] = ''.join(map(str,vals[i]))
    return ', '.join(map(str,vals))

if __name__ == "__main__":
    primes = primelist()
    matches = findperms(primes)
    print concat(checkmatches(matches)) # 296962999629, 148748178147

