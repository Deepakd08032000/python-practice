class Employee:   #template
    no_of_leave = 4    #class variable
    pass

ddd = Employee()       #object
deepak = Employee()    
ddd.name = "deepak"
ddd.salary = 455
ddd.role = "inspector"
deepak.name = "eepak"
deepak.salary = 45
deepak.role = "iAs"   #instance of class
Employee.no_of_leave = 6
print(ddd.no_of_leave)
print(deepak.__dict__)
print(deepak.no_of_leave)
