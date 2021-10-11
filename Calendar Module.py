import calendar as c


month,day,year = map (int,input().split())
y= c.day_name[c.weekday(year, month, day)]
print(y.upper())