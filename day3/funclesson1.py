def hello():
    print('こんにちは')

hello()


def plus(x,y):
    answer=x+y
    return answer

answer=plus(100,50)
print(f'足し算の答えは{answer}です')

def plus_and_minus(a,b):
    return a+b,a-b

next,prev =plus_and_minus(1978,1)
print(next,prev)

def eat(breakfast,lunch='ラーメン',dinner='カレー'):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')

eat('トースト','おにぎり')
eat('バナナ','そば','焼肉')
eat('バナナ',dinner='カレーうどん')

def eat(**kwargs):
    for key in kwargs:
        print(f'{key}に{kwargs[key]}を食べました')

eat(朝='納豆',昼='パスタ',夜='カレーパン')
