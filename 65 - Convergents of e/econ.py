def contfrac(e):
    n=0
    for digit in e[:0:-1]: # work from end back
        n = 1.0 / (digit + n)
    return (e[0]+n).as_integer_ratio() # returns as nom

def getnumsum():
    e = [2,1,2,1,1,4,1,1,6]
    i=4
    while len(e)<100:
        e+=[1,1,2*i]
        i+=1
    e=e[:100]
    frac = contfrac(e)
    print sum(map(int,list(str(frac[0])))) # 53, incorrect
#---------------not precise enough with floats and irrational numbers

def gen100e():
    e = [2,1,2]
    i=2
    while len(e)<100:
        e+=[1,1,2*i]
        i+=1
    e=e[:100]
    return e

""" using a pattern based approach similar to Problem 57
    e = [2,1,2,1,1,4,1,1,6,...1,1,2k...] - k incrementing every use
    n = [3,2,8,11,19,87,106,193,1264,1457]
    
    for each number in the sequence, it consists of 
"""#    ni = (ei * ni-1) + ni-2

def generatenumto(e):
    numerators = [3,2,8,11]
    i=(numerators.index(numerators[-1]))+1
    while i < len(e):
        numerators.append((e[i]*numerators[i-1])+numerators[i-2])
        i+=1
    return numerators

if __name__ == "__main__":
    e = gen100e()
    noms = generatenumto(e)
    print sum(map(int,list(str(noms[-1])))) # 272
