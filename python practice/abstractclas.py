# मतलब: ऐसी class जिसका object नहीं बनाया जा सकता,
# लेकिन दूसरी classes उसे inherit कर सकती हैं।
# Abstract class एक blueprint होती है
# ये ensure करती है कि child classes कुछ specific methods implement करें
# Code structure maintain करने में help करती है


"""from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):   # abstract method (no body)
        pass

# Child class
class Dog(Animal):
    def sound(self):   # compulsory implement
        print("Dog barks: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow!")

# Objects
d = Dog()
d.sound()

c = Cat()
c.sound()
"""

"""from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")

car = Car()
car.go()
boat=Boat()
boat.go()
boat.stop()
car.stop()"""

# questionn Q1: Abstract class Shape banani hai with abstract method area().
# Child class Rectangle → area = l × b
# Child class Circle → area = π × r²
"""
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Child class Rectangle
class Rectangle(Shape):
    def area(self):
        l, b = 4, 3
        area = l * b
        print("Area of rectangle is:", area)

# Child class Circle
class Circle(Shape):
    def area(self):
        pi, r = 3.14, 2
        area_c = pi * r * r
        print("Area of circle is:", area_c)



rectangle_ = Rectangle()
rectangle_.area()

circle_ = Circle()
circle_.area()"""

"""from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):
        print("This is a shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Usage
# shape = Shape()  # ❌ Error!

rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())
rect.description()

circle = Circle(7)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
circle.description()"""

"""# School management system
from abc import ABC, abstractmethod


# Abstract class Staff
class Staff(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    def staff_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


# Teacher class
class Teacher(Staff):
    def __init__(self, name, employee_id, subject, experience_years):
        super().__init__(name, employee_id)
        self.subject = subject
        self.experience_years = experience_years

    def calculate_salary(self):
        return 30000 + (self.experience_years * 2000)

    def get_role(self):
        return "Teacher"
# Administrator class
class Administrator(Staff):
    def __init__(self, name, employee_id, department, grade):
        super().__init__(name, employee_id)
        self.department = department
        self.grade = grade

    def calculate_salary(self):
        return 25000 + (self.grade * 5000)

    def get_role(self):
        return "Administrator"


# Usage
print("=== Teacher Information ===")
teacher = Teacher("Rahul Sharma", "T001", "Mathematics", 5)
teacher.staff_info()
print(f"Role: {teacher.get_role()}")
print(f"Subject: {teacher.subject}")
print(f"Experience: {teacher.experience_years} years")
print(f"Salary: {teacher.calculate_salary()} Rs")

print("\n=== Administrator Information ===")
admin = Administrator("Priya Patel", "A001", "Accounts", 3)
admin.staff_info()
print(f"Role: {admin.get_role()}")
print(f"Department: {admin.department}")
print(f"Grade: {admin.grade}")
print(f"Salary: {admin.calculate_salary()} Rs")

"""
#
# Question:
#
# Abstract class Vehicle banao.
#
# Usme ek abstract method no_of_wheels() ho.
#
# Bike class Vehicle se inherit ho aur no_of_wheels() implement kare (2 wheels).
#
# Car class bhi Vehicle se inherit ho aur no_of_wheels() implement kare (4 wheels).
#
# Dono classes ka object banao aur unka result print karo.

"""from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        pass

class Bike(Vehicle):
    def no_of_wheels(self):
        print("No of wheels are 4")
class Car(Vehicle):
    def no_of_wheels(self):
        print("No of wheels of car 4")

    def show_info(self):
        print("Car has 4 wheels and bike has 2 wheels")

# objects create
b=Bike()
b.no_of_wheels()
c=Car()
c.no_of_wheels()
"""

#Question:
# Abstract class BankAccount banao.
# Usme ek abstract method calculate_interest() ho.
# SavingAccount class usse inherit kare aur simple interest calculate kare.
# CurrentAccount class usse inherit kare aur bole “No interest for current account”.
# Dono ka object banake unka output dikhana hai.
# 🔑 Hint
# SavingAccount me formula: Interest = (P × R × T) / 100
# CurrentAccount me sirf ek message print karna hai.
"""from abc import ABC , abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class Saving(BankAccount):
    def calculate_interest(self):
       P,R,T=3000,4,5
       interst= (P * R * T) / 100
       print("Simple Interest is :",interst)
class current(BankAccount):
    def calculate_interest(self):
        print("No interest for current account")

s1=Saving()
s1.calculate_interest()
c1=current()
c1.calculate_interest()
# calculate interest jo hey wo alag alga class mey hoga alag alag tababstract claas"""

# Abstract class Shape banao jisme ek abstract method area() ho.
# Rctangle aur Circle classes ko Shape se inherit karna hai.
# Rectangle ka area = length × breadth
# Circle ka area = π × radius²
# Rectangle aur Circle ke object banao aur unka area calculate karke print karo.
# 💡 Hint:
# math module ka use karke pi le sakta hai.
# Abstract class force karegi ki har child class apna area() define kare.


"""from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        length,breadth=3,4
        area = length*breadth
        print("Area of a Rectangle is :", area)

class Circle(Shape):
    def area(self):
        pi,r=3.14,4
        area=pi*r*r
        print("Area of a circle is ",area)

r1=Rectangle()
r1.area()
c1=Circle()
c1.area()"""

# user sey values
"""from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area of Rectangle is:", self.l * self.b)

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        pi = 3.14
        print("Area of Circle is:", pi * self.r * self.r)

# Objects with dynamic values
r1 = Rectangle(5, 7)
r1.area()

c1 = Circle(6)
c1.area()"""
