# https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp
import pandas as pd

# Pandas has a to_datetime() method for fixing wrong date format:
df = pd.read_csv('../datasets/data.csv')
df['Date'] = pd.to_datetime(df['Date'])
# This failed to fix the wrong date format, and thus I didn't bother
# fixing the recurring error. It was because of some date format.
df.dropna(subset=['Date'], inplace=True)
print(df.to_string())

# The date in row 1 was fixed,
# but the empty date cells got a NaT (Not a Time) value, in
# other words an empty value. One way to deal with empty values
# is simply removing the entire row or fill with some data.
