#  #Property--Normally jab hum kisi attribute (jaise balance) ko access karte hain, wo directly
#  variable ke through hota hai.
# But kabhi-kabhi hume chahiye hota hai ki jab wo
# attribute access ho, tab kuch extra logic run ho (jaise validation, formatting, calculation).
# Iske liye hum @property decorator use karte hain.
# Ye ek method ko attribute ki tarah behave karwa deta hai.
# getter, setter, aur deleter ke liye use hota hai.
# Kaise hota hai?
#
# Getter (@property) → jab tum attribute ko read karna chahte ho.
# Example: print(s1.marks) → internally method call hoga jo marks return karega.
#
# Setter (@marks.setter) → jab tum attribute ko update karna chahte ho.
# Example: s1.marks = 95 → setter method check karega ki value valid hai ya nahi.
"""class Student:
        def __init__(self, name, marks):
            self._name = name
            self._marks = marks

        @property
        def marks(self):
            return self._marks

        @marks.setter
        def marks(self, value):
            if value < 0 or value > 100:
                print("Invalid marks! (0-100 allowed)")
            else:
                self._marks = value

    # Object create
s1 = Student("Deepanshu", 90)

print(s1.marks)  # attribute ki tarah access ho raha hai
s1.marks = 105  # setter call hoga
print(s1.marks)"""



# ⚠️ Problem → Negative marks bhi assign ho gaye.
#
# Matlab koi bhi galat value directly set kar dega.
#
# Property ka kaam
#
# Property ka matlab hai:
# 👉 Tum apne variable/attribute ko protected rakhte ho aur control
# karte ho ki usme kya value set ho sakti hai aur kaise access hoga.

# question --2 bank balance
# negativ balance is not allowed
# without property
"""class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
#object creation
acc=BankAccount("Deepanshu",2000)
print(acc.balance)
acc.balance=-1000 # that cannot be possible
print(acc.balance)
#acc.balance()--method"""

# use property
"""class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # note: private bana diya (underscore laga ke)
    @property
    #getter
    def balance(self):
       return self._balance
    #setter
    @balance.setter
    def balance(self,amount):
        if amount<0:
            print("Balance can't be negative")
        else:
            self._balance=amount #amount value goes to balance
# object
acc=BankAccount("Deepanshu",2000)
print(acc.balance) #getter call 2000
acc.balance=-3000 #setter call balance cant be negative"""

# question - tempreature
"""
class Tempreature:
    def __init__(self,celsius):
        self._celsius=celsius
    @property
    def celsius(self):
        return self._celsius
    @property
    def faherniet(self):
        return (self.celsius*915)+32
    #condtiton
    @celsius.setter
    def celsius(self,value):
        if value<-273:
            print("Tempreature below -273")
        else:
            self._celsius=value
# object creation
temp=Tempreature(2.14)
print(temp.celsius)
print(temp.faherniet)
temp.celsius=-300
print(temp.celsius)"""

# next question
"""class Student:
    def __init__(self,name,marks):
        self.name=name
        self._marks=marks
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self,value):
        if value<0 or value>100:
            print("Value must be in 1 -100")
            raise ValueError("Marks must be between 0 and 100")
        self._marks = value

    @property
    def grade(self):
        if self._marks >= 90:
            return "A"
        elif self._marks >= 75:
            return "B"
        elif self._marks >= 50:
            return "C"
        else:
            return "F"
# ---- Test Code ----
s1 = Student("Ravi", 85)
print(f"Name: {s1.name}, Marks: {s1.marks}, Grade: {s1.grade}")

s1.marks = 95
print(f"Updated Marks: {s1.marks}, Grade: {s1.grade}")

# Invalid marks
# s1.marks = 150   # ❌ ValueError"""

class BankAccount:
    def __init__(self, balance):
        self._balance = None   # private variable
        self.balance = balance # setter call hoga

    # balance getter
    @property
    def balance(self):
        return self._balance

    # balance setter
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    # sirf read-only property → interest
    @property
    def interest(self):
        return self._balance * 0.05   # 5% yearly interest


# ---- Test ----
acc = BankAccount(1000)
print("Balance:", acc.balance)
print("Interest (5%):", acc.interest)

# Update balance
acc.balance = 2000
print("Updated Balance:", acc.balance)
print("Updated Interest:", acc.interest)

# Negative balance test
# acc.balance = -500  # ❌ ValueError
