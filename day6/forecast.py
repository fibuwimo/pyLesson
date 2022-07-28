import requests
import json
from datetime import datetime,timedelta,timezone
from pprint import pprint
import pandas as pd


url = ('https://api.openweathermap.org/data/2.5/forecast'
'?q={city}&appid={key}&lang=ja&units=metric')
url=url.format(city='Tokyo,jp',key='a66cd3acfcd9761c9199b4df4c0c947a')
jsondata=requests.get(url).json()

df=pd.DataFrame(columns=['気温'])

tz=timezone(timedelta(hours=+9),'jst')
for dat in jsondata['list']:
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[5:-9]
    weather=dat['weather'][0]['description']
    temp=dat['main']['temp']
    df.loc[jst]=temp
    #print(f'日時:{jst},天気:{weather},気温:{temp}度')
