from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(40.2290, -75.3879, 13)

import csv
#opens 911 calls as coordinates
with open('911.csv', 'rt') as ambulance_calls:
    csvreader = csv.reader(ambulance_calls)
    header = next(csvreader)
    coordinates_list = []
    #for each row, assigns lat as first row and lng as second
    counter = 0
    for row in ambulance_calls.readlines():
        if counter < 10:
            coordinates = row.split(',')
            lat = float(coordinates[0])
            lng = float(coordinates[1])

            #appends coordinates to the empty list
            coordinates_list.append((lat,lng))
            counter += 1

# Scatter points
ambulance_lat, ambulance_lng = zip(*coordinates_list)
gmap.scatter(ambulance_lats, ambulance_lngs, '#3B0B39', size=40, marker=False)

# Draw
gmap.draw("my_map.html")
