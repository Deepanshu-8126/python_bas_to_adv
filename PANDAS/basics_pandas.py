# PANDAS -- PANDAS IS A PYTHON LIBRARY
#PANDAS USES IN Data analysis , data science , machine learning

# way of making series
# import pandas as pd
# series = pd.Series([1,2,3,4,5])
# print(series)

# series is a one dimensional ( a data of a single column)
#CREATE LABELS
# CUSTOM INDEX
# WITH  THE INDEX ARGUMENT we can own labels
"""
s= pd.Series([10,20,30],index=["a","b","c"])
print(s)

# lables as a index a bc 10 20 30

# ACESS  AN ITEM
print(s["b"]) # acess value using labels
print(s["c"])
print(f"VALUE OF A IS ",s["a"])

# ACESS THE VALUE BY LOC
print(s.loc["a"]) #using lock location by label = 10
print(s.loc["b"]) #20
print(s.loc["c"]) #30
"""
# FILTER BY VALUE
# WHO  HAS MORE THAN 200 VALUE

"""data =[100,102,104,200,202]
series=pd.Series(data,index=["a","b","c","d","e"])
print(series[series>=200]) # 200 sey jyada and less
print(series[series<200]) # less than 200 filter
"""

# key / value object as series dicitonary
# we can also use key/value object, like a dictionary when creating a series
"""
import pandas as pd
calories={"day":420,"day2":380,"day3":390}
my_var=pd.Series(calories) # pass dicitionary
print(my_var)  

# we dont want to pass an index
# key or labels
# ACESSS USING THE LOC PROPERTY TO SEE how many calories i have eaten on a certain day
print(my_var.loc["day2"])  # my_var ubder series
# result 380

#UPDATE DAY 3
my_var.loc["day3"]+=500     # using label update thhe value  by key or wee can say label 
print(my_var)       # 390 to 890

# FILTER VALUES
print("Value greater than 200  ",my_var[my_var>200])
# this will filter
# another variable store that filter out data from dictionary who has bigger values 200
series=my_var[my_var>200]
print(series)      """


# make a series using scalar single vaue
"""import pandas as pd
s = pd.Series(5, index=['x','y','z'])
print(s)       """

# series attributes
"""import pandas as pd
series=pd.Series([1,2,3,4,5,6])
print(series.shape) #6,
print(series.index)
print(series.dtype)
print(series.size) #total elements --6                   """

#-----------------------------------------------------------------------------------
#--------------------------PRACTICE QUESTIONS--------------------------------------
#🔹 Question 1: Create a Series
# [10, 20, 30, 40, 50] values se ek Series banao.
# Default index use ho
""""
import pandas as pd
series=pd.Series([10,20,30,40,50])
print(series)

# 🔹 Question 2: Custom Index
#
# Ek Series banao values [100, 200, 300] ke saath aur index ['a','b','c'].

series=pd.Series([100,200,300],index=('a','b','c'))
print(series)

# Question 3: Dictionary to Series
#
# Dictionary se ek Series banao:
fruits = {'apple': 50, 'banana': 30, 'mango': 20}
my_var=pd.Series(fruits) # fruits pass in series my variable
print(my_var)

# sclaar question all value 5 and index
series=pd.Series(5,index=['x','y','z'])
print(series)
"""
