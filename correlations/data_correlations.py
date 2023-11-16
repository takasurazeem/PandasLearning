# https://www.w3schools.com/python/pandas/pandas_correlations.asp
import pandas as pd

df = pd.read_csv('../datasets/data.csv')
print(df.corr())
