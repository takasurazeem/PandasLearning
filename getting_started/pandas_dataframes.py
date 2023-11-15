# https://www.w3schools.com/python/pandas/pandas_dataframes.asp
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)

# Locate row
print(df.loc[0])

# Return row 0 and 1: (Note: When using [], the result is a Pandas DataFrame.)
print(df.loc[[0, 1]])

df2 = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df2)

#Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).
print()
print(df2.loc["day2"])

cities = pd.read_csv('datasets/worldcities.csv')
print(cities)