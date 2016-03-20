input1="""3
7 4
2 4 6
8 5 9 3"""

input2= """          75
                    95 64
                  17 47 82
                 18 35 87 10
               20 04 82 47 65
              19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
         41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
     70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def get_noomers(inpoot):
    nooms = []
    for line in inpoot.splitlines():
        nooms += [[int(x) for x in line.split()]]
    return nooms
        
def bottoms_up(nooms):
    # do lines from bottom, starting second from bottom
    for i in xrange(len(nooms)-2,-1,-1):
        # go through each element, and add the greater underneath
        for j in xrange(len(nooms[i])):
            nooms[i][j]+=max(nooms[i+1][j],nooms[i+1][j+1])
    # return the top value, which has the greatest path value
    return nooms[0][0]

def bot_up(input):
    nooms = []
    # split input into a list of lists
    for line in input.splitlines():
        nooms += [[int(x) for x in line.split()]]
    # do lines from bottom, starting second from bottom
    for i in xrange(len(nooms)-2,-1,-1):
        # go through each element, and add the greater underneath
        for j in xrange(len(nooms[i])):
            nooms[i][j]+=max(nooms[i+1][j],nooms[i+1][j+1])
    # return the top value, which has the greatest path value
    print nooms[0][0]

nums=get_noomers(input1)
print bottoms_up(nums)

nums2=get_noomers(input2)#23
print bottoms_up(nums2)#1074

bot_up(input2)

