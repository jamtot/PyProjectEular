def sum_of_multiple(multiple, ceiling):
    sum = 0    
    for i in xrange(0,1000,multiple):
        sum+=i
    return sum

def sum_of_multiples(multiple1, multiple2, ceiling):
    sum = 0    
    for i in xrange(0,1000):
        if i%multiple1 == 0 and i%multiple2 == 0:
            sum+=i
        elif i%multiple1 == 0: sum+=i
        elif i%multiple2 == 0: sum+=i
    return sum

# includes same numbers
sum = 0
sum+= sum_of_multiple(3,1001)
sum+= sum_of_multiple(5,1001)
print sum

sum2 = sum_of_multiples(3,5,1000)
print sum2
