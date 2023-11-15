# https://www.w3schools.com/python/pandas/pandas_getting_started.asp

import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

df = pd.DataFrame(mydataset)

print(df)

print(pd.__version__)
