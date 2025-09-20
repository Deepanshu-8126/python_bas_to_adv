# FIRST Program
'''print("Hi World i am deepanshu")'''

# Variables

# Strings
'''first_name = "Deepanshu"
last_name = "Kapri"
food = "Burger"
email = "deepanshukapri4@gmail.com"
print(f"hi my name is {first_name} {last_name}")
print(f"I like {food}")
print(f"My email is {email}")'''

#INTEGERS
'''age = 19
quantity = 34
num_of_students = 39
print(f"You are {age} old ")
print(f"You are buyingg {quantity} items")
print(f"You class has {num_of_students} students")'''

#FLOAT
'''price = 3.14
ran = 3.15
print(f"Price is {price} ")
print(f"You can run {ran} km")'''

#BOOLEAN
'''is_student = True
if is_student:
            print(f"Are you a student ")
else:
    print("You are not a student")'''

'''for_sale = True
if for_sale:
    print("This item is for the sale ")
else:
    print("This item is not available")'''

# Type casting

'''age = 18
gpa = 7.8
name = "Deepanshu"
print(type(age)) # integer data type
gpa = int(gpa)
print(gpa)
print(type(gpa))
age = float(age)
print(age)'''

'''age = "18"
age = int(age)
age = age + 1
print(age)'''

# INPUT
'''name = input("Enter your name :")
age = int(input("Enter your age :"))
age = age +1

print(f"Hi my name is {name} :")
print("Happy Birthday")
print(f"You are {age} years old")'''

# ExERCISE 1 area
'''length = int(input("Enter length :"))
width = int(input("Enter width"))
area = length*width
print(f"Area is {area} :")'''

# Exercise 2 - Shoppinng cart program
'''item=input("Enter what would you like to buy ? ")
quantity= int(input("How much would you like ?"))
price=float(input("What is the price ?"))
total= quantity*price

print(f"You have bought {quantity} {item}s")
print(f"Your total is {total } :")'''

# EXercise ---3
# Matplibs game
# fill in the games where you create a story

# Basic arithmethic operators
#ASsignment operatos
# freinds = 0
# freinds+=1
# print(freinds)

'''friends = 4
#friends*=9
#friends**=2 # 2 power of 4
#remainder = friends%2 #0
print(remainder)'''

# Round FUNCTION
'''x = 3.14
y = -3
z = 9
result = round(x) # round it off
#
# result = pow(3,4) # power of 3 into 4 times 81
# print(result)
# print(abs(y)) #distance away from zero (-3) --- (-4)
# print(result)
#maximum find and minimum
result = max(x,y,z)
min = min(x,y,z)
print(min)
print(result)'''

# IMPORT

'''import math
x = 9
sqaure = math.sqrt(x)
print(sqaure)'''

# Exercise circumference of a circle
'''import math
math.pi
radius = float(input("Enter radius of a  circle :"))
circumference = 2*math.pi*radius
print(math.pi)
print(circumference)
result = radius
radius = int(radius)
print(radius)'''

# Exercise area of a circle pi*radius*radius
'''import math
radius = float(input("Enter radius of a circle ?"))
area = math.pi*pow(radius,2)
print(f"Area of a circle is {area}")'''

#EXERCISE - Find hypotenuse of a rectangle formula sqaure root of a square + b square
'''import math
a = float(input("Enter side of a "))
b = float(input("Enter side of b "))
hypotenuse = math.sqrt(pow(a,2)+pow(b,2))
print(hypotenuse) '''


