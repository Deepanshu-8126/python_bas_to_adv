#POlymorphism = poly msy morphism -- many forms
# There are two methods of performing polymorphism 1- inheritanfce 2- duck typing
# ep 2: Python me 2 tareeke se hota hai
# Polymorphism with Functions and Objects
# Ek hi function call karega, but different class ke objects alag output denge.
# Polymorphism with Inheritance (Method Overriding)
# Child class parent ke method ko apne hisaab se override karega.
"""class Bird():
    def fly(self):
        print("Bird can fly")
class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b = Bird()
b.fly()
p=Penguin()
p.fly()
"""

# Question
"""class Bank_Account():
    def calculate_interst(self):
        pass

class Savings_Account(Bank_Account):
    def calculate_interst(self,P,R,T):
         # Simple Interest
         interest = (P * R * T) / 100
         print(f"Simple Interest on Saving Account: {interest}")
class CurrentAccount(Bank_Account):
    def calculate_interest(self, P, R, T):
        # Current accounts usually don't give interest
        print("No interest for Current Account.")

class FixedDeposit(Bank_Account):
    def calculate_interest(self, P, R, T):
        # Compound Interest
        amount = P * (1 + R/100) ** T
        ci = amount - P
        print(f"Compound Interest on Fixed Deposit: {ci}")

# OBJECT IN POLYMORPHISM
account=[Savings_Account(),CurrentAccount(),FixedDeposit()]
P, R, T = 10000, 5, 2
for acc in account:
    acc.calculate_interest(P,R,T)
"""

# Shape area calculator
"""class Shape():
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of a Rectangle is:", self.l * self.b)


class Circle(Shape):
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def area(self):
        print("Area of a Circle is:", self.pi * self.r*self.r)


# object create
r=Rectangle(2,3)
c=Circle(3.14,4)

r.area()
r.area()
"""
# Return value method
"""class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

r = Rectangle(5, 3)

print("Rectangle Area:", r.area())  # 15"""

#loops
"""

# ✅ objects ek list me daal do
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(6, 8)
]

# ✅ loop se har ek ka area nikalna
for s in shapes:
    print("Area:", s.area())"""

# Question - payment System
"""class Payment():
    def pay(self):
        pass
class Credit_Card(Payment):
    def pay(self):
        print("PAYMENT DONE USING CREDIT CARD")
class PAYPAL(Payment):
    def pay(self):
        print("Payment done with pay pal")

#Object ek list
payment =[Credit_Card(),PAYPAL()]
for p in payment:
    p.pay()"""

# use of abstract class and loop hard question
"""from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self):
        pass

class Bus(Transport):
    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        print("Bus Fare:", self.distance * 10)

class Train(Transport):
    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        print("Train Fare:", self.distance * 5)

class Flight(Transport):
    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        print("Flight Fare:", self.distance * 50)


# Objects ko ek hi list me dal kar loop se call
transports = [Bus(100), Train(100), Flight(100)]

for t in transports:
    t.calculate_fare()

"""
# second method super
"""from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, distance):   # Parent constructor
        self.distance = distance

    @abstractmethod
    def calculate_fare(self):
        pass

class Bus(Transport):
    def __init__(self, distance):
        super().__init__(distance)   # parent constructor call

    def calculate_fare(self):
        print("Bus Fare:", self.distance * 10)

class Train(Transport):
    def __init__(self, distance):
        super().__init__(distance)

    def calculate_fare(self):
        print("Train Fare:", self.distance * 5)

class Flight(Transport):
    def __init__(self, distance):
        super().__init__(distance)

    def calculate_fare(self):
        print("Flight Fare:", self.distance * 50)


# Objects list
transports = [Bus(100), Train(100), Flight(100)]

for t in transports:
    t.calculate_fare()

"""
"""from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, distance):
        self.distance = distance

    @abstractmethod
    def calculate_fare(self):
        pass

class Bus(Transport):
    def __init__(self, distance):
        super().__init__(distance)

    def calculate_fare(self):
        return self.distance * 10

class Train(Transport):
    def __init__(self, distance):
        super().__init__(distance)

    def calculate_fare(self):
        return self.distance * 5

class Flight(Transport):
    def __init__(self, distance):
        super().__init__(distance)

    def calculate_fare(self):
        return self.distance * 50


# Objects list
transports = [Bus(100), Train(100), Flight(100)]

for t in transports:
    print(f"{t.__class__.__name__} Fare: {t.calculate_fare()}")"""

# Question --
class Animal():
    def make_sound(self):
        pass
    def move(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Dog make sound too much")
    def move(self):
        print("Dog can move")
class Bird(Animal):
    def make_sound(self):
        print("Bird can fly")
    def move(self):
        print("Bird can  move")
# object
animal=[Dog(),Bird()]
for a in animal:
    a.make_sound()
    a.move()