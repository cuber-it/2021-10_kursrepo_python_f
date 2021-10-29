#!/usr/bin/env python3

import csv
def csv_einlesen():
    with open ('/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv') as csvdatei:
        csv_reader_object = csv.reader(csvdatei)

        zeilennummer = 0
        for row in csv_reader_object:

            if zeilennummer == 0:
                print(f'Spaltennamen sind: {", ".join(row)}')
            else:
                print(f' Datum: {row[0][3:5]}.{row[0][:2]}.{row[0][6:]} | Close/Last: {row[1].replace("$","")}\t| Volume: {row[2]} | Open: {row[3].replace("$","")} \t| High: {row[4].replace("$","")} | Low: {row[5].replace("$","")} ')
            zeilennummer += 1

        print(f'Anzahl Datensätze: {zeilennummer-1}')

csv_einlesen()   
    