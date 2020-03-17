'''
Created on Mar 17, 2020

@author: marbe
'''
from numpy.ma.core import append

class Employee:
    
    # class variable (for any instance the same)
    raise_amount = 1.04
    
    # -------------------------- regulars methods -> first always self (instance)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)     
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  


# Subclasses
class Developer(Employee):
    raise_amount = 1.10
    
    # overwrite the init method
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # or (but better with super()
        # Employee.__init__(self, first, last, pay)
        
        self.prog_lang = prog_lang
        
class Manager(Employee):
    
    # overwrite the init method
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
     
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp) 
    
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())
            
dev_1 = Developer("Corey","Schafer",50000,"Python")
dev_2 = Developer("Test","User",60000,"Java")   

mgr_1 = Manager("Sue","Smith",90000,[dev_1])

# checks if the object is an instance of a class                                    ----!!!!!
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

'''
print(mgr_1.email)

mgr_1.add_employee(dev_2)
mgr_1.remove_employee(dev_1)

mgr_1.print_emps()
'''

'''
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
'''

# help for the class -> informatrion                                                        ------------!!!!!!
#print(help(Developer))

#print(dev_1.email)
#print(dev_2.email)