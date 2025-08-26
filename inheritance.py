#INHERITANCE
#Child class use properties and methods of parent class
'''class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    # Chuld class
class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Mouse(Animal):
    pass
Dog=Dog("Scooby")
Cat = Cat("Rubby")
Mouse = Mouse("Rocky")

Dog.sleep()
Cat.sleep()
Mouse.sleep()'''


# Multiple inheritance
'''class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):   # inheritance ho gaya
    pass

obj = Child()
obj.greet()   # Output: Hello from Parent!'''

# Q1: Single Inheritance
#
# 👉 Ek Person class bana, jisme name aur age store ho.
# 👉 Ek Student class bana jo Person ko inherit kare, aur usme ek roll_number add kare.
# 👉 Input leke dono ko print kar.
'''class Person:
    def Pers(self, age, name):
        print(f"Roll no is 23, Name: {name}, Age: {age}")


class Student(Person):
    pass


c = Student()
c.Pers(20, "Rahul") '''





