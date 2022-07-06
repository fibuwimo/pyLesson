userinfo=input('名前,血液型>>')
[name,blood]=userinfo.split(',')
blood = blood.upper().strip()
print(f'{name}さんは{blood}型なので大吉です')

result='banana'.replace('a','o')
print(result)

aCount='banana'.count('a')
print(aCount)

def add(x,y):
    return x+y

print(type(add))
newadd=add
print(newadd(4,5))
