"""
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""

def sumnumspiral(sidesize):
    num = 1
    # you step starts at 2, every second number is counted
    step = 2
    # start with the middle 1 counted
    total=1
    # once your step is greater than your sidesize, you are 
    # past where you need to be
    while step < sidesize:
        # each step in the spiral applies to 4 sides
        for x in xrange(4):
            # add the step yto your num
            num+=step
            # and the num to your total
            total+=num
        # for each ring of the sprial,
        # your step will grow 2
        step+=2
    return total

assert sumnumspiral(5) == 101
print sumnumspiral(1001)

