def sumofpowers(power):
    
    # find the upper limit
    n = 1
    # once the length of the number is less than the amount
    # of digits used to make it, you've got your number to go up to
    while len(str((9**power)*n)) > n:
        n+=1

    nums = []
    for x in xrange( 2, ((9**power)*n) ):
        total = 0
        for i in str(x):
            total+= int(i)**power

        if total == x:
            nums.append(x)

    totes = 0
    for x in nums:
        #print x
        totes+=1

    return sum(nums)
                 
assert (sumofpowers(4) == 19316)
print sumofpowers(5)
