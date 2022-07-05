name=input('あなたの名前>>')
print('{}さん、こんにちは'.format(name))
food=input('{}さんの好きな食べ物>>'.format(name))

if 'カレー' in food:
    print('素敵です。カレーは最高ですよね‼')
else:
    print('私も{}が好きですよ'.format(food))
