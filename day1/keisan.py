a=10
b=5

answer=a+b
print(a,'+',b,'=',answer)
answer=a-b
print(a,'-',b,'=',answer)
answer=a*b
print(a,'*',b,'=',answer)
answer=a/b
print(a,'/',b,'=',answer)

"""str='Hello'*5
print(str)"""

x=10
if x>0:
    print('正')

else:
    print('正じゃない')
print('test')

n=0
while n<10:
    print(n)
    n=n+1
print('終了')

for i in range(5):
    print(i)

for i in range(1,11):
    print(i,end=' ')
print()

for i in range(1,4):
    for j in range(1,11):
        print(i*j,end=' ')
    print()

import random

num= random.randint(5,10)
print(num)

a='tim'
x=10
print(type(x))
print(type(type(x)))
y=type(a)(x)
print(type(y))
print(type('hello') is str)
print(isinstance(x,int))

name='わし'
age=53
height=165.4567
print(f'わたしの名前は{name}、年齢は{age}、身長は{height:.1f}cmです')

print(0**0)
print(3**(-2))

h=float(input('身長(cm)>>'))/100
w=float(input('体重(kg)>>'))
b=w/(h**2)
print(f'あなたのBMIは{b:.2f}です')
