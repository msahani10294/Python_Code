class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last +"@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay* self.raise_amt)

    def __repr__(self):
        return "Employees ({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{}-{}".format(self.fullname(), self.email)


emp1 = Employee("Manoj", "Sahani", 20000)
emp2 = Employee("Rohit ", "Kumar", 50000)

print(emp1)  # o/p <__main__.Employee object at 0x0000029EBA9C7400>befor using any dunder method.
