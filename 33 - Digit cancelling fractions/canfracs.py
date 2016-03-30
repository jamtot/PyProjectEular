def cancelling_fractions():
    fracs = []
    for x in xrange(10,100):
        for y in xrange(x+1,100):
            if x%10!=0 and y%10!=0:
                xstr = str(x)
                ystr = str(y)
                for num in xstr:
                    if num in ystr:
                        xrem=0
                        yrem=0
                        if xstr.replace(num, "") != "":
                            xrem = int(xstr.replace(num, ""))
                        if ystr.replace(num, "") != "":
                            yrem = int(ystr.replace(num, ""))
                        
                        
                        if xrem!=0 and yrem!=0 and ((float(xrem)/float(yrem)) == (float(x)/float(y))):
                            fracs.append([x,y])
    return fracs

def product(fractions):
    num = 1 
    for frac in fractions:
        num*= (float(frac[0])/float(frac[1]))
        denom = 1/num
    return denom

fracs = cancelling_fractions()
print product(fracs) # 1/100
