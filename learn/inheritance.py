from classes import Person, Employee

person = Person('Katy', 43)
person.age = 35
person.print_info()

employee = Employee('Nick', 30, 'Yandex')
employee.print_info()
employee.more_info()
print(employee)
