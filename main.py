import csv
from geopy.geocoders import Nominatim


with open('Data-nom.csv', 'r') as file:
    addresses = list(csv.reader(file))

listSize = len(addresses)

print('Nombre de lignes: ', listSize)

index = 0
while index < listSize:
#    print(addresses[index])

    progress = 100 * (index+1) / listSize

    if addresses[index][0][0].isdigit():
        geolocator = Nominatim(user_agent="test")
        location = geolocator.geocode(addresses[index])

        if location is None:
            print("[" + str(progress) + "%] No address found for " + str(addresses[index]) + " at index " + str(index))
        else:
            print("[" + str(progress) + "%] Found location " + str(location.address) + " at index " + str(index))

            latlong = (location.latitude, location.longitude)
#            print(latlong)
            with open('out.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow(latlong)

    else:
        print("[" + str(progress) + "%] Skipping " + str(addresses[index]) + " at index " + str(index))

    index += 1