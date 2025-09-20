# DICTIONARY -- A DICTIONARY IS A CHANGEABLE UNORDERED COLLECTION OF UNIQUE KEY VALUE PAIRS
# THIS IS FAST BECAUSE OF HASHING , ALLOW US TO ACESS A VALUE QUICKLY
"""
capitals={"usa":'Washington',
          "india":'new delhi'}
# using key acess the value
print(capitals["usa"]) # open brackets use
print(capitals["india"]) #new delhi
print(capitals) #it will print whole dicitionary

# Length
print(len(capitals)) #2
"""
# data types any of data
"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["year"]) #1964

# dict() constructor # make dicitonary
thisdict=dict(name="Deepanshu",age=19,rollNo=4)
print(thisdict)

# RETURN KEYS
print(thisdict.keys())"""
"""
# Print both key and values
print(capitals.items()) # print both key and value

# RETURN ONLY VALUES
print(thisdict.values())


# Update / add key -value
capitals.update({"Germany":"Berlin"})
print(capitals["Germany"])
print(capitals)
"""
# another metho (ADD METHOD)
"""capitals["Nepal"]="KATHMANDU"
print(capitals["Nepal"])
"""


"""
# another way loop
capitals={"usa":'Washington',
          "india":'new delhi'}
for key,value in capitals.items():
    print(key,value) # print values

# values method
for x in capitals.values():
  print(x)

# keys return
for x in capitals.keys():
    print(x)
    
    """
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change"""

"""
# check if key exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("YES model in this dictionary")


# CHANGE VALUES
thisdict["year"]=2020
print(thisdict["year"]) #2020 change

# in update both key value
thisdict.update({"year": 2020})


# ADD METHODS
thisdict["color"]="red"
print(thisdict.items()) # color :red addded

# Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


# REMOVE ITEMS pop
thisdict.pop("year")
print(thisdict) # removed

# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)"""

# copy dictionary
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict=thisdict.copy()
print("my dicitionary is :",mydict)"""


# NESTED DICTIOANRY
# create a dictionary that contains three dicitonnaries
# note comma after assigning all the dictionary

"""
myfamily = {
  "child1" : {
    "name" : "Deepanshu",
    "year" : 2007
  },
  "child2" : {
    "name" : "Chetan",
    "year" : 2007
  },
  "child3" : {
    "name" : "Priyanshu",
    "year" : 2008
  }
}

print(myfamily)

# create one dictionary that contain all three dictionary
child1 = {
  "name" : "Deepanshu",
  "year" : 2007
}
child2 = {
  "name" : "Chetan",
  "year" : 2007
}
child3 = {
  "name" : "Priyanshu",
  "year" : 2009
}
myfamily={"child1":child1,
          "child2":child2,
          "child3":child3 }

# acess items in  nested dictionary
print(myfamily["child2"]["name"]) #chetan

print(myfamily.items()) # all items
print(myfamily.keys()) #child1 child2 child3
print(myfamily.values()) # all values

# loop in nested dictionary
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
    
"""