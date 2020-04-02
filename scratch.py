import datetime

now = str(datetime.datetime.now())
date_now, time_now = now.split(' ')
print(date_now)
print(time_now)

year, month, date = date_now.split("-")
hour, minuits, second = time_now.split(':')
print(hour)
