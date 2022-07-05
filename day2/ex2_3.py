p1={'読書','昼寝','映画鑑賞','散歩','料理'}
p2={'テニス','将棋','料理','読書','旅行'}
input('エンター>>')
common=p1 & p2
total=p1 | p2
compatibility_rate =len(common) / len(total)*100
print(f'相性度{compatibility_rate}パーセントです')
