def check_palindromic(number):
    number = list(str(number))
    for i in xrange(len(number)):
        if number[i] != number[-i-1]:
            return False
    return True
            
palindromics = []
for x in xrange(999, 0, -1):
    for y in xrange(999, 0, -1):
        number = x*y
        if check_palindromic(number):
            palindromics+=[number]
            break

print sorted(palindromics) # largest is 906609
