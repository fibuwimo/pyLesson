try:
    price=int(input('料金を入力>>'))
    number=int(input('人数を入力>>'))
    print('一人あたり{}円です'.format(price/number))
except ValueError:
    print('料金ないし人数には整数を入力してください')
print('おわり')
