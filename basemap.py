from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
m = Basemap(
    llcrnrlon=44, llcrnrlat=24, urcrnrlon=63, urcrnrlat=40,
    rsphere=(6378137.00, 6356752.3142),
    resolution='i', projection='merc',
    lat_0=32.5, lon_0=53.688
)

cities = {
    'Tehran': {'lat': 35.6892, 'lon': 51.3890, 'pop': 6693706},
    'Mashhad': {'lat': 36.2605, 'lon': 59.6168, 'pop': 3001184},
    'Isfahan': {'lat': 32.6526, 'lon': 51.6680, 'pop': 1961260},
    'Karaj': {'lat': 35.8325, 'lon': 50.9915, 'pop': 1592492},
    'Shiraz': {'lat': 29.6199, 'lon': 52.5311, 'pop': 1565572},
    'Tabriz': {'lat': 38.0918, 'lon': 46.3028, 'pop': 1424641},
    'Qom': {'lat': 34.6399, 'lon': 50.8760, 'pop': 1260000},
    'Ahvaz': {'lat': 31.3202, 'lon': 48.6770, 'pop': 1184788},
    'Kermanshah': {'lat': 34.3140, 'lon': 47.0650, 'pop': 1083833},
    'Urmia': {'lat': 37.5501, 'lon': 45.0750, 'pop': 1000000}
}

for city, data in cities.items():
    x, y = m(data['lon'], data['lat'])
    size = data['pop'] / 600000
    m.plot(x, y, marker='o', color='red', markersize=size ,alpha=0.5)

    if city == 'Karaj':
        plt.text(x + 35000, y + 35000, f"{city}", fontsize=9, color='blue')
    else:
        plt.text(x + 5000, y + 5000, f"{city}", fontsize=9, color='blue')



m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='cornsilk', lake_color='skyblue')
m.drawmapboundary(fill_color='skyblue')


m.drawparallels(np.arange(25, 41, 3), labels=[1,0,0,0])
m.drawmeridians(np.arange(44, 64, 3), labels=[0,0,0,1])

plt.title("The Ten Most Populous Cities of Iran ", fontsize=14, fontweight='bold', color='navy')

plt.show()

