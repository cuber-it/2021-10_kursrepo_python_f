#!/usr/bin/env python3
import sys
import csv

def read_quotes(fname, delimiter=","):
    with open(fname) as file:
        return file.read().strip("\n").split(delimiter)

def csv_lesen(fname):
    csv_text = []
    with open(fname) as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_text.append(dict(row))
    return csv_text

if __name__ == "__main__":
    dateiname = "/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"
    rohdaten = read_quotes(dateiname)
    print(rohdaten)