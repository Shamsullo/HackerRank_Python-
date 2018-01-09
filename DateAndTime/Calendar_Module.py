import calendar
import datetime

input_date = input()

month,day,year=map(int,input_date.split())

day_of_the_week = datetime.date(year,month,day)

print(calendar.day_name[day_of_the_week.weekday()].upper())
