class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"From Person constructor")
    def my_info(self):
        print(f"My name is: {self.name}")

class Employee(Person):
    def __init__(self,name,age,emp_id,dept):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.dept=dept
        print("From Employee Constructor")
    def my_info(self):
       print(f"My name is:{self.name}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, dept,proj_fund):
        super().__init__(name, age, emp_id, dept)
        self.proj_fund=proj_fund
        print("Manager Constructor")
        print(self.name)
        
a=Person("Ram",9)#1.Case:- Will not print ram name
b=Employee("Shyam",18,"001CS","CS")#2Case:-Will get shyam name using another fun
b.my_info()
c=Manager("Mohan",9,"001CS","CS",2000)#3-Will get Mohan name Manager