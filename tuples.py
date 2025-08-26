# Tuples -- immuutable
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

#But there are some workarounds.
# convert it into list
tuple = ("dk","nc","rb","kk","km")
y = list(tuple)
y[1]="Deepanshu"
y.append("Deepanshu")
tuple =y
print(tuple)