import folium
map = folium.Map(location=[40.63,22.94],zoom_start = 10)

fg = folium.FeatureGroup(name = "My feauter")

for condinates in [[40.631,22.942],[40.64,22.943],[55.64,66.943]]:
    fg.add_child(folium.Marker(location=condinates, popup ="Hi I am a Marker", icon = folium.Icon(color = "green")))
map.add_child(fg)

map.save("Map.html")
