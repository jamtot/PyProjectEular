def get_num_word(num):
    # num / n = how many ns
    # num % n = next num to check

    # a better way would be using dictionary values (1, "one"), (2, "two")
    if num/1000:
        return "%s thousand %s" % ( get_num_word(num/1000), get_num_word(num%1000))
    elif num/100>0 and num%100 == 0:
        return "%s hundred %s" % (get_num_word(num/100), get_num_word(num%100))
    elif num/100>0:
        return "%s hundred and %s" % (get_num_word(num/100), get_num_word(num%100))
    elif num/90>0:
        return "ninety %s" % (get_num_word(num%90))
    elif num/80>0:
        return "eighty %s" % (get_num_word(num%80))
    elif num/70>0:
        return "seventy %s" % (get_num_word(num%70))
    elif num/60>0:
        return "sixty %s" % (get_num_word(num%60))
    elif num/50>0:
        return "fifty %s" % (get_num_word(num%50))
    elif num/40>0:
        return "forty %s" % (get_num_word(num%40))
    elif num/30>0:
        return "thirty %s" % (get_num_word(num%30))
    elif num/20>0:
        return "twenty %s" % (get_num_word(num%20))
    elif num/19>0:
        return "nineteen %s" % (get_num_word(num%19))
    elif num/18>0:
        return "eighteen %s" % (get_num_word(num%18))
    elif num/17>0:
        return "seventeen %s" % (get_num_word(num%17))
    elif num/16>0:
        return "sixteen %s" % (get_num_word(num%16))
    elif num/15>0:
        return "fifteen %s" % (get_num_word(num%15))
    elif num/14>0:
        return "fourteen %s" % (get_num_word(num%14))
    elif num/13>0:
        return "thirteen %s" % (get_num_word(num%13))
    elif num/12>0:
        return "twelve %s" % (get_num_word(num%12))
    elif num/11>0:
        return "eleven %s" % (get_num_word(num%11))
    elif num/10>0:
        return "ten %s" % (get_num_word(num%10))
    elif num/9>0:
        return "nine %s" % (get_num_word(num%9))
    elif num/8>0:
        return "eight %s" % (get_num_word(num%8))
    elif num/7>0:
        return "seven %s" % (get_num_word(num%7))
    elif num/6>0:
        return "six %s" % (get_num_word(num%6))
    elif num/5>0:
        return "five %s" % (get_num_word(num%5))
    elif num/4>0:
        return "four %s" % (get_num_word(num%4))
    elif num/3>0:
        return "three %s" % (get_num_word(num%3))
    elif num/2>0:
        return "two %s" % (get_num_word(num%2))
    elif num/1>0:
        return "one %s" % (get_num_word(num%1))
    elif num==0:
        return ""


from collections import OrderedDict
num_dict = OrderedDict([(1000,"thousand"),(100,"hundred"),(90,"ninety"),(80,"eighty"),
            (70,"seventy"),(60,"sixty"),(50,"fifty"),(40,"forty"),(30,"thirty"),
            (20,"twenty"),(19,"nineteen"),(18,"eighteen"),(17,"seventeen"),
            (16,"sixteen"),(15,"fifteen"),(14,"fourteen"),(13,"thirteen"),
            (12,"twelve"),(11,"eleven"),(10,"ten"),(9,"nine"),(8,"eight"),
            (7,"seven"),(6,"six"),(5,"five"),(4,"four"),(3,"three"),(2,"two"),(1,"one")])

def get_num_word_dict(num):

    for val in num_dict:
        if num==0: return ""
        elif num/val>0:
            if num>99:
                if num < 1000 and num%100!=0:
                   return "%s %s and %s"%( get_num_word_dict(num/val), 
                                        num_dict[val], 
                                        get_num_word_dict(num%val))
                else:
                    return "%s %s %s"%( get_num_word_dict(num/val), 
                                        num_dict[val], 
                                        get_num_word_dict(num%val))
            else: 
                return "%s %s" %  ( num_dict[val], 
                                    get_num_word_dict(num%val))

# not working as of yet
"""import operator
num_udict = {1000:"thousand",100:"hundred",90:"ninety",80:"eighty",
            70:"seventy",60:"sixty",50:"fifty",40:"forty",30:"thirty",
            20:"twenty",19:"nineteen",18:"eighteen",17:"seventeen",
            16:"sixteen",15:"fifteen",14:"fourteen",13:"thirteen",
            12:"twelve",11:"eleven",10:"ten",9:"nine",8:"eight",
            7:"seven",6:"six",5:"five",4:"four",3:"three",2:"two",1:"one"}

s_num_udict = sorted(num_dict, key=operator.itemgetter(1), reverse=True)

def get_num_word_udict(num):

    for val in s_num_udict:
        if num==0: return ""
        elif num/val>0:
            if num>99:
                if num < 1000 and num%100!=0:
                   return "%s %s and %s"%( get_num_word_udict(num/val), 
                                        num_dict[val], 
                                        get_num_word_udict(num%val))
                else:
                    return "%s %s %s"%( get_num_word_udict(num/val), 
                                        num_dict[val], 
                                        get_num_word_udict(num%val))
            else: 
                return "%s %s" %  ( num_dict[val], 
                                    get_num_word_udict(num%val))"""


def remove_fluff(numstr):
    return ("").join(numstr.split(" "))

def get_len(string):
    return len(string)

def sumgetter(nfrom, nto):

    sum = 0
    for i in xrange(nfrom, nto+1): # inclusive of nto
        sum+=get_len(remove_fluff(get_num_word(i)))
    print sum

def sumgetterdict(nfrom, nto):

    sum = 0
    for i in xrange(nfrom, nto+1): # inclusive of nto
        sum+=get_len(remove_fluff(get_num_word_dict(i)))
    print sum


if __name__ == "__main__":
    sumgetter(1, 5) # 19
    sumgetter(1,1000) # 21124

    # slower using an ordered dictionary
    sumgetterdict(1,5)
    sumgetterdict(1,1000)

    #print get_num_word_dict(1324)
    
