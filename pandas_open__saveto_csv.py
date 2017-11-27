# Youtube tutorial https://www.youtube.com/watch?v=-0NwrcZOKhQ
# Github files https://github.com/codebasics/py/blob/master/pandas/4_read_write_to_excel

import pandas as pd

# to read and write to a csv
df = pd.read_csv("sample_data.csv")
# if you had a file that had no column names, you can add them
# df = pd.read_csv("sample_data.csv", header=None, names=["ticker", "eps", "revenue", "price", "people"]

print(df)

df.to_csv('new.csv', index=False)


