#inserts dictionary of priorities based upon MPDS
import csv

#opens key_words.csv as key_words
with open('key_words.csv', 'rt') as key_words:
    #for each row, assigns symptoms as the first column and priority as the second column
    for row in key_words.readlines():
        array = row.split(',')
        symptoms = array[0]
        priority = array[1].strip()
        #creates a dictionary as priority_dict with the key being the key words and the value is the priority
        priority_dict = {}
        priority_dict.update({symptoms:priority})

