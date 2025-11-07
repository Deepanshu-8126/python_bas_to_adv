# DECORATOR-Decorator ek function hai jo dusre function ko modify karta hai.
#Yeh hi decorator ka power hai:
# Original function ka code badle bina, uske upar extra feature jod dete hain.

# This is normal return  function
"""def add(a,b):
    return a+b
result=add(2,3)
print(result)
"""


# Decorator example
"""def my_decorator(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper()  # through decorator original function ko wrapping mil gayi
@my_decorator
def greet():
    print("Hello Deepanshu")"""


#login check
"""def login_required(func):  # decorator
        def wrapper():
            print("🔑 Checking login credentials...")
            func()  # agar credentials sahi hai toh original function chalega
            print("✅ Login success! Session closed.")

        return wrapper
@login_required  #decorator func hey access_account input me lega
def access_account():
    print("Accessing your bank account...")
access_account()"""
"""


# Q1: Greeting Decorator
#
# Task: Ek function greet(name) banao jo "Hello, name" print kare.
#
# Decorator: Agar name "Admin" ho, toh greeting me "Welcome Admin!" add karo.
#
# Hint: Use ek wrapper function + if condition."""



"""def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Start operation")
        result=func(*args,**kwargs)
        return result
    return wrapper
@my_decorator
def add(a,b):
    return a+b
print(add(4,5))"""