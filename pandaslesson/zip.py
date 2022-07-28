import pandas as pd
df = pd.read_csv('13TOKYO.CSV',header=None,encoding="shift_jis")

print(len(df))
print(df.columns.values)

results=df[df[2] == 1660014]
print(results[[2,6,7,8]])

results=df[df[8].str.contains('四谷')]
print(results[[2,6,7,8]])

results=df[df[8]==('四谷')]
print(results[[2,6,7,8]])
