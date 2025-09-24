import pandas as pd
df = pd.read_csv("data.csv.txt")
print(df) # this data is truncated
# means first five rows and last five rows
# for entire data frame
print(df.to_string()) # entire data

