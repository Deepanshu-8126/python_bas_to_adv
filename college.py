# Print any  number of table using while loop and for loop
# '''num = 2
# i = 1
# while i <= 10:
#     print(f"{num} * {i} = {num * i}")
#     i += 1'''

#
# num = int(input("Enter any number :"))
# i = 1
# while i<=10:
#     print(f"{num}*{i}={num*i}")
#     i+=1


# Factorial number
'''def factorial(num):
    fact = 1
    i = 1
    while i <= num:
        fact = fact * i
        i += 1
    return fact

print(factorial(5))'''

'''num = int(input("Enter any number for factorial :"))
fact= 1
for i in range(1,num+1):
    fact = fact*i
    print(fact)'''

def fact(num):
     for i in range(1,num+1):
     fact = fact*i
       return fact


print(fact(5))