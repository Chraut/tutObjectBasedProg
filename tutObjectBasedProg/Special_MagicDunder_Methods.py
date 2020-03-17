'''
Created on Mar 17, 2020

@author: marbe
'''

class Employee:
    
    raise_amount = 1.04
    
    # __  is called dunder             you say: "dunder" init "dunder"                ----!!!!!
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)     
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  
    
    
    # the __repr__ and __str__ should always be implemented                                    ----!!!!
    
    # for debuging of logging -> when you now print(instanmce) it shows with which parameters the instance was created 
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)
    
    # readable representive of the object
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    # my own adding (magic) method
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    
emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)   


print(len("test"))
print(len(emp_1))  # for our function


# defined the add function above __add__()
#print(emp_1 + emp_2)

#print(repr(emp_1))
#print(str(emp_1))

'''
# the behavior of adding a string or a number is different
print(1+2)
print(int.__add__(1,2))

print('A'+'B')
print(str.__add__('A','B'))
'''