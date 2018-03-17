
#inserts dictionary of priorities based upon MPDS

import csv


#creates function which reads the csv module and creates a dictionary
call_reader = csv.DictReader(open('mpds.csv','rt'))
priority_list = []
for call in call_reader:
    priority_list.append(call)
