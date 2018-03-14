
#imports csv module and accesses the file as hospital_summary
import csv
with open('911.csv', newline='') as hospital_summary:
    hospital_reader = csv.reader(hospital_summary)

    #parses each row of data
    for row in hospital_reader:

        #combines the list of strings in each row to one large string
        EMS = "EMS"
        for call in row:
            if EMS in call:
                print("EMS needed")
            else:
                print("EMS not needed")


