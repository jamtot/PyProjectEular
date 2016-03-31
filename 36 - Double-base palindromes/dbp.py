def decToBin(number):
    n = 0
    binstr = ''
    while 2**n <= number:
        n+=1
    n-=1
    for x in xrange(n+1):
        if 2**n <= number:
            number-=2**n
            binstr+='1'
        else:
            binstr+='0'
        n-=1
    return binstr

def checkPalindrome(nstr):
    if all(nstr[i] == nstr[-(i+1)] for i in xrange(len(nstr))):
        return True
    return False
        
def checkNums(limit):
    double_palindromic = []
    for n in xrange(limit):
        bn = decToBin(n)
        if checkPalindrome(str(n)) == checkPalindrome(bn) == True:
            double_palindromic.append(n)

    return sum(double_palindromic)

if __name__ == "__main__":
    assert decToBin(13) == "1101"
    assert checkPalindrome("10101") == True
    assert checkPalindrome("101010") == False
    print checkNums(1000000) # 872187
