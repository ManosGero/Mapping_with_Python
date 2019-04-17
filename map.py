import pandas
import folium

map = folium.Map([40.63,22.94],zoom_start = 3)

fg =folium.FeatureGroup(name = "My feauter")
try:
    data = pandas.read_csv("Volcanoes.txt")
except:
    data = False
    
for intex , row  in data.iterrows() :
        fg.add_child(folium.Marker(location=[row["LAT"],row["LON"]], popup =row["NAME"], icon = folium.Icon(color = "red")))

map.add_child(fg)

map.save("Map.html")
