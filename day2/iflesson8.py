month = int(input('何月？>>'))
if month in [1,3,5,7,8,10,12]:
    print('31日まである')
else:
    if month !=2:
        print('30日まである')
    else:
        print('1年で一番寒い月')
    print('年が明けてから')
print('{}ヵ月が過ぎました'.format(month))
