# https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
import pandas as pd

df = pd.read_csv('../datasets/data.csv')

# cleaned_df = df.dropna()
#
# print(cleaned_df.to_string())

# to change the original DataFrame, use the inplace = True argument:

# df.dropna(inplace=True)

# Replace NULL values with the number 130:
# df.fillna(130, inplace=True)

# Replace NULL values in the "Calories" columns with the number 130:
# df["Calories"].fillna(130, inplace=True)

# Replace Using Mean, Median, or Mode
# mean = df["Calories"].mean()
# df["Calories"].fillna(mean, inplace=True)

# median = df["Calories"].median()
# df["Calories"].fillna(median, inplace=True)

# mode = the value that appears most frequently.
mode = df["Calories"].mode()[0]
df["Calories"].fillna(mode, inplace=True)

print(df.to_string())
