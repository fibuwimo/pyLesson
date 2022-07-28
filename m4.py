import pandas as pd

title=input('csvファイル>>')
df = pd.read_csv(title)
words=df.iloc[:,3]

print(len(words))

count=0;
word=input('調べたい単語>>')
for w in words:
    if (word in w):
        count +=1

print(title,'の本文中に',word,'は',count,'回')
