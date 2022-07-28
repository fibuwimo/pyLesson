import requests
import json
from datetime import datetime,timedelta,timezone

url = ('https://api.openweathermap.org/data/2.5/weather'
'?zip={zip}&appid={key}&lang=ja&units=metric')
url=url.format(zip='166-0014,JP',key='a66cd3acfcd9761c9199b4df4c0c947a')
jsondata=requests.get(url).json()

print('都市名:',jsondata['name'])
print('気温:',jsondata['main']['temp'])
print('天気:',jsondata['weather'][0]['main'])
print('天気詳細:',jsondata['weather'][0]['description'])

tz=timezone(timedelta(hours=+9),'jst')
for dat in jsondata['list']:
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[:-9]
    weather=dat['weather'][0]['description']
    temp=dat['main']['temp']
    print(f'日時:{jst},天気:{weather},気温:{temp}度')
