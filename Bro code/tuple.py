# Tuple -- ordered and unchangeable
# surrounded with rounded brackets
#name = ("Deepanshu", "Himanshu", "Vishal","Sandy", "Gaurav")
#print(name) # this will print tuple

#Tuple length find
#print(len(name))   #5

# Also tuple create using thistuple() constructor
'''thetuple=tuple(("Deepanshu", "Himanshu", "Vishal","Sandy", "Gaurav"))
print(thetuple)'''

# Acess tuple
'''print(name[0])
print(name[::-1]) #reverse
print(name[2:4]) # exclusice'''

# Check is items exists or not
'''if "Deepanshu" in name:
    print("Yes , Deepanshu in name tuplle as wwe created")
else:
    print("No")'''

# Update tuples - index changed karna padega hame lekin tuplees unchangeable hote  heey
#convert tup to list then update then again list-tup
'''y = list(name)
y[2]="GAURAV PANDEY"
name = list(y)
print(name)'''

#add items in tuple append
'''y = list(name)
y.append("KK")
name = list(y)
print(name)'''

# Remove Tuples
#Convert into list then .remove then
'''y= list(name)
y.remove("Himanshu")
name = list(y)
print(name)'''

#For loop
'''for i in name:
    print(i,end=" , ")'''
'''for i in range(len(name)):
  print(name[i])'''

#Count
'''name = ("Deepanshu", "Himanshu", "Vishal","Sandy", "Gaurav","Deepanshu")
print(name.count("Deepanshu"))'''







