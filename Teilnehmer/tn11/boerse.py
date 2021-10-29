#!/usr/bin/env python3
import csv
import time

with open('/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn11/HistoricalQuotes.csv') as csvdatei:
    csv_reader_object = csv.reader(csvdatei)
    zeilennummer = 0
    for row in csv_reader_object:
        if zeilennummer == 0:
            print(f'Spaltennamen sind: {", ".join(row)}')
        else:
             print(f'- Datum: {row[0]} | Close/Last: {row[1]} | Volume: {row[2]} | Open: {row[3]} | High: {row[4]} | Low: {row[5]} ')
        zeilennummer += 1
    print(f'Anzahl Datensätze: {zeilennummer-1}')

