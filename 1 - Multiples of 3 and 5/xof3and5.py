def sum_of_multiples(multiple1, multiple2, ceiling):
    """sum = 0    
    for i in xrange(0,1000):
        if i%multiple1 == 0 or i%multiple2 == 0:
            sum+=i"""
    # returning after a few weeks can change so much
    return sum([i for i in xrange(ceiling) if i%multiple1 == 0 or i%multiple2 == 0])

if __name__ == "__main__":
    print sum_of_multiples(3,5,1000)
