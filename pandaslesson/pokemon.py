import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('pokemon_status.csv',encoding='shift-jis')
result1=df[df['すばやさ']>=102]
print(result1[['ポケモン名','すばやさ']])

result2=df[(df['タイプ１']=='ほのお')&(df['タイプ２']=='ひこう') | (df['タイプ１']=='ひこう')&(df['タイプ２']=='ほのお') ]
print(result2[['ポケモン名','タイプ１','タイプ２']])
