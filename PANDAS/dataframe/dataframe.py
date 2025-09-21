# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# 2- dimensional labelled data structure (rows+columns)

# CREATING  DATAFRAMES
# from dictionary - most common
"""
import pandas as pd
date= {
    "Name":['Deepanshu','Ankit','Himanshu'],
    "AGE":[18,19,19],
'Marks': [85, 90, 88]
     }
# my_var=pd.DataFrame(date)

my=pd.DataFrame(date,index=['name','age','roll_no'])

# print(my_var) # normal

# print(my) # index

# ---------------------ACESS--------------------
# using index access
print(my.loc["name"])

# using integer locatipon
print(my.iloc[0])
print(my.iloc[1]) #ankit 19 90

# adding a column
# my["job"]=['cook','n/a','cashier']
# print(my)

# adding a new row
new_row = pd.DataFrame([{"Name": "Sandy", "AGE": 18, "Marks": 92}], index=["Employee"])
my = pd.concat([my, new_row])
print(my)
"""
# call the concatenata function also append

# From list of lists
"""
data = [
    ['Aman', 21, 85],
    ['Rohit', 22, 90],
    ['Priya', 20, 88]
]
# FROM DICTIONARY OF SERIES# columns labels
df = pd.DataFrame(data, columns=['Name', 'Age', 'Marks'])
print(df)

"""


"""data = {

    'Name': pd.Series(['Aman', 'Rohit', 'Priya']),
    'Age': pd.Series([21, 22, 20])
}

df = pd.DataFrame(data)
print(df)
"""
# 4-- FROM NUMPY ARRAY
"""import numpy as np

data = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(data, columns=['Col1','Col2','Col3'])
print(df)
"""

"""import pandas as pd

student_details={"Name":
                 ['Deepanshu','ankit'],
                 "Rollno": [21,22],
                 }
my_var=pd.DataFrame(student_details)
print(my_var)
"""

# creating from list to lists
""""
import pandas as pd
data =[
      ["deepanshu",18,4],
      ["chetan",18,7],
      ["priyanshu",16,8]
]
my_var=pd.DataFrame(data,columns=["Name","Age","Rollno"])
print(my_var)
print(my_var.loc[2]) # return row 2
print(my_var.loc[0,1]) # retunr row 1 to 2

"""


#------------------------------------------------------------------------------------------
"""
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
# day 1 day 2 day 3 are index 0 1 2
#refer to the named index:
print(df.loc["day2"])

"""

# creating dataframe from csv file

#-------------------Questions----------------------------------------------------------