import folium

mapa = folium.Map(
    location=[-23550093493433984, -46.6341472592547],
    tiles="Stamen Terrain",
    zoom_start=16
)

folium.Marker(
    [-23.550093493433984, -46.6341472592547],
    popup="<i>Praca da Se</i>",
    tooltip="Click aqui!"
).add_to(mapa)

mapa.save(r'mapa.html')