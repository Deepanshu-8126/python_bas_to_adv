import pandas as pd

data = {
    "Name": ["Deepanshu", "Vishal", "Himanshu", "Guarav", "Sandy"],
    "Age": [18, 21, 19, 22, 20],
    "Maths": [85, 90, 78, 60, 95],
    "Science": [88, 92, 80, 70, 98]
}

df = pd.DataFrame(data)
print(df)


# operations perform on dataframe
# FILTERING - select row based on condition
# Pehla df → Jisme se data lena hai. 2 df
# Matlab → pura DataFrame (Excel sheet jaisa).
# # Second df["Maths"] > 80 → ye ek condition hai jo True/False values return karti hai for each row.
# df[ condition ] → Matlab sirf un rows ko select karo jaha condition True hai.
"""high_math = df[df["Maths"]>80]
print(high_math)
low_math = df[df["Maths"]<80]
print(low_math) # dataframe ke andar maths mey 80 sey kam unki details

"""
# mutiple conditions
# in maths marks are greater than 80 and age is less than 21
"""s = df[(df["Maths"] > 80) & (df["Age"] < 21)]
print(s)
#-------------------------------------------------------------------------------------------------------
# science mey marks 80 sey greater and age less than 21
d = df[(df['Science']>80) & (df["Age"]<21)]
print(d)

# maths and science who has less than 50 marks and age less than 21
e = df[(df["Maths"]<80)& (df["Science"]<80) & (df["Age"]>21)]
print(e)

# or
science_or_age = df[(df["Science"] > 90) | (df["Age"] > 21)]
print(science_or_age)
"""
# total added to a new colummn create a new colummn

df["Total"]=df["Maths"]+df["Science"]
print(df)
# result in a new series row wise add

# modify column
df["Grade"] = ["A" if x >= 170 else "B" if x >= 150 else "C" for x in df["Total"]]
print(df)


df["Percentage"]=df["Total"]/2
print(df)
# filter who has less than  80 percentage
less_percentage=df[df["Percentage"]<80]
print(less_percentage) # himanshu and gaurav has less than 80 percentage


# PASS / FAIL STATUS
df["Result"] = ["Pass" if x >= 80 else "Fail" for x in df["Total"]]

#DELETE COLUMMN
df=df.drop("Age",axis=1)
print(df) # age column is deleted

# DELETE ROW
df=df.drop(4,axis=0) # by giving index number
print(df) # 4 row deleted

