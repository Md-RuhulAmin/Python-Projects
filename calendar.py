import calendar


 
#Creating a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
# st = c.formatmonth(2020, 12, 0, 0)
# print(st)

#To figure out the fist friday of every month
print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2021, m)
    weekOne = cal[0]
    weekTwo = cal[1]

    if weekOne[calendar.FRIDAY] != 0:
        meetday = weekOne[calendar.FRIDAY]
    else:
        meetday = weekTwo[calendar.FRIDAY]
    
    print("%10s %2d" % (calendar.month_name[m], meetday))