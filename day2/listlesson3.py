import random
num=int(input('何回？>>'))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print(sum(dices))

num=int(input('何回？>>'))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print(f'出た目は{set(dices)}の{len(set(dices))}種類です')


num=int(input('いくつ？>>'))
data=[random.randrange(100,1000,2) for _ in range(num)]
data.sort(reverse=True)
print(num,'個生成、降順表記',data)

import random
while True:
	user=int(input('手を入力[0:グー,1:チョキ,2:パー]>>'))
	pc=random.randint(0,2)
	hands=['グー','チョキ','パー']
	print(f'あなたは{hands[user]},PCは{hands[pc]}')
	if user==pc:
		print('あいこ')
		continue
	elif (user+3-pc)%3==1 :
		print('あなたの負け')
	else:
		print('あなたの勝ち')
	break

