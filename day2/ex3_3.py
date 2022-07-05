num =int(input('数値>>'))
if num %2==0:
    print('偶数')
else:
    print('奇数')

div='偶数' if num %2 ==0 else '奇数'
print(div)
result='優'if num >=80 else '良' if num >=60 else '可' if num >=40 else '不可'
print(result)
