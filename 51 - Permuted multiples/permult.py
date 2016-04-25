def findpermutedmultiples(multiples):
    found=False 
    multrange=range(2,multiples+1)
    x = 1   
    while not found:
        for i in multrange:
            if sorted(str(x)) != sorted(str(x*i)):
                break
        else:
            found=True
            return x
        x+=1

if __name__ == "__main__":
    print findpermutedmultiples(6) # 142857
        
