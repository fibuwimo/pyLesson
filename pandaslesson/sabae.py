import pandas as pd
import folium
df = pd.read_csv('200.csv',encoding='shift-jis')
m=folium.Map(location=[35.942957,136.198863],zoom_start=16)

hydrant=df[['緯度','経度']].values

for data in hydrant:
    folium.Marker([data[0],data[1]]).add_to(m)
m.save("sabae.html")
