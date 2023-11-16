# https://www.w3schools.com/python/pandas/pandas_plotting.asp
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../datasets/data.csv')

# df.plot()
# plt.show()

# Scatter Plot
# df.plot(kind='scatter', x='Duration', y='Calories')
# plt.show()

# A scatterplot where there are no relationship between the columns:
# df.plot(kind='scatter', x='Duration', y='Maxpulse')
# plt.show()

# Histogram
df["Duration"].plot(kind='hist')
plt.show()