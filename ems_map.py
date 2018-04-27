
from gmplot import gmplot

# Place map (try both ways below)
gmap = gmplot.GoogleMapPlotter(40.2290, -75.3879, 13)
gmap = gmplot.GoogleMapPlotter.from_geocode("Montgomery County, Pennsylvania")

import csv
#opens 911 calls as coordinates
with open('dummy.csv', 'rt') as ambulance_calls:
    csvreader = csv.reader(ambulance_calls)
    header = next(csvreader)

    #for each row, assigns lat as first row and lng as second
    for row in ambulance_calls:

        coordinates = row.split(',')
        lat = float(coordinates[0])
        lng = float(coordinates[1])
        if coordinates[-1].strip() is 'A':
            # Marker
            a_priority_lat, a_priority_lng = lat,lng
            gmap.marker(a_priority_lat, a_priority_lng, 'limegreen')

        elif coordinates[-1].strip() is 'B':
            # Marker
            b_priority_lat, b_priority_lng = lat,lng
            gmap.marker(b_priority_lat, b_priority_lng, 'yellow')

        elif coordinates[-1].strip() is 'C':
            # Marker
            c_priority_lat, c_priority_lng = lat,lng
            gmap.marker(c_priority_lat, c_priority_lng, 'gold')

        elif coordinates[-1].strip() is 'D':
            # Marker
            d_priority_lat, d_priority_lng = lat,lng
            gmap.marker(d_priority_lat, d_priority_lng, 'darkorange')

        elif coordinates[-1].strip() is 'E':
            # Marker
            e_priority_lat, e_priority_lng = lat,lng
            gmap.marker(e_priority_lat, e_priority_lng, 'red')

        else:
            print('no')


# Draw
gmap.draw("my_map.html")
