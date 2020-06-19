class Person(object):
	"""Class of human"""

	def __init__(self, name, age):
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

class Employee(Person):
	"""docstring for Employee"""
	
	def __init__(self, name, age, company):
		super().__init__(name, age)
		self.company = company
	
	def more_info(self):
		print(f'{self.name} works in {self.company}')

	def __str__(self):
		return Person.__name__
		
		