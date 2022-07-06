scores1=[80,40,50]
scores2=[80,40,50]
scores3=scores1

print(f'1idは{id(scores1)}')
print(f'2idは{id(scores2)}')

if scores1==scores2:
    print('等価である（同じ内容）')
else:
    print('等価でない（違う内容）')
if id(scores1)==id(scores2):
    print('等値である（同じ存在）')
else:
    print('等値でない（違う存在）')
if id(scores1)==id(scores3):
    print('等値である（同じ存在）')
else:
    print('等値でない（違う存在）')

names=list()
print(f'前:{id(names)}')
names.append('松田')
print(f'後:{id(names)}')

name='松田'
print(f'前:{id(name)}')
name=name+'さん'
print(f'前:{id(name)}')

