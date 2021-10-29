# Einlesen von Börsendaten

#from datetime import datetime
#print(datetime.today())

FILE = '/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv', 'r'

def read_quotes(FILE):
    with open(FILE) as file:
        return file.read().splitline()

if __name__ == '__main__':
    




