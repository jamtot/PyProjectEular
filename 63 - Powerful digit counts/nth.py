def findpowers():
    i,found1,nths=1,True,0
    while found1: 
        j,found1=1,False
        while True:
            nlen = len(str(j**i))
            if nlen == i:     
                nths+=1
                found1 = True
            elif nlen > i:
                break
            j+=1
        i+=1
    return nths

if __name__ == "__main__":
    print findpowers() # 49
