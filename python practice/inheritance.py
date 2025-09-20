#INHERITANCE
#Child class use properties and methods of parent class
# parent class
#self always represents the current object.
# Jab tu d.bark() call karta hai
# → Python internally likhta hai Dog.bark(d).
# Isliye bark(self) ke andar self = d ho jata hai
'''class Animal:
    def speak(self):
        print("animal speak in its own way")
# child class
class Dog(Animal): #dog is inheriting animal
    def bark(self):
        print("Dog barks: Woof! Woof!")

#Objects methods
a = Animal()
a.speak()

#dog
d = Dog()
d.bark() # apna method bhhi use karega
d.speak() # parent ka bhi method use kar sakta hey
'''
# At constructor ke sath
# Question
'''class Vehicle():
    def move(self):
        print("Vehicle can move")
class Car(Vehicle):
    def honk(self):
     print("Car horns beep beep")
c = Vehicle()     # Object बनाया
c.move()          # move method call की

h = Car()         # Car object बनाया
h.honk()          # honk method call की
h.move()          # inherited move method call की (Vehicle से आया है)'''

# Q2: Person → Student
#
# Ek parent class Person banao jisme method details()
# ho jo ek naam print kare.
# Ek child class Student banao jo apna method study()
# rakhe jo print kare "Student is studying".
# Object banake parent aur child dono ke methods call karo.

'''class Person():
    def details(self):
        print("Your name is Deepanshu")
class Child(Person):
    def study(self):
        print(f"Deepanshu is studying")

# object banate hey
p = Person()
p.details()
c = Child()
c.study()
c.details()'''

#Mutiple Inheritance
#one class multiple parents'''

#  Question 1: Banking System
# Scenario: एक bank में different types of accounts हैं
# Requirements:
# BankAccount abstract class बनाओ:
# Attributes: account_number, balance, account_holder
# Abstract methods: calculate_interest(), get_account_type()
# Normal methods: deposit(), withdraw(), get_balance()
# SavingsAccount class:
# Interest rate = 4% per annum
# Minimum balance = 1000 Rs
# Withdrawal limit = 50000 per day
# CurrentAccount class:
# Interest rate = 1% per annum
# No minimum balance
# No withdrawal limit
# Overdraft facility = 10000 Rs
# Task: Dono accounts के objects बनाओ और transactions करो
'''from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass
    @abstractmethod
    def get_account_type(self):
        pass
class Savings_Account(ABC):
    def calculate_interest(self):
        P = 1000  # Principal
        R = 4  # Rate of Interest (4% per annum)
        T = 2  # Time in years

        interest = (P * R * T) / 100
        print("Simple Interest:", interest)

    def get_account_type(self):
        print("===Savings Account====")
        print("Minimum Balance will be 1000")
        print("Withdrawl limit 50000 per day")

class Current_Account(ABC):
    def calculate_interest(self):
      P = 1000  # Principa# l
      R = 1 # Rate of Interest (4% per annum)
      T = 2  # Time in years
      interest = (P * R * T) / 100
      print("Simple Interest :", interest)

    def get_account_type(self):
      print("===Current Account====")
      print("No minimum balance")
      print("No withdrawl limit")
      print("Overdraft facility = 10000 Rs")

s1=Savings_Account()
s1.calculate_interest()
s1.get_account_type()
c1=Current_Account()
c1.calculate_interest()
c1.get_account_type()
'''
"""from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    @abstractmethod
    def calculate_interest(self):
        pass

    @abstractmethod
    def get_account_type(self):
        pass

    # Normal methods
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance


# Savings Account - ABC हटाना है क्योंकि ये concrete class है
class Savings_Account(BankAccount):  # Parent class BankAccount को inherit करे
    def __init__(self, account_number, balance, account_holder):
        super().__init__(account_number, balance, account_holder)

    def calculate_interest(self):
        # यहाँ dynamic values use करनी चाहिए, hardcoded नहीं
        interest = (self.balance * 4 * 1) / 100  # 4% for 1 year
        return interest

    def get_account_type(self):
        return "Savings Account"

    def display_info(self):
        print("=== Savings Account ===")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print("Minimum Balance: 1000 Rs")
        print("Withdrawal limit: 50000 per day")


# Current Account - ABC हटाना है
class Current_Account(BankAccount):  # Parent class BankAccount को inherit करे
    def __init__(self, account_number, balance, account_holder):
        super().__init__(account_number, balance, account_holder)

    def calculate_interest(self):
        interest = (self.balance * 1 * 1) / 100  # 1% for 1 year
        return interest

    def get_account_type(self):
        return "Current Account"

    def display_info(self):
        print("=== Current Account ===")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print("No minimum balance")
        print("No withdrawal limit")
        print("Overdraft facility: 10000 Rs")


# Usage
print("=== Savings Account ===")
savings = Savings_Account("SA001", 25000, "Rahul Sharma")
savings.display_info()
print(f"Interest for 1 year: {savings.calculate_interest()} Rs")
savings.deposit(5000)
savings.withdraw(10000)

print("\n=== Current Account ===")
current = Current_Account("CA001", 100000, "Priya Patel")
current.display_info()
print(f"Interest for 1 year: {current.calculate_interest()} Rs")
current.deposit(20000)
current.withdraw(50000)"""
