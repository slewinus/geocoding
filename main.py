

import pandas as pd
import csv
import googlemaps
import geocoder
from geopy.geocoders import Nominatim


f = open('Data-nom.csv', 'r')

NumberOfLine = 0
for line in f:
    NumberOfLine += 1

print('Nombre de lignes: ',NumberOfLine)

e = 0
d = 0
while d < 20464 :

    e += 1
    with open('Data-nom.csv', 'r') as file:
        val = list(csv.reader(file))[e]
        print(val)
        x = val
        geolocator = Nominatim(user_agent="test")
        location = geolocator.geocode(x)


    print(location.address)
    latlong = (location.latitude, location.longitude)
    print(latlong)

    with open('out.csv', 'w', newline = '') as csvfile:
        my_writer = csv.writer(csvfile, delimiter = ' ')
        my_writer.writerow(latlong)

    d += 1
