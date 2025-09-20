# duck typing -- object type matter nahi karta bas methods hona chhaiye uske pass
# Duck & Dog
# Banado 2 classes – Duck aur Dog. Dono me ek sound() method ho
# (duck → “Quack”, dog → “Bark”).
# Ek function make_sound(obj) banao jo dono objects accept kare.
"""class Duck():
    def sound(self):
        print("Quack Quack")

class Dog():
    def sound(self):
        print("Bark")
def make_sound(obj):
    obj.sound()
d=Duck()
d1=Dog()
make_sound(d)
make_sound(d1)"""
#
# Calculator & Laptop
# Banado 2 classes – ek Calculator jisme compute()
# ho aur ek Laptop jisme bhi compute()
# ho. Duck typing ka use karke dono ko ek hi function me call karo.
"""
class Calculator():
    def compute(self):
        print("Compute")
class Laptop():
    def compute(self):
        print("compute")
def make_compute(obj):
    obj.compute()
C=Calculator()
L=Laptop()

make_compute(C)
make_compute(L)"""

# Next question--
"""class Pen():
    def write(self):
        print("We can write with  pen")
class Printer():
    def write(self):
        print("Printer prints the  data")
# duck typing inaction
def print_text(obj):
    obj.write()
p=Pen()
P1=Printer()

print_text(p)
print_text(P1)"""
# Payment Systems
# Banado 2 classes – CreditCard aur UPI.
# Dono me ek method pay(amount)
# ho. Ek function make_payment(obj, amount)
# banao jo dono se payment kare.
"""class Credit_Card():
    def method_pay(self):
        print("Credit Card")
class Upi():
    def method_pay(self):
        print("Upi")
def make_payment(obj):
    obj.method_pay()
c=Credit_Card()
u=Upi()
make_payment(c)
make_payment(u)"""

"""class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card ✅")

class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI ✅")

# Duck Typing in action
def make_payment(obj, amount):
    obj.pay(amount)   # yahan obj ke type ka koi matlab nahi, sirf pay() hona chahiye

# Objects
c = CreditCard()
u = UPI()

# Payment
make_payment(c, 500)   
make_payment(u, 200)   
"""
# Transport System
# Class Car me method travel(distance) aur class Bike me bhi same method ho.
# Duck typing use karke ek hi function se dono ka travel cost calculate karo
class Car:
    def travel(self, distance):
        cost = distance * 10
        print(f"Car travel cost for {distance} km: {cost}")

class Bike:
    def travel(self, distance):
        cost = distance * 5
        print(f"Bike travel cost for {distance} km: {cost}")

# Duck typing function
def calculate_cost(obj, distance):
    obj.travel(distance)   # obj ka type check nahi, bas travel() hona chahiye

# Objects
c = Car()
b = Bike()

# Calculate costs
calculate_cost(c, 15)   # Car ke liye
calculate_cost(b, 15)   # Bike ke liye



