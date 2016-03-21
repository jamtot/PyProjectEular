def get_names(filename):
    with open(filename) as nfile:
        names =sorted([x[1:-1] for x in nfile.read().split(",")])
    return names

def name_score(name,position,offset):
    return sum([(ord(letter)-offset)*position for letter in name])

if __name__=="__main__":
    names = get_names("p022_names.txt")
    total=0
    offset=ord("A")-1
    print sum([name_score(names[i],i+1,offset
            ) for i in xrange(len(names))])
