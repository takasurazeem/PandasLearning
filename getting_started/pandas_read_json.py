# https://www.w3schools.com/python/pandas/pandas_json.asp
import pandas as pd

df = pd.read_json('../datasets/cities.json')

print(df)
