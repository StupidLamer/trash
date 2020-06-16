while True:
	try: 
		num = int(input('Enter your num: '))
		print(100/num)
	except ZeroDivisionError:
		print('The number must not be zero.')
	except ValueError:
		print('Must be a number.')
	else:
		break
