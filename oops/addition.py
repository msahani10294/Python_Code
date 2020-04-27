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

    #     "__add__" basically sum the total pay of all the emp
    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee("Manoj ", "Sahani", 20000)
emp2 = Employee("Rohit ", "Kumar", 50000)

print(emp1+emp2)