# LENGTH FUNCTION
# name.find -- for finding
""""
name = input("Enter name :")
# result = name.find(" ")# in which position space
# result = name.find("a") # deepanshu a in 4th position
reverse_num = name.rfind("a") # deepanshua ast one index will give
print(reverse_num)"""

'''name = input("Enter name")
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())'''

# doubt ki int mey run nahi ho raha hey runn
'''phone = input("Enter phone number ?")
# result = phone.count("-")

phone =  phone.replace("-"," ")
print(phone)'''

# Exercisee
#validate username
# user is no more than 12 characters
# user  must not contain spaces
# username must not contain digits

'''username = input("Enter username ")
if len(username) > 12:
    print("Your username is can't be 12 characters")
elif not username.find(" ") ==-1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digits")
else:
    print(f"Your username is {username}")'''

    # another method
'''username = input("Enter username ")

    if len(username) > 12:
        print("Your username can't be more than 12 characters")
    elif " " in username:
        print("Your username can't contain spaces")
    elif not username.isalpha():
        print("Your username must contain only letters")
    else:
        print(f"Your username is {username}")'''

#INDEXING in string
credit_number = "1234,56,789,1234"
#print(credit_number[0]) # at 0 index  it will print 1
#print(credit_number[0:4] )# exclusive so 1234 print comma will not print
# as default indexing
#print(credit_number[:15]) # all print from starign python see  as default

'''print(credit_number[3:9])
print([credit_number[-1]]) #reverse number print

print([credit_number][::2]) #start to end print with step of 2'''

'''last_digit= credit_number[-4:]
print(f"xxxx,xxxx,xxxx,{last_digit}")'''

# print reverse credit number
'''credit_number[::-1]
print(credit_number) #4321'''


