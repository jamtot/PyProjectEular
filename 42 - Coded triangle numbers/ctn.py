# -*- coding: utf-8 -*-
#tn = ½n(n+1)
def trinum(n):
    return n*(n+1)/2

def getwords(filename):
    with open(filename) as wordfile:
        contents = wordfile.read()
        wwqs = contents.split(",") # gets words with quotes
        words = [w[1:-1] for w in wwqs]
        return words

def lettervalue(l):
    return ord(l.upper())-(ord("A")-1)

def wordvalue(w):
    return sum([lettervalue(l) for l in word])

def trinext(n=1):
    while True:
        yield trinum(n)
        n+=1

def checkword(word, tricache, trigen):
    wval = wordvalue(word)
    while wval > tricache[-1]:
        tricache.append(next(trigen))
    if wval in tricache:
        return True
    else: return False
        

if __name__ == "__main__":
    assert [trinum(n) for n in xrange(1,11)] == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    words = getwords("p042_words.txt")
    trigen = trinext()
    triwords, tricache = [], []
    tricache.append(next(trigen))
    for word in words:
        if checkword(word, tricache, trigen):
            triwords.append(word)
    print triwords
    print len(triwords)#162
    
    
