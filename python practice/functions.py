'''def greet():
    print("Hello World i am deepanshu")
greet()'''


# 4. Function with Parameters
# def greet(name):
#     print("Hello " , name)
# greet("Rahul")
# greet("Deepanshu")

# Using function print any number of table
'''def fun (num):
    for i in range(1,11):
        print(f"Table of {num} is :{num}*{i}={num*i}")

fun(3)'''
# Using while loop
'''def fun(num):
    i= 1
    while i<=10:
        print(f"Table of this number is :{num}*{i}:{num*i}")
        i+=1

fun(4)'''


# Functions questions

'''def greet():
    print("Hello WORLD")
greet()

# Sqaure return
def square(n):
    return n * n

# Example calls
print(square(5))   # Output: 25
print(square(10))  # Output: 100

# Even
def even(n):
 if n%2==0:
     return "Even"
 else:
     return "Odd"

print(even(55))'''

#-----------------
#-- Function
#Argument and parameter assignment
'''def greet(name):
    print("Hello", name)

greet("Aman")
greet("Ravi")'''

#Default argument
'''def greet(name="deepanshu"):
    print("Hello ", name)
greet()
greet("Himanshu")'''

#Return Statement
# Function result return bhi kar sakta hai.
'''def add(a, b):
   return  a+b
result = add(a,b)
print(add(4,5))'''


# Keyword agrument
# Order matter nahi karega agar naam se input doge.

'''def intro(name, age):
    print("Name:", name, "Age:", age)

intro(age=20, name="Ravi")'''

# def fun(name,age,roll_no):
#    print(f"Name:{name},Age:{age}, Roll no :{roll_no}")
#
# fun(age = 20, name = "Deepanshu",roll_no=45)
# # Order doesnnt matter
'''def fun(*args):
    total=0
    for num in args:
        total = total+num'''
# x =[1,2,[3,4]]
# x[2].append(5)
# print(x)