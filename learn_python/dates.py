import datetime
now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.strftime("%A"))

someday = datetime.datetime(2020, 6, 12)
print(someday)
