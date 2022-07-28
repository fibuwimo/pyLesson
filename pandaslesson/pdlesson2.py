import pandas as pd
df=pd.read_csv('test.csv')

data_s=df[df['国語']>=90]
print(data_s)

data_s=df[(df['国語']>=90) & (df['数学']>=80)]
print(data_s)

df.loc[0,'数学']=89

print('最高',df['数学'].max())
print('最低',df['数学'].min())
print('平均',df['数学'].mean())
print('中央',df['数学'].median())
print('最頻',df['数学'].mode())
print('合計',df['数学'].sum())

math_df=df.sort_values('数学')
print(math_df)
kokugo_df=df.sort_values('国語',ascending=False)
print(kokugo_df)

df_T=df.T
print(df_T)

li=df.values
print(li)

kokugo_df.to_csv("export1.csv")

kokugo_df.to_csv("export2.csv",index=False)

kokugo_df.to_csv("export3.csv",index=False,header=False)
