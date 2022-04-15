import gmplot
import pandas as pd

dataset = pd.read_csv('venv/data/out.csv')
latitudes = dataset.loc[:, 'latitude']
longitudes = dataset.loc[:, 'longitude']
min_latitude = latitudes.min()
max_latitude = latitudes.max()
min_longitude = longitudes.min()
max_longitude = longitudes.max()

gmap = gmplot.GoogleMapPlotter(35, -102, 5)
gmap.scatter(latitudes[:1000], longitudes[:1000], 'red', size = 10)
gmap.apikey = 'AIzaSyBgYjmLWQd4j0N_WUL68lJcUNGCxN_dyVg'
gmap.draw('gmplot2.html')