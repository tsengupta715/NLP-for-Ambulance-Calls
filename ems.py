
#imports csv module and accesses the file as hospital_summary
import csv
with open('911.csv', newline='') as hospital_summary:
    hospital_reader = csv.reader(hospital_summary)
    #parses each row of data 
    for row in hospital_reader:

        #combines the list of strings in each row to one large string
        EMS = "EMS"
        row_string = ' '.join(row)

        #detects whether or not EMS is in the string
        if EMS in row_string:
            print("EMS needed")
        else:
            print("EMS not needed")

