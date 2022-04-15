import csv
from geopy.geocoders import Nominatim
import logging
import os


with open('venv/data/data_geocoded_ephad.csv', 'r') as file:
    addresses = list(csv.reader(file))

listSize = len(addresses)

print('Nombre de lignes: ', listSize)

index =0

logger = logging.getLogger(__name__)
c_handler = logging.basicConfig(filename="app.log",format="%(asctime)s:%(levelname)s:%(message)s")
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)

os.remove('venv/data/out.csv')

while index < listSize:

    progress = 100 * (index+1) / listSize

    if addresses[index][0][0].isdigit():
        geolocator = Nominatim(user_agent="test", timeout=4)
        location = geolocator.geocode(addresses[index])

        if location is None:
            logger.warning("[" + str(progress) + "%] No address found for " + str(addresses[index]) + " at index " + str(index))
        else:
            print("[" + str(progress) + "%] Found location " + str(location.address) + " at index " + str(index))

            latlong = (location.latitude, location.longitude)
            with open('venv/data/out.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow(addresses[index])
                writer.writerow(latlong)
    else:
        logger.warning("[" + str(progress) + "%] Skipping " + str(addresses[index]) + " at index " + str(index))

    index += 1

