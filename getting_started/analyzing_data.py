# https://www.w3schools.com/python/pandas/pandas_analyzing.asp
import pandas as pd

# Get a quick overview by printing the first 10 rows of the DataFrame:
df = pd.read_csv('../datasets/cities_population.csv')
# print(df.head(10)) # Note: if the number of rows is not specified, the head() method will return the top 5 rows.
# print(df.head())

# The tail() method returns the headers and a specified number of rows, starting from the bottom.
# print(df.tail())

# Print information about the data:
print(df.info())
