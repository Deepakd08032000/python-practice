class Employee:   #template
    no_of_leave = 4    #class variable

    def __init__(self , aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    
    def printdetails(self):   #method of class
        return f" the name is {self.name} salary is {self.salary} and role is {self.role}"
        # f string




# ddd = Employee()       #object
# deepak = Employee()    
# ddd.name = "deepak"
# ddd.salary = 455
# ddd.role = "inspector"


# deepak.name = "eepak"
# deepak.salary = 45
# deepak.role = "iAs"   #instance of class
# print(ddd.printdetails())
# print(deepak.printdetails())

deepak = Employee("deepak" , 355 , "inspector")   #work as constructor
print(deepak.name)