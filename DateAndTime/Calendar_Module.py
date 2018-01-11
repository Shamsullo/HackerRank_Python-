import calendar, datetime

input_date = input()

month,day,year = map(int,input_date.split())

day_of_the_week = datetime.date(year,month,day)

print calendar.day_name[day_of_the_week.weekday()].upper()

#the code isn't giving an expected result, i wonder why?

