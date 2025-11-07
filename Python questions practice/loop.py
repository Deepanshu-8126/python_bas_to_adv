# FOR loop questions--
"""n=int(input("Enter an number "))
result = 0
for i in range(1, n + 1):
    result = result + i
print(result)
"""

"""n=int(input('Enter number'))
total=0
i=1
while i<=n:
    total=total+i
    i=i+1
print(total)
"""
# question - print square from 1 to 20
"""n=20
i=1
while i<=n:
    square = i**2
    print(f"Sqaure of {i} is ", square)
    i+=1
"""
# using for loop
"""n=int(input("Enter any number "))
for i in range(1,n+1 ):
    square=i**2
    print(f" square of {i} is  ",square)"""

# print sum of first 10 natural numbers
# both for loop and while loop
"""num=10
total=0
for i in range(1,num+1):
    total+=i
print(total) # 55
"""
"""
num=10
total=0
while num==10:
    total+=num
print(total)
"""

# Print only odd numbers from 1 to 50
"""for i in range(1,51):
    if i%2!=0:
        print(i,end=" ")

# Print only even numbers from 1 to  50
for i in range(1,51):
    if i%2==0:
        print(i,end="")
"""

# Print table of 5 using loops
"""num=5
i=1
while i<=10:
  print(f"{num}*{i}={num*i}")
  i+=1"""

# using for loop
"""num = int(input("Enter number "))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")
    
"""

"""n = int(input("Enter number"))
table=lambda x:list(map(lambda i:f"{x}*{i}={x*i}",range(1,11)))
print("\n".join(table(n)))"""


