#see in which week your where born

birthday = 'your_birth_date'

import datetime
import calendar as c

d = datetime.date(2001, 10, 10) #write your birthdate (year, month, day)
print(c.day_name[d.weekday()])