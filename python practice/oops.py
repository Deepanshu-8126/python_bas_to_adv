# Oops - OBJECT ORIENTED Programming language
# Python ek Object-Oriented Language hai.
# oops ek aisa tarika hai programming karne ka jisme hum real world
# cheezon ko code mein object ki tarah represent karte hain.
# 💡 Example:
# Real life mein ek Car hoti hai →
# Python mein hum uska ek class bana sakte hain.
# Car ke features hote hain
# → color, brand, model →
# OOPS mein inhe attributes/properties (variables) bolte hain.
# Car ke actions hote hain →
# start(), brake(), horn() →
# OOPS mein inhe methods (functions) bolte hain.


#CODEEEEEE-
"""class Student:
    # init ek constructor hey yey automatically call hota hey jab object banta hey
    #self current objecct adres jo ban raha hey name and age are parameters
    def __init__(self,name,age):
      self.name=name#instance variable object ke andar ek variable bana dete hey called instance
      self.age=age





    def display(self):
          print(f"My name is {self.name} and I am {self.age} years old.")
          #self use karke objecct ke data ko acess kar sakte hey
#error aaya tha because display constructor ka hi part heey
#object banajjna
s1=Student("Deepanshu",21)
s2=Student("Vishal",22)

s1.display()
s2.display()"""
# Questionss
# Ek Car class banao jisme constructor brand aur model le.
# Phir ek display_info() method banao jo car ka brand aur model print kare.
# 👉 Object banao aur method call karo.
'''class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display_info(self):
         print(f"Your brand is{self.brand}and  model is {self.model}")

#objects
s1=Car("tATA",2017)
s2=Car("bmv",3045)

s1.display_info()
s2.display_info()'''
# Q2.
# Ek Book class banao
#     jisme constructor title aur author le.
# Ek show_details() method banao jo
# "Book Title is <title> written by <author>" print kare.
'''class Book:
    def __init__(self,title,author):
        self.title= title
        self.author=author
    def display (self):
       print(f"Book title is {self.title} written by author {self.author}")

d1=Book("C language","Dennis Ritchie")
d2=Book("python","d")

d1.display()
d2.display()'''

# #Q3.
# Ek Employee class banao jisme constructor name aur salary le.
# Ek method give_bonus() banao jo salary me 5000 add kare aur updated salary print kare.
# 👉 Object banake pehle salary aur bonus ke baad salary dikhana.

'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def give_bonus(self):
        self.salary+=5000
        print("updated salary",self.salary)
emp1=Employee("Deepanshu",2000)
emp1.give_bonus()'''''
# Q4.
# Ek Dog class banao jisme constructor name aur age le.
# Ek method bark() banao jo print kare "Woof! My name is <name>".
# 👉 Do dog objects banao aur bark method call karo.
'''class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
       print(f"Woof! My name is {self.name} and my age is {self.age}")

#Objects create karte hey
d1=Dog("Rocky",17)
d2=Dog("jackey",12)

d1.bark()
d2.bark()'''
#
# Q5.
# Ek Laptop class banao jisme constructor brand aur price le.
# Ek method apply_discount() banao jo price ka 10% kam kare aur naya price print kare.
# 👉 Alag-alag laptops ke liye method call karo.
'''class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def apply_discount(self):
     discount=self.price*0.10
     self.price = self.price - discount  #  self.price -= discount
     print("New Price after discount",self.price)

laptop1 = Laptop("Dell", 50000)
laptop2 = Laptop("HP", 60000)
laptop3 = Laptop("Lenovo", 45000)

#before discount
print("Before discount:")
print(laptop1.brand, "price:", laptop1.price)
print(laptop2.brand, "price:", laptop2.price)
print(laptop3.brand, "price:", laptop3.price)

laptop1.apply_discount()'''

# Main topic -- class variable and instance variable
# Class variables vs Instance variables
# Abhi tu self.name, self.age banata tha (yeh instance variables hain →
# har object ke liye alag value hoti hai).
# Lekin class variables hoti hain jo sabhi objects me common hoti hain.

'''class Student:
    #class varibale yey sabke liye same
    college_name ="Miet Kumoan"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print(f"Your name is {self.name}, and roll no is {self.roll_no} and you are from {Student.college_name}")

s1=Student("Deepansu",19)
s2= Student("Himanshu", 19)
s1.display()
s2.display()'''
# ⚡ Ab tere liye Practice Questions (Class Variables)
# Car Company Example
# Ek Car class bana jisme class variable wheels = 4 ho.
# Object me alag-alag name aur color le
# Ek method show_details() bana jo car ka naam, color aur wheels print kare.
# wheels ko class ke through update karke
# check kar ke dekh (sab object ke liye update hona chahiye).
'''class Car:
    wheels = 4
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def show_details(self):
        print(f"car name is {self.name} and car color is {self.color} and wheels are {Car.wheels}")
c1 = Car("bmw","blue")
c2= Car("bugati chiron","black ")

c1.show_details()
c2.show_details()'''

# Bank Example
# Ek BankAccount class bana jisme class variable bank_name = "SBI Bank" ho.
# Instance variables: holder_name, balance
# Method: account_info() → jo holder name, balance aur bank name print kare.
# bank_name ko change karke sab accounts ke liye check kar.

'''class bank_account():
    bank_name = ("Sbi bank")
    def __init__(self,holder_name,balance):
        self.holder_name=holder_name
        self.balance=balance
    def account_info(self):
        print(f"Holder name is {self.holder_name}, balance is {self.balance} , bank name is {bank_account.bank_name}")

h1=bank_account("Deepanshu",20000)
h2=bank_account("Vishal",20000)

h2.account_info()
h1.account_info()'''

# New Topic
# Class variables and static variables
# revise -- 1️⃣ Instance Method (jo tu already use kar raha hai)
# Ye methods object ke sath kaam karte hain.
# Hamesha self parameter hota hai
# Instance variables ko access/change karte hain.
# 2️⃣ Class Method
# Ye methods class variables ke sath kaam karte hain.
# @classmethod decorator use karte hain.
# Iska pehla argument cls hota hai (self ki jagah).
'''class Student:
    school = "NEPS"  #class variable
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def change_school(cls, new_name): # argumrnt cls hota hey 
      cls.school = new_name
    # Before change
print(Student.school)
    # Change using class method
Student.change_school("DPS School")
    # After change
print(Student.school)
'''
# 3️⃣ Static Method
#
# Ye methods class/instance se directly related nahi hote,
# bas logically class ke andar hote hain.
# @staticmethod decorator use karte hain.
# Ye self ya cls nahi lete.
#👉 Example:
'''
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 7))   # 12'''

'''# Questions
class Bank:
    bank_name= "SBI BANK"
    def __init__(self,holder_name,balance):
        self.holder_name=holder_name
        self.balance=balance
    def show_info(self):
             print(  f"Account holder : {self.holder_name}, balance {self.balance}, bank{self.bank_name}")
    @classmethod
    def change_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def bank_policy():
        print("Minimum balance should be 1000 ruppes")
#object create
h1 =Bank("Deepansu",20000)
h2= Bank("Vishal",30000)
h1.show_info()
h2.show_info()
#before bank account name
print(Bank.bank_name)
#after bank name
#change new bank account name
Bank.change_name="Baroda Bank of India"
print(Bank.change_name)'''

# Question - library system
"""class library:
    library_name = "City Library"
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def show_info(self):
        print(f"Library title {self.title}, author{self.title}, library name {self.library_name}")
        @classmethod
        def change_name(cls,newname):
            cls.library_name = newname
        @staticmethod
        def library_rules():
            print("Return books within 14 days")

l1=library("fifa","dk")
l2=library("fgh","fg")

l1.show_info()
l2.show_info()

#before name of library
print(library.library_name)
#after library name
library.change_name="FIFA"
print(library.change_name)"""
