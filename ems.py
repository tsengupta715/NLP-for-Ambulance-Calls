
import csv
with open('911.csv', newline='') as hospital_summary:
    hospital_reader = csv.reader(hospital_summary)
    for row in hospital_reader:

        EMS = "EMS"
        row_string = ' '.join(row)

        if EMS in row_string:
            print("EMS needed")
        else:
            print("EMS not needed")

