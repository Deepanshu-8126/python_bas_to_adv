# Lambda function is a small anonyms function
# --- This is a short form of write function
# A small function for one time use
# They take mutiple number of arguments but only have one expression
# variable = lamba parameter : expression
# namespace clean useful

# use in high order function
#map(),sort(),reduce()
# Single argument
"""double_num=lambda x:x*2
print(double_num(2)
"""

# No Argument
# variable store
say_hello="Good Morning"
print(say_hello) # return good morning
# Double argument pass
add= lambda a,b:a+b
print(add(5,6)) #11

# minimum number find out
min_num=lambda x,y:x if x<y else y
print(min(3,4))

# max number
max_num=lambda x,y:x if x>y else y
print(max(4,3)) # x return

# add two string
full_name = lambda first,last:first+" "+last
print(full_name('Deepanshu',"kapri"))

# even and odd number check
num= lambda x: "Even " if x%2==0 else "Odd"
print(num(5)) # odd
