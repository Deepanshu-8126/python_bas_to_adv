import pandas as pd
df = pd.read_csv("data.csv.txt")
# selection
print(df["Name"].to_string())
print(df["Height"].to_string())
print(df["Type1"].to_string())
print(df["Legendary"].to_string())

