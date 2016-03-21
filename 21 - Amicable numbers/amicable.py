def factors(n):
    if n%2==1:
        return ([i for i in xrange(1,int(n/2)+1,2) if n % i == 0])
    else:
        return ([i for i in xrange(1,int(n/2)+1) if n % i == 0])
     
def facsum(n):
    return sum(factors(n))

if __name__ == "__main__":
    amicables = []    
    for a in xrange(1,10000):
        b=facsum(a)
        fsB=facsum(b)
        if a!=b and fsB==a:
            if a not in amicables:
                amicables.append(a)
            if fsB not in amicables:
                amicables.append(b)
            with open("amic.txt", "a") as file: 
                file.write("Pair - %r : %r\n"%(a,b))
    print "Sum is %r" % (sum(amicables))
        
