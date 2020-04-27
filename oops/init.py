
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + "@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay* self.raise_amt)


emp1 = Employee("Manoj ", "Sahani", 20000)
emp2 = Employee("Rohit ", "Kumar", 50000)

# print(emp1.fullname())
# print(emp2.fullname())

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# print(emp1.__dict__)
# print("-----------")
# print(Employee.__dict__)

# if you want to change raise_amt for all the instance of a class
print(emp1.raise_amt)
Employee.raise_amt = 1.05
print(emp1.raise_amt)
print(emp2.raise_amt)

