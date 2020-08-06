  
import pandas
from geopy.geocoders import Nominatim
import gmplot


colnames=['latitude','longitude']
data=pandas.read_csv('twittr117.csv',names=colnames)
latitude=data.latitude.tolist()
longitude=data.longitude.tolist()
for i in range(0,latitude.count('99999.99')):
    latitude.remove('99999.99')
for i in range(0,longitude.count('9999.99')):
    longitude.remove('9999.99')
latitude=latitude[1:]
longitude=longitude[1:]
latitude=list(map(float, latitude))
longitude=list(map(float, longitude))

data=pandas.read_csv('twittr118.csv',names=colnames)
latitude1=data.latitude.tolist()
longitude1=data.longitude.tolist()
for i in range(0,latitude1.count('99999.99')):
    latitude1.remove('99999.99')
for i in range(0,longitude1.count('9999.99')):
    longitude1.remove('9999.99')
latitude1=latitude1[1:]
longitude1=longitude1[1:]
latitude1=list(map(float, latitude1))
longitude1=list(map(float, longitude1))
latitude.extend(latitude1)
longitude.extend(longitude1)
print(latitude)
print(longitude)
gmap = gmplot.GoogleMapPlotter(30, 0, 3)


# Overlay our datapoints onto the map
gmap.heatmap(latitude, longitude)

# Generate the heatmap into an HTML file
gmap.draw("fina234.html")
