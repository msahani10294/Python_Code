
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


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang ):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


emp1 = Employee("Manoj ", "Sahani", 20000)
emp2 = Employee("Rohit ", "Kumar", 50000)

