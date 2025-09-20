"""# super() - jab ek child class parent class ke methods ya constructor reuse karna chahta ho
#code--
class Person():
     def __init__(self,name,age):
         self.name=name
         self.age=age
     def show_info(self):
         print(f"Name:{self.name},AGE:{self.age}")
class Student(Person):
     def __init__(self,name,age,roll_no,course): #yaha bhi define karna padega name age ko
         super().__init__(name,age)  # galti yey thi ki hamne bhar call kardi thi
         self.roll_no = roll_no
         self.course = course
     def show_student_info(self):
         # parent metod call
         super().show_info()
         print(f"Roll No: {self.roll_no}, Course: {self.course}")

#object create kaerte hain
s1= Student("Deepanshu",21,101,"bca")
s1.show_student_info()
"""

# Question ---2
"""class Vehicle():
    def __init__(self,brand,model):
     self.brand=brand
     self.model=model
    def show_info(self):
         print(f"Brand :{self.brand}, Model : {self.model}")

class Car(Vehicle):
    def __init__(self,brand,model,fuel_type,seats):
     super().__init__(brand,model)
     self.seats=seats
     self.fuel_type=fuel_type
    def show_car_info(self):
     super().show_info()
     print(f"Seats :{self.seats}, Fue Type {self.fuel_type}")
#Object create
c1=Car("Fortuner","Toyota","Diesel",7)
c1.show_car_info()
"""

# Question 3--
"""class Employee:
     def __init__(self,name,salary):
         self.name=name
         self.salary = salary
     def show_details(self):
          print(f"Name of the  employee :{self.name} , Salary {self.salary}")

class Manager(Employee):
     def __init__(self,name,salary,department):
         super().__init__(name,salary)
         self.department=department
     def show_manager_details(self):
         super().show_details()
         print(f"Department is {self.department}")

class Developer(Employee):
    def __init__(self,name,salary,programming):
        self.programming=programming
        super().__init__(name,salary)
    def show_developer_details(self):
        super().show_details()
        print(f"Programming language {self.programming}")

# object create
m1 =Manager("Deepanshu",20000,"BCA")
m1.show_manager_details()

d1= Developer("Vishal","30000","Dart")
d1.show_developer_details()
"""