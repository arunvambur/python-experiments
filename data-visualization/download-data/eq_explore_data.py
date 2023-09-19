import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

filename = "data/1.0_week.geojson"

with open(filename, encoding="utf8") as f:
    all_eq_data = json.load(f)

#readable_file = "data/readable_eq_data.json"
#with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
    title = eq_dict['properties']['title']
    hover_texts.append(title)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')



