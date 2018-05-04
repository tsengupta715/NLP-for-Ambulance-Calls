
#imports csv module and accesses the file as hospital_summary
import csv

def extract_EMS_string(call):
    EMS = "EMS"
    if EMS in call:
        print("EMS needed")
    # else:
    #     print("EMS not needed")

#def extract_cell_type(cell)

with open('911.csv', "rt") as hospital_summary: #, newline='\n'
    hospital_reader = csv.reader(hospital_summary)

# def mainFunc()
    #goes through rows and cells 
        #1. finds EMS
        #2. extracts string following "EMS: "
    row_ind = 0
    for row in hospital_reader:
        row_ind = row_ind + 1;
        print (row_ind)
        for cell in row:
            extract_EMS_string(cell)
            #extract_cell_type(cell)

