# DECORATOR-Decorator ek function hai jo dusre function ko modify karta hai.
#Yeh hi decorator ka power hai:
# Original function ka code badle bina, uske upar extra feature jod dete hain.

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
Real-life samajh:

Without decorator: Direct bank account khul jata (unsafe).

With decorator: Pehle login check hota hai, fir account open hota hai."""

# practice question
# Discount Decorator
"""def discount_decorator(func):
    def wrapper(amount):
        # Discount logic
        if amount > 1000:
            discount_rate = 0.10   # 10%
        elif amount > 500:
            discount_rate = 0.05   # 5%
        else:
            discount_rate = 0.0    # No discount

        # Final amount after discount
        final_amount = amount - (amount * discount_rate)

        print(f"Original Bill: ₹{amount}")
        print(f"Discount Applied: {discount_rate*100}%")
        print(f"Final Bill After Discount: ₹{final_amount}")

        # Call the original function with final amount
        return func(final_amount)
    return wrapper


# Checkout function
@discount_decorator
def checkout(amount):
    print(f"✅ Payment of ₹{amount} done successfully!\n")


# ---- Usage ----
checkout(1200)   # 10% discount
checkout(700)    # 5% discount
checkout(400)    # no discount
"""

# Q1: Greeting Decorator
#
# Task: Ek function greet(name) banao jo "Hello, name" print kare.
#
# Decorator: Agar name "Admin" ho, toh greeting me "Welcome Admin!" add karo.
#
# Hint: Use ek wrapper function + if condition.