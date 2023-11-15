# https://www.w3schools.com/python/pandas/pandas_csv.asp
import pandas as pd

df = pd.read_csv('../datasets/worldcities.csv')
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
# print(df.to_string())

# print(df)

# Check your system's maximum rows with the pd.options.display.max_rows statement.
print(pd.options.display.max_rows)

# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999

print(df)
