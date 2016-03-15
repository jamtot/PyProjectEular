def find_smallest(limit, highest):
    for i in xrange(20,limit,highest):
        for j in xrange(highest,0,-1):
            if i%j != 0:
                break
        if i%j != 0: pass        
        else: return i

def smallest(step = 20):
    # taking out numbers that are divisors of other
    # numbers in the list
    # I don't like how hard-coded this is
    check_list = [20, 19, 18, 17, 16, 14, 13, 11]

    i = step
    #for i in xrange(step,limit,step):
    while True:
        if all(i % n == 0 for n in check_list):
            return i
        i += step

# brute force, takes a few seconds
#print find_smallest(500000000, 20)
print smallest()
