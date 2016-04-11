def selfpower(n):
    return n**n

if __name__=="__main__":
    number = str(sum([selfpower(i) for i in xrange(1,1001)]))
    print "The last ten digits are %s"%number[-10:] #9110846700
    with open("answer.txt", 'w') as nfile:
        nfile.write(number)
