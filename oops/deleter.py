class Employee:

    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + '.' + self.last + "@gmail.com"

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Successfully ! ")
        self.first = None
        self.last = None


emp1 = Employee('manoj', 'kumar')
emp1.fullname = 'M Sahani'
print(emp1.fullname)
del emp1.fullname