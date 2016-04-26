def digsum(n):
    return sum([int(x) for x in str(n)])

if __name__ == "__main__":
    largest = 0
    lnum = 0
    for a in xrange(1,100):
        for b in xrange(1,100):
            num = a**b
            dsum = digsum(num)
            if dsum > largest: 
                largest = dsum
                lnum = num
    print largest, lnum # 972
            
    
