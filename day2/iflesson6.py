print('y or n')
okane_aruka = input('お金に余裕は？>>')
if okane_aruka =='y':
    onaka_suiteruka =input('お腹すごく空いてる？>>')
    nomitai_kibunka =input('ビール飲みたい？>>')
    if onaka_suiteruka=='y' and nomitai_kibunka =='y':
        print('焼肉ぅ！！！')
    elif onaka_suiteruka=='y':
        print('カレー！！')
    elif nomitai_kibunka =='y':
        print('焼き鳥ぃ！')
    else:
        print('パスタァ')
    yashoku_iruka=input('夜食ぅ？>>')
    if yashoku_iruka=='y':
        print('(ファミチキください)')
else:
    print('家で食べる')
