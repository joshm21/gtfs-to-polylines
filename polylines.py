import csv
import simplekml

kml = simplekml.Kml()

current_trip = ""
current_line = None

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        trip_id = row[0]
        stop_name = row[3]
        stop_lat = row[4]
        stop_lon = row[5]

        if trip_id != current_trip:
            current_trip = trip_id
            current_line = kml.newlinestring(name=current_trip)

        current_line.coords.addcoordinates([(stop_lon,stop_lat)])



kml.save("lines.kml")
