import datetime
import random

x = random.randint(1, 100)
user_num = 0
cnt = 0

while True:
	user_num = int(input('Look for the my num: '))
	cnt += 1
	if user_num == x:
		print(f"You did it for {cnt} try")
		print('The end')
		break
	elif user_num > x:
		print('My num less')
	else: 
		print('My num bigger')