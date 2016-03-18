def collatz_number(nummy, printy = False):#
    num = nummy
    if printy: print num,
    terms = 1
    while num != 1:
        if num%2==0:
            num=num/2  
        else:
            num=(3*num)+1
        terms+=1
        if printy: print num,
    return terms,nummy


def collatz_check(ceiling):
    largest_term = 0
    n = 1
    for i in xrange(1,ceiling):
        terms,num = collatz_number(i)
        if terms>largest_term: 
            largest_term = terms
            n = num

    print n, largest_term
        
        

print "| There are %d terms in %d. |"% collatz_number(12, True)
collatz_check(1000000)
