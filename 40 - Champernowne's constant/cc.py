def champernownes(numstomult):
    # make sure the largest is to the back
    numstomult = sorted(numstomult)
    numstr = ''
    i = 1
    while len(numstr) < numstomult[-1]:
        numstr+=str(i)
        i+=1
    #print [numstr[x-1] for x in numstomult]
    # kinda proud of this
    num = reduce(lambda x,y: x*y, map(int, [numstr[x-1] for x in numstomult] ))
    return num
    


if __name__ == "__main__":
    assert champernownes([1,2,3,4,5]) == 120
    print champernownes([1,10,100,1000,10000,100000,1000000]) # 210
