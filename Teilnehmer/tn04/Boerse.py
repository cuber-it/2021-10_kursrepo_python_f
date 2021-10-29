#!/usr/bin/env python3
import sys
import os
import csv

fname_datei = r"/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"
daten = []

def read_data(datei):
    results = []
    with open(datei, newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)
    print(results)
    return(results)

def vdata(y):
    pass

def adata(z):
    pass

  

# daten = read_data(fname_datei)
# print(read_data(fname_datei))