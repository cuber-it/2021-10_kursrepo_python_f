filename = '/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv'
with open(filename) as fd:
    lines = fd.readlines()
for line in lines:
    print(line)
    line.split(',')
