# while -- jab tak condition true nahi ho jati loop chalte rahega

"""name = input("ENter name :")
if name=="":
    print("You  didnt enter your name")
else:
    print(f"Hello {name}")"""


# continusoly puchega jab tak nam nahi de dete enter your name

'''name =input("Enter your name ")
while name =="":
    print("you did not enter your name ")
    name = input("Enter your name ")

print(f"hello{name}") # agar name dal diya loop false bhar aa jayega or yey print ho jayega'''

'''age = int(input('Enter your age'))
while age>=18:
    print("You are eligible to vote")
    age= int(input("Enter again "))  # otherwise infinite loop begins
print("You are not eligible to vote")'''

# Exercise food # dobut double equals too
'''food = input("Enter food you like (q to  quit) ")
while not food=="q": # jab tak ham q nahi while not tab tak puchte rahega
    print(f"You like {food}") #agar eske bad food inpout nahidiya next konsa food pasan hhehy infinte loop chalega
    food = input("Enter another food you like ")

print("You quit this game")'''

#Its workingggggg

# Make a program loop chalate raho tab tak
num = int(input("Enter a number between 1-10 "))
while num<1 or num>10: # num 1 sey chota and 10 sey bada thoo not valid
    print("Number is not valid")
    num = int(input("Enter a number between 1-10"))

print(f"Your number is {num}")
# 3 true -1 not valid