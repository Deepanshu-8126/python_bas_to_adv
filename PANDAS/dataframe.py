# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# 2- dimensional labelled data structure (rows+columns)

# CREATING  DATAFRAMES
# from dictionary - most common
import pandas as pd
date= {
    "Name":['Deepanshu','Ankit','Himanshu'],
    "AGE":[18,19,19],
'Marks': [85, 90, 88]
     }
my_var=pd.DataFrame(date)
print(my_var)

# From list of lists
data = [
    ['Aman', 21, 85],
    ['Rohit', 22, 90],
    ['Priya', 20, 88]
]
# FROM DICTIONARY OF SERIES# columns labels
df = pd.DataFrame(data, columns=['Name', 'Age', 'Marks'])
print(df)
data = {
    'Name': pd.Series(['Aman', 'Rohit', 'Priya']),
    'Age': pd.Series([21, 22, 20])
}

df = pd.DataFrame(data)
print(df)

# 4-- FROM NUMPY ARRAY
import numpy as np

data = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(data, columns=['Col1','Col2','Col3'])
print(df)
