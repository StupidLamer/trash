class Person(object):
	"""Class of human"""

	name = 'John'

	def __init__(self, name):
		self.name = name
		self.__age = 20

	def print_info(self):
		print(f'Name is {self.name}, age is {self.__age}')

	# def get_age(self):
	# 	return self.__age

	@property
	def age(self):
		return self.__age


	@age.setter
	def age(self, value):
		if 1 <= value <= 100:
			self.__age = value
		else:
			print('Wrong age')

