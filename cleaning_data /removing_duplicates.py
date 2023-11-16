# https://www.w3schools.com/python/pandas/pandas_cleaning_duplicates.asp
import pandas as pd

df = pd.read_csv('../datasets/data.csv')
# print(df.head(15).duplicated())
# remove duplicates
df.drop_duplicates(inplace=True)

print(df.to_string())