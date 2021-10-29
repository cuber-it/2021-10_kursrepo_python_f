import pandas

class Stockqoutes:
    def __init__(self, fname):
        self.fname = fname



    def readfile(self):
        ergebnis =[]
        with open(self.fname) as fd:
            daten = fd.read().splitlines()
        header = raw[0].replace(" ", "").split(",")
        for zeile in raw[1:]:
            zeile = zeile.replace(" ", "").replace("$", "").split(",")
            zeile[0] = f"{zeile[0][3:5]}.{zeile[0][:2]}.{zeile[0][6:]}"
            eintrag = {header[0]: zeile[0]}
            for i, key in enumerate(header[1:], start=1):
                eintrag[key] = float(zeile[i])
            result.append(eintrag)
        self.data = pandas.DataFrame(result)

    def verarbeitung(self):
        pass


test = Stockqoutes("/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv")
print(test.readfile)

