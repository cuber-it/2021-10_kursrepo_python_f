import csv

filename=r"/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"


print(filename)

with open(filename,'r') as data:
   for line in csv.reader(data):
            print(line)

with open(filename, 'r') as data:
      
    for line in csv.DictReader(data):
        print(line)

#for key in a_dict.keys():
#...     print(key)

#a_csv_file = open(filename, "r")
#dict_reader = csv.DictReader(a_csv_file)

#ordered_dict_from_csv = list(dict_reader)[0]
#dict_from_csv = dict(ordered_dict_from_csv)

import pandas as pd

dict_from_csv = pd.read_csv(filename, header=None, index_col=0, squeeze=True).to_dict()
print(dict_from_csv)

df = pd.read_csv(filename)
print(df.head())

print(df.info())