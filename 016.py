# learn to use `datetime` module
import datetime

# date object, time object, datetime object
myBirthday=datetime.date(1997,8,28)
myToday=datetime.date.today()
myDatetime=datetime.datetime(2017,2,3,12,42,29)

# print objects
print('My birthday: ',myBirthday.strftime('%d/%m/%Y'))
print('Current time: ', myDatetime.strftime('%d/%m/%Y %H:%M:%S'))

# date arithmetic
myTomorrow=myToday+datetime.timedelta(days=1)
print("Tomorrow:",myTomorrow.strftime('%d/%m/%Y'))

# date replace
myTomorrow=myToday.replace(day=myToday.day+1)
print("Tomorrow:",myTomorrow.strftime('%d/%m/%Y'))
