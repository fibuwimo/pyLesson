scores={'ne':60,'da':80,'se':50}
key=input('科目>>')
if key in scores:
    print('登録済み')
else:
    data=int(input('点数>>'))
    scores[key]=data
print(scores)
