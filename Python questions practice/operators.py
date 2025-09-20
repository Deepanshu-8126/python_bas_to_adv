# Question:
# Write a program that checks whether a
# number is divisible by both 3 and 5 using logical operators.

"""num = int(input("Enter a number "))
if num%3==0 and num%5==0:
    print("Yes number is divisible by both 3 and 5")
else:
    print("Number is  not divisble by both number")"""

# #Question:
# Swap two numbers without using a third variable (only operators).

'''a= int(input("Enter a"))
b=int(input("Enter b"))
a = a+b
b = a-b
a = a-b
print("A",a)
print("B",b)'''
# Question:
# Take a 3-digit number from user, print the sum of its digits using operators.
'''num = int(input("Enter number "))
sum_digits=0
while num>0:
    digits = num%10
    sum_digits+=digits
    num = num//10

print("sum of digits is :", sum_digits)'''

#🔹 Shortcut Approach (3-digit ke liye only)
# Example: num = 123
# Last digit → d1 = num % 10 → 123 % 10 = 3
# Middle digit → d2 = (num // 10) % 10 → (123 // 10) % 10 = 12 % 10 = 2
# First digit → d3 = num // 100 → 123 // 100 = 1
# Ab sum kar do → d1 + d2 + d3 = 3 + 2 + 1 = 6

'''num = 145
d1 = num%10
d2= (num//10)%10
d3= num//100
sum = d1+d2+d3
print(f"sum of digits is : {sum}")'''
 #6--Question:
# Check whether a given year is a leap year or not using operators.
'''year =int(input("Enter year"))
if year%4==0:  #year%400==0 year%100!=0
    print("Year is leap year")
else:
    print("Not leap year")'''

'''num=1234
d1=(num%10) #last digit
d2=(num%100)//10
d3=(num%1000)//100
d4=(num%10000)//1000
sum_digits = d1+d2+d3+d4
print(sum_digits)'''

# Question -- aa student is pass or not
'''marks = 65
attendence = 80
if marks>=40 and attendence>=75:
    print("Student pass")
else:
    print("Student fail")'''
# Question --4 salary
'''salary = 20000
performance = "good"
if performance=="good":
    salary += salary *0.10 # add then multiply
else:
    salary += salary *0.05
print("Final Salary", salary)'''

#5-- Password strength checker
'''password = input("Enter password")
if len(password)>=8 and any(char.isdigit() for char in  password):
    print("Strong password")
else:
    print("Weak password")'''

# Electricity bill calculator
'''units = int(input("Enter units"))
bill =0
if units<=100: # agar unit 100 sey kam hey ya equal hey  into 5 kardo
    bill = units*5
elif units<=200:
    bill = units*8
else:
    bill=units*10
print("Total Bill", bill)'''

#atm pin checker
# give user 3 chances pin dalne ka
#for loop
'''correct_pin =1234
pin=[1111,1323,4332]
attempts=0
for attempt in pin:
    attempt+=1
    if attempt == correct_pin:
        print("Access Granted")
    else:
        print("Acess Denied")'''
# basic version
'''correct_pin = 1234
pin = int(input("Enter pin"))
if pin==correct_pin:
    print("Acess granted")
else:
    print("Acess Denied")'''
# multi attempt
'''correct_pin = 1234
attempts = 0
pin = int(input("Enter again pin"))
while attempts <2:
    pin = int(input("Enter again pin"))
    attempts+=1
    if pin == correct_pin:
        print("Acess granted")
        break
    else:
        print("Wrong Pin")
        if attempts==3:
            print("Acess Denied")'''

# Armstrong number
'''num = 153
d1= num//100  #first digit
d2= (num//10)%10 #second digit
d3= num%10 #last digit

result = d1**3+d2**3+d3**3
if result==num:
    print("Armstrong number")
else:
    print("Not armstrong number")'''



