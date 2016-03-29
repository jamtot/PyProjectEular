coins = [1,2,5,10,20,50,100,200]



def coincombos(target):
    ways=0
    # we ignore 1ps as that will always be used to fill the 
    # gaps the others can't
    for a in xrange(0,target+1,200):
        for b in xrange(a,target+1,100):
            for c in xrange(b,target+1,50):
                for d in xrange(c,target+1,20):
                    for e in xrange(d,target+1,10):
                        for f in xrange(e,target+1,5):
                            for g in xrange(f,target+1,2):
                                ways+=1
    return ways
    


print coincombos(200) # 73682 ways
