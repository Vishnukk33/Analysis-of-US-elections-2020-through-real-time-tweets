# Plotting Heatmaps using Coordinates.

import pandas
from geopy.geocoders import Nominatim
import gmplot

latitude_final=[]
longitude_final=[]
for name in range(1,6):
    data=pandas.read_csv('repub'+str(name)+'.csv')
    latitude=data.latitude.tolist()
    longitude=data.longitude.tolist()
    # Non Geo-tagged tweets were given a value of (99999.99,99999.99). We are removing them from the list.
    for i in range(0,latitude.count(99999.99)):
        latitude.remove(99999.99)
    for i in range(0,longitude.count(99999.99)):
        longitude.remove(99999.99)
    latitude=list(map(float, latitude))
    longitude=list(map(float, longitude))
    latitude_final.extend(latitude)
    longitude_final.extend(longitude)
    print(len(latitude_final))
    print(len(longitude_final))
gmap = gmplot.GoogleMapPlotter(30, 0, 3)


# Overlay the datapoints into the map
gmap.heatmap(latitude_final, longitude_final)

# Generate the heatmap into an HTML file
gmap.draw("repub_map.html")
