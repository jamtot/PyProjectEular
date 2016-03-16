# from 10001st prime
def generate_primes_to_n(n):
    # starting with 2 as it's the only even prime
    primes = [2]
    # starting with 3
    current = 3
    while primes[-1] < n:
        # make a list of bools for whether nunmbers are prime or not
        # by dividing them by previous primes
        prime_test = [current for i in primes if current%i == 0]
        # for every False (non divisible by previous primes) add to primes
        primes+= [] if prime_test else [current]
        # incrementing in 2s, as only odds should be tested
        current+= 2
    # goes 1 past end, this is hacky
    primes.pop()
    return primes

primes = generate_primes_to_n(10)
print primes
sump = sum(primes)
print sump

#milprim = generate_primes_to_n(2000000)
#milsum = sum(milprim)
#print milsum

# got 142913828922
# took a few hours

# a bit faster (done in a lot less time
def get_prims_to_n(n):
    marked = [0] * n
    current = 3
    sum = 2
    while current < n:
        if marked[current] == 0:
            sum += current
            i = current
            while i < n:
                marked[i] = 1
                i += current
        current += 2
    print sum

get_prims_to_n(2000000)
