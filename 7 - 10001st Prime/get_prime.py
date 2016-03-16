def generate_n_primes(n):
    # starting with 2 as it's the only even prime
    primes = [2]
    # starting with 3
    current = 3
    while len(primes) < n:
        # make a list of bools for whether nunmbers are prime or not
        # by dividing them by previous primes
        prime_test = [current for i in primes if current%i == 0]
        # for every False (non divisible by previous primes) add to primes
        primes+= [] if prime_test else [current]
        # incrementing in 2s, as only odds should be tested
        current+= 2
    return primes

print generate_n_primes(10001)
