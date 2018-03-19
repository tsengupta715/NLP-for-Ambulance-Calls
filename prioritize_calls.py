

#inserts dictionary of priorities based upon MPDS

import csv
#opens key_words.csv as key_words
with open('key_words.csv', 'rt') as key_words:
    #for each row, assigns symptoms as the first column and priority as the second column
    for row in key_words.readlines():
        mpds_key = row.split(',')
        symptoms = mpds_key[0]
        priority = mpds_key[1].strip()

        #creates a dictionary as priority_dict with the key being the key words and the value is the priority
        priority_dict = {}
        priority_dict.update({symptoms:priority})


#imports csv module and accesses file as summary_hospital
with open('911.csv', newline='') as summary_hospital:
    summary_reader = csv.reader(summary_hospital)

    #parses each row of data and combines into one string
    for row in summary_reader:
        joined_call = ''.join(row)

        #checks if the string is in the symptoms and returns the priority if it is
        if symptoms.upper() in joined_call.upper():
            print(row)
            print(priority)





