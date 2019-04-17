import pandas
import folium
import numpy



map = folium.Map([40.63,22.94],zoom_start = 2)

fg_v =folium.FeatureGroup(name = "Volcanoes")
fgp =folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open('world.json',
                                      'r',
                                      encoding = 'utf-8-sig').read(),
                                      style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' } ))
try:
    data = pandas.read_csv("ALL World's volcanoes.csv", sep=";")
    
except:
    data = False
latL  = list(data["Lat"])
lonL  = list(data["Lon"])
eleL  = list(data["Elevation (m)"])
nameL = list(data["Volcano Name"])

def getColorByEle(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000 :
        return "orange"
    else :
        return "red"
    


for lat,lon,ele,name  in zip(latL,lonL,eleL,nameL) :
    pop = "Volcano Name: {} \nElevation: {} (m)".format(name,ele)
    fg_v.add_child(folium.CircleMarker(location=[lat,lon],
                                     radius = 7,
                                     popup = pop ,
                                     fill_color=getColorByEle(ele),
                                     fill = True,
                                     color = "grey",
                                     fill_opacity = 0.7    ))
    
map.add_child(fgp)
map.add_child(fg_v)

map.add_child(folium.LayerControl())

map.save("Map.html")
