"""class Book:
    def __init__(self,pages):
     self.pages=pages
    def __add__(self,other):
      return self.pages+other.pages
    def __len__(self):
        return (self.pages)

# object usage
b1=Book(100)
b2=Book(200)
print("Total pages :",b1+b2)
print("PAGES IN b1 :",len(b1))
print("Pages in b2 :",len(b2))"""

"""class Bank_Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __add__(self, other):
        return self.balance +other.balance
    def __str__(self):
        return f"Name of the owner is {self.owner}, Balance of the owner is :{self.balance}"
    def __len__(self):
        return str(self.balance)
# object create
b1=Bank_Account("Deepanshu",20000)
b2=Bank_Account("Himanshu ",23000)
print(f" Bank ownner first details{b1}")
print(f"Bank owner second details {b2}")
print(f"Total of both bank accounts {b1+b2}")
print(f"Lenght of first bank account {len(b1)}")
print(len(b2))
"""


"""class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

    def __len__(self):
        # balance ke digits count return karega
        return len(str(self.balance))

    def __gt__(self, other):
        return self.balance > other.balance


# object create
b1 = BankAccount("Deepanshu", 20000)
b2 = BankAccount("Himanshu", 23000)

print("Bank owner first details:", b1)  
print("Bank owner second details:", b2)
# ek hi print function ke andar dono bank accounts print karne hey tho
print("Bank owner first details:", b1, "| Bank owner second details:", b2)

print("Total of both bank accounts:", b1 + b2)
print("Length (digits) of first bank account balance:", len(b1))
print("Length (digits) of second bank account balance:", len(b2))

print("Is b1 > b2?", b1 > b2)
"""

