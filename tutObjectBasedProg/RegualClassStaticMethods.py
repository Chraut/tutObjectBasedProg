'''
Created on Mar 17, 2020

@author: marbe
'''
from builtins import staticmethod

class Employee:
    
    # class variable (for any instance the same)
    num_of_emps = 0
    raise_amount = 1.04
    
    # -------------------------- regulars methods -> first always self (instance)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        # always takes the class variable -> so employees is always 1 number
        Employee.num_of_emps += 1
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)     
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  
    
    # -------------------------- class methods -> first always cls (class)
    @classmethod
    def set_raise_amp(cls, amount): 
        cls.raise_amount = amount
    
    # class methods as alternative constructors               ---!!!!
    @classmethod
    def from_string(cls,emp_str):    
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    # -------------------------- static methods -> nothing first.. static
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)   

import datetime
my_date = datetime.date(2020, 3, 18)

print(Employee.is_workday(my_date))

'''
emp_str_1 = "John-Elder-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "BJ-Hopkins-90000"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_1.pay)
'''


'''
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)    

Employee.set_raise_amp(1.05)    

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)   
'''
