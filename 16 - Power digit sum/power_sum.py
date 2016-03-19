def sum_of_power(number, power):
    # return sum(map(int,list(str(number**power))))
    # or
    # return sum(map(int,str(number**power)))
    # or
    return sum([int(i) for i in str(number**power)])





print sum_of_power(2,15) # 26
print sum_of_power(2,1000) # 1366
