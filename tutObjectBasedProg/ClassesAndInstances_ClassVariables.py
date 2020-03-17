'''
Created on Mar 17, 2020

@author: marbe
'''

class Employee:
    
    # class variable (for any instance the same)
    num_of_emps = 0
    raise_amount = 1.04
    
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
        #self.pay = int(self.pay * Employee.raise_amount)    
            # or
        # self.raise_amount could be may different from one to the other employee -> so with self it would be possible to create an own number per instance
        self.pay = int(self.pay * self.raise_amount)  

        
emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)   
        
print(Employee.num_of_emps)

'''        

# possible to change the raise for emp_1 -> not anymore a class variable
emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
'''

'''
print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


print(Employee.fullname(emp_1))
print(emp_2.fullname())
'''
