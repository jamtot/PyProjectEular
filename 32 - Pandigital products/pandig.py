def paniprods():
    prods = []
    for x in xrange(1,9999):
        # adding the /x drastically reduces runtime, yet yields the
        # correct answer still
        for y in xrange(1,9999/x):
            num = x*y
            numstr = "".join(sorted(str(num)+str(x)+str(y)))
            #print numstr
            if numstr == "123456789":
                if num not in prods:
                    prods.append(num)
    return sum(prods)

print paniprods() # 45228

