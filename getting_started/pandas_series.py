# https://www.w3schools.com/python/pandas/pandas_getting_started.asp

import pandas as pd

x = [1, 7, 2]

series = pd.Series(x)

print(series)

# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
#
# This label can be used to access a specified value.


# Return the first value of the Series:
print(series[0])

# Create Labels
# With the index argument, you can name your own labels.
#
# Example
# Create your own labels:
series_with_label = pd.Series(x, index=["x", "y", "z"])
print(series_with_label)

# Return the value of "y":
#
print(series_with_label["y"])