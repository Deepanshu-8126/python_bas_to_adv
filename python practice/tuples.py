# Tuples -- immuutable
# Tuples are used to store multiple items in a single variable
#Store collection of data lists set dictionary faster tuple comparisonn to lists

# CREATE A TUPLE
"""this_tuple=("apple","banana","cheerry")
print(this_tuple) # print all the elements in tuple

#TUPLE LENGTH
print(f"Length of this tuple is : {len(this_tuple)}") #3
"""

'''tuple = (1,"deepanshu", "himmashu")
# Acessing
print(tuple[0])
# Negative indexing
print(tuple[-1]) # himmashu'''

# We can also give range where we want to print
'''tuple = ("spd","power rangers", "Bro code", "Code with harry")
# WE can give range slicing
print(tuple[:-1])'''

'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# apple banana  cherry orange
print(thistuple[-1:])'''

# Check if item exists or not using in keyword
'''tuple = ("dk","nc","rb","kk","km")
if "nc" in tuple:
    print("yes nc in tuple")'''

# Update tuples
#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

#But there are some workarounds
# TUPLE -- LISTS -- LISTS -- TUPLE

"""
tuple_0=("Deeepanshu","AMIT","HImanshu")
#convert into list
y = list(tuple_0)
print(y) # ['deepanshu,'amit',himashu'] behave like a list
#update list and convert to tuple
y[0]="Vishal"  # vishal updated as name of deepanshu
x= tuple(y)  # here , we covert list into a tuple and store in a x variable beahve a tuple
print(x)"""


# ADD ITEMS (same process as update 'append)
"""
this_tuple=("Deeepanshu","AMIT","HImanshu")
y=list(this_tuple)
y.append("Vishal")
x=tuple(y)
print(x)

"""
#ADD TUPLE TO TUPLE
"""
this_tuple=("Deepanshu","Vishal","Himanshu")
y=("GAURAV",) #comma is imp python is not idfentified as tuple
this_tuple+=y
print(this_tuple)
"""

#REMOVE ITEMS IN A TUPLE
#TUPLES ARE UNCHANGEABLE convert to list remove then list to tuple

# ------------- UNPACK TUPLES -----
# PACKING TUPLES -- when we create a tuple , we noramlly assing values to it . This is called packing a tuple
"""
thistuple=("Deepanshu","Vishal","Himanshu")

# But in python extract values back into variables this is called unpacking

fruits = ('apple','banana','cheery')
(green,yellow,red)=fruits
print(green) # return apple
print(yellow)
print(red) #note number of variables match no of values in tuple

#USING ASTRIK(*)
#assign the rest of the values as a list ]
fruits=('a','b','c','d','e','f')
(green,red,happy,*red)=fruits
#red return rest of the values in tuple
print(green)
print(*red) #d e f return
"""
# LOOP IN TUPLES

"""
thistuple=("Deepanshu","Vishal","Himanshu")
for i in range(len(thistuple)):
    print(thistuple[i])
#while loop
thistuple=("Deepanshu","Vishal","Himanshu")
i=0
while len(thistuple):
     print(thistuple[i])
     i=i+1

"""