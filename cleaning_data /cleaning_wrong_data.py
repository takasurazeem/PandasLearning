import pandas as pd

df = pd.read_csv('../datasets/data.csv')
# Update a single record
df.loc[7, "Duration"] = 45

# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:

# for index in df.index:
#     if df.loc[index, "Duration"] > 120:
#         df.loc[index, "Duration"] = 120

# Delete rows where "Duration" is higher than 120:
for index in df.index:
    if df.loc[index, "Duration"] > 120:
        df.drop(index, inplace=True)

print(df.to_string())
