def checkdiv(num, divs):
    numstr = (str(num)).zfill(10)
    for i in xrange(7):
        if int(numstr[i+1]+numstr[i+2]+numstr[i+3]) % divs[i] != 0:
            break
    else:
        return True
    return False
    
def listtostr(nums):
    num = "".join(map(str, nums))
    return num

# taken from solution to problem 24, 
# lexicographic permutations
# modified to use a string and return a string 
# int will lose the preceeding 0 at the start
def get_next(numstr):

    nums = [int(x) for x in numstr]

    # find longest subsection that won't increase (highest permutation)
    i = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i-=1
    # now i is the start of the subsection

    #are we at the front
    if i<=0:
        print "Last permutation reached."
        return "END"

    # let nums[i-1] be the next to move
    # find the rightmost element that is bigger than num[i-1]
    j =  len(nums)-1
    while nums[j] <= nums[i-1]:
        j-=1
    # now the value of nums[j] becomes the new number to move
    # assertion: j >= i

    # swap the number with j
    temp = nums[i-1]
    nums[i-1] = nums[j]
    nums[j] = temp

    # reverse the subsection to have from lowest to highest
    j = len(nums)-1
    while i<j:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i+=1
        j-=1

    return listtostr(nums)

def nextpan(n = 123456788):
    pan = "0123456789"
    while n <= 9876543210:        
        n+=1
        nstr = ("".join(sorted(list(str(n))))).zfill(10)
        if pan == nstr:
            yield n

if __name__ == "__main__":
    divs = [2,3,5,7,11,13,17]
    assert checkdiv("1406357289", divs) == True
    assert get_next("0123456789") == "0123456798"
    textpgen = nextpan()
    assert textpgen.next() == 123456789

    solpans = []

    # takes a long time to iterate to the pandigitals
    # a very long time.
    """pangen = nextpan()
    pan = pangen.next()
    while pan < 9876543210:

        pan = pangen.next()
        print pan
        if checkdiv(pan, divs):
            solpans.append(pan)
    print sum(solpans)"""

    num ="0123456789"
    while num != "END":
        if checkdiv(num, divs):
            solpans.append(num)
        num = get_next(num)
    print sum(map(int,solpans)) # 16695334890
    
