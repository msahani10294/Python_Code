# class method changes all instances of the class
class Employee:

    raise_amt = 10

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + "@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay* self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp1 = Employee("Manoj ", "Sahani", 20000)
emp2 = Employee("Rohit ", "Kumar", 50000)

Employee.set_raise_amt(20)
print(emp1.raise_amt)
print(emp2.raise_amt)
