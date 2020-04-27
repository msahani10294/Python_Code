# class method changes all instances of the class
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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp1 = Employee("Manoj ", "Sahani", 20000)
emp2 = Employee("Rohit ", "Kumar", 50000)

emp_str1 = 'Abhishek-Yadav-3000'
emp_str2 = 'Vikrant-Kumar-45000'
emp_str3 = 'Nil-singh-30500'

# for individual emp
# first, last, pay = emp_str1.split('-')
# new_emp1 = Employee(first, last, pay)

new_emp1 = Employee.from_string(emp_str1)
new_emp2 = Employee.from_string(emp_str2)
print(new_emp1.fullname())
print(new_emp1.email)
print(new_emp2.fullname())

# print(emp1.raise_amt)
# print(emp2.raise_amt)
