'''
Created on Mar 17, 2020

@author: marbe
'''

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    # getter
    # the email is declared like a method, however we can access like an atribute                ---!!!!
    @property    
    def email(self):
        return "{} {}@email.com".format(self.first, self.last)
    
    @property     
    def fullname(self):
        return "{} {}".format(self.first, self.last)     
    
    # setter
    # that you can write a method like an atribute
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    # deleter
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
        
emp_1 = Employee("Corey","Schafer")

emp_1.first ="John"

emp_1.fullname = 'Hans Pumpernickel'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

