import pprint as pp
from datetime import datetime
import csv
with open('/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn02/HistoricalQuotes.csv') as csvdatei:
    csv_reader_object=csv.reader(csvdatei,delimiter=',')
    
    d=[]
    for row in csv_reader_object:
        k=['Date','Close/Last','Volume', 'Open', 'High', 'Low']
        w=row[0:5]
        datetime.strftime(row[0],'%d.%m.%Y')
        s=dict(zip(k,w))
        d.append(s)
    pp.pprint(d)


