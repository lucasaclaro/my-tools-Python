import folium

map = folium.Map(
    location=[-23.550093493433984, -46.6341472592547],
    titles = 'Stamen Terrain', #estilo do mapa
    zoom_start=16
)

folium.Marker(
    location=[-23.550093493433984, -46.6341472592547],
    popup='<i>Praça da Sé</i>',
    tooltip='Click aqui'
).add_to(map)

map.save('map.html')