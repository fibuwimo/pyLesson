import pandas as pd

df=pd.read_csv("test.csv")
print(df)

print('件数',len(df))
print('項目名',df.columns.values)
print('index',df.index.values)

print('行index',df.loc[2])

print('行index',df.loc[[3,4]])

print('value',df.loc[2]['国語'])

print('列名',df['国語'])

print('列名',df[['国語','理科']])

df.loc[6]=['G恵',90,92,94,96,92]
print(df)

df['美術']=[68,73,82,77,94,96,98]
print(df)

df.loc[0,'国語']=85
print(df)
df.loc[0]=['A太',82,90,76,97,76,70]
print(df)
df['美術']=[69,74,83,78,95,97,99]
print(df)


