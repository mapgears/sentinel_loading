import geojson
import json
import point as p

x_min=int(input("x_min= "))
x_max=int(input("x_max= "))
y_min=int(input("y_min= "))
y_max=int(input("x_max= "))

p1 = p.Point(x_min,y_min)
p2 = p.Point(x_max,y_min)
p3 = p.Point(x_max,y_max)
p4 = p.Point(x_min,y_max)

geos = []
poly = {
    'type': 'Polygon',
    'coordinates': [[p1.get_point(), p2.get_point(), p3.get_point(), p4.get_point(),p1.get_point()]]
}
geos.append(poly)
geometries = {
    'type': 'FeatureCollection',
    'features': [{"type": "Feature", "geometry":geos[0], "properties": {"name_fr": ""}}]
}
geo_str = json.dumps(geometries)

with open('../../Geojson/polygone.geojson', 'w') as outfile:
	outfile.write(geo_str)
print(geo_str)