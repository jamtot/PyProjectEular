months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
days = {1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",
            6:"saturday",7:"sunday"}

day=1
month=1
year=1900

end_day=31
end_month=12
end_year=2000

leap = False
counter=0

for y in xrange(year,end_year+1):

    if year%400==0 or (year%4 and year%100!=0):
        leap=True
    else:
        leap=False
    
    for m in xrange(1,end_month+1):
        if leap and m == 2:
            days_in_month = months[m]+1
        else:
            days_in_month = months[m]
        for d in xrange(1,days_in_month+1):
            if day%7==0 and d==1 and y>1900:
                counter+=1
            day+=1
                
print counter#171
print day#36866   
