from datetime import date, datetime, timedelta
import locale

# today = date.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.weekday())

#locale.setlocale(locale.LC_ALL, 'ru')

# now = datetime.now()
# print(now)

# print(now.strftime('%a'))
# print(now.strftime('%A'))

# print(f'Date: {now.strftime("%A %d %b %Y")}')
# print(f'Time: {now.strftime("%c")}')
# print(f'Time: {now.strftime("%x")}')

now = datetime.now()
print(now + timedelta(days=1, hours=2, minutes=10))
