# # Area of a rectangle
# length = int(input("Enter length"))
# width =  int(input("Enter width :"))
# area =  length * width
# print(area)

# Calculator
'''operator = input("Enter operator + - * /  %  : ")
num1 = int(input("Enter first number :"))
num2= int(input("Enter  second number :"))
if operator == "+":
    result = num1+num2
    print(f"Multiplication of this number is {result}")
elif operator == "-":
    result = num1-num2
    print(f"Subtraction of this number is {result }")
elif operator =="*":
    result = num1 *num2
    print(f"Multiplication of this number is {result}")
elif operator == "%":
    result = num1%num2
print(f"Divison of this number is {result}")
else:
    print(f"{operator} is not valid")'''

row=8
# clm=8
# for i in range(1,row+1):        #8 times loop will run
#     for j in range(clm//2):     #4 time loop runs prinitng 2 patterns (4*2=8)
#         if i%2!=0:              #If row is odd
#             print("X  0  ",end="")
#         else:                   #If row is even
#             print("0  X  ",end="")
#     print()

# def median(l):
#     l.sort()     #sort list
#     n=len(l)
#     if n%2==1:   #odd length
#         mid1=l[n//2]
#     else:        #even length
#         a=l[n//2]
#         b=l[(n//2)-1]
#         mid1=(a+b)/2
#     print(f"Median = {mid1}")
# l=[1,2,3,4,6,7,5]
# median(l)

'''def largest(a,b,c):
    return  max(a,b,c) # in built function
print(largest(10,20,30))

def largest(a,b,c):'''

# Type casting
# Means convert one data type into another data type

#1----Ek integer input lo aur usko float me convert karke print karo.
'''num = int(input("Enter any number"))
b =float(num)
print(b)'''

#2--Ek float input lo aur usko integer me convert karo (decimal part hat jana chahiye).
'''number = float(input("Enter any number"))
y=int(number)
print(y)'''

#3--Ek string "100" ko integer me convert karo aur 50 add karke result print karo.

'''a = "100"
b = int(a)
print(f"{b+50}")'''


#4--Ek integer ko string me convert karke uska type print karo.

'''a = "Deepanshu"
print(type(a))'''

#5--User se ek number string form me input lo (e.g., "45.67")
# aur usko float me convert karke square nikalo.
'''number = "4"
b = float(number)
square = b*b
print(f"Sqaure of this number :", square)'''

#6-- Ek string "True" ko boolean me convert karke print karo.
'''string = "Deepanshu"
y = bool(string)
print(y)'''
#--------------------------------------------------------------------------------

# --- lists , sets , tuples , dictionary
#1--Find the sum of all numbers in a list.
'''list=[1,2,3,4,5]
total = 0
for num in list:
    total = total + num
print(total)'''

#2-- method sum()
'''list=[2,3,4,5,6]
sum =sum(list)
print(sum)'''

#3-- Find the maximum and minimum element in a list.

# using condition and loop or built in function
'''max = max(list)
print(f"Maximum element is {max}")

min = min(list)
print(f"Minimum element is {min}")'''

#using loop
'''list = [12,3,4,5,6]
max_ = list[0]
for i in list:
    if max_<i:
        max_=i
print(max_)'''

#4-- Count how many times an element occurs in a list.(.count)
'''list = [2,3,4,5,6,2]
print(list.count(3))'''

#5--Calculate the sum of all odd numbers in the list.
'''list = [3,5,7,8,9]
total = 0
for num in list:
    if num%2!=0:
        total+=num
print("Summ of all odd numbers in the list is :", total)'''

#6-- Calculate the sum of all even numbers in a list
'''list = [3,5,7,8,9]
total = 0
for num in list:
    if num%2==0:
        total = total+num
print(total)'''

#7--- Reverse a list without using reverse method.
'''list = [3,5,7,8,9]
print(list[: :-1])'''

#8-- Merge two lists element-wise (like zip).
# Example: [1,2,3] & [‘a’,‘b’,‘c’] → [(1,'a'),(2,'b'),(3,'c')] 🔑 Hint: Use zip().
'''list =  [1,2,3]
list_2 = ['a','b','c']
list_merge=[list,list_2]
print(list_merge)'''

#9--Find second largest number in a list
'''numbers = [10, 25, 7, 35, 19]
second_largest = numbers[-2]
print(numbers.sort())

print(f"Second largest element in list is : {second_largest}")'''


