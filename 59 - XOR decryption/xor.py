import string

def splitinput(filename):
    with open(filename) as ciphertext:
        return [int(x) for x in ciphertext.read().split(",")]

def findtext(cipher):
    letterlist = list(string.ascii_lowercase)
    lenllist = len(letterlist)
    output = ''
    # top 5 common English words
    common = ["the", "be", "to", "of", "and"]
    for i in xrange(lenllist):
        for j in xrange(lenllist):
            for k in xrange(lenllist):
                #print letterlist[i],letterlist[j],letterlist[k]
                for x in xrange(len(cipher)):
                    if x%3==0:
                        output+=chr(cipher[x] ^ ord(letterlist[i]))
                    elif x%3==1:
                        output+=chr(cipher[x] ^ ord(letterlist[j]))
                    elif x%3==2:
                        output+=chr(cipher[x] ^ ord(letterlist[k]))
                #print output
                if all(c in output for c in common):
                    #print letterlist[i],letterlist[j],letterlist[k]
                    #print output
                    return output
                output=''
    return "Unsuccessful decryption."

def textsum(text):
    tsum=0
    for i in xrange(len(text)):
        tsum+=ord(text[i])
    return tsum

if __name__ == "__main__":
    cipher = splitinput("p059_cipher.txt")
    text = findtext(cipher)
    print textsum(text)
    
                
