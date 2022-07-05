members=["あ","い","う","え"]
print(members)
print(members[0])

scores=[89,90,95]
total=sum(scores)
print(f'合計{total}')

ave=sum(scores)/len(scores)
print(f'平均{ave}')

members.append('お')
members.append('か')
members.append('き')
print(members)
members.remove('か')
del members[5]
print(members)

members[0]='ん'
print(members)

a=[10,20,30,40,50]
b=a[1:3]
print(b)
c=a[2:]
print(c)
d=a[:3]
print(d)
e=a[:]
print(e)

f=a[-2:]
print(f)
g=a[4:0:-1]
print(g)
