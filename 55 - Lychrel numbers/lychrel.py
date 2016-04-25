def ispal(n):
    n=str(n)
    half=len(n)//2
    return n[:half]==n[::-1][:half]

def reverse(n):
    return int(str(n)[::-1])

def islychrel(n):
    for i in xrange(50):
        n+=reverse(n)
        if ispal(n): 
            return 0
    return 1
        
if __name__ == "__main__":
    total_lychrels=0
    for i in xrange(10000):
        total_lychrels+=islychrel(i)
    print "There are %d Lychrel numbers under ten thousand."%total_lychrels # 249  
