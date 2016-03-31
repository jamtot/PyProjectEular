def checkpan(nstr):
    return sorted(nstr) == sorted("123456789")

def gen_nums(limit):
    numbers = []
    for i in xrange(limit):
        concat = ''
        x = 1
        while len(concat) < 9:
            concat+=str(i*x)
            x+=1
        if checkpan(concat):
            numbers.append(int(concat))
    return sorted(numbers)

if __name__ == "__main__":
    assert checkpan("564738291") == True
    assert checkpan("123467689") == False
    
    print gen_nums(12345) # 932718654
