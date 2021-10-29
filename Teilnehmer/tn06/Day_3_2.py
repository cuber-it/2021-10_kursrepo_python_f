#!/usr/bin/env python3

#Klasse Quotes
import pandas

class Quotes:
    def __init__(self, dateiname):
        self.dateiname = dateiname
        self.data = pandas.DataFrame()

    def __read_txt_and_prepare(self): # echt private, wird nicht zugreifbar in der Vererbung sein
        result = []   # Gesamtform ist dann [{}]
        with open(self.dateiname) as fd:
            raw = fd.read().splitlines()
        header = raw[0].replace(" ", "").split(",")
        for zeile in raw[1:]:
            zeile = zeile.replace(" ", "").replace("$", "").split(",")
            zeile[0] = f"{zeile[0][3:5]}.{zeile[0][:2]}.{zeile[0][6:]}"
            eintrag = {header[0]: zeile[0]}
            for i, key in enumerate(header[1:], start=1):
                eintrag[key] = float(zeile[i])
            result.append(eintrag)
        self.data = pandas.DataFrame(result)

    def read(self):
        self.__read_txt_and_prepare()
        return self

    def write(self, target, filetype):
        ftype = filetype.upper()
        if ftype == "CSV":
            self.data.to_csv(f"{target}.csv", index=False)
        elif ftype == "JSON":
            self.data.to_json(f"{target}.json", orient='records')
        else:
            raise RuntimeError(f"Unbekannter Dateityp: {ftype}")
    
    def to_dict(self):
        return self.data.to_dict('records')

if __name__ == "__main__":
    aapl = Quotes("/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv")
    if not aapl.data.empty:
        print(aapl.data)
    else:
        print("Daten sind leer")
    
    #aapl.read()
    #if not aapl.data.empty:
    #    print(aapl.data)
    #else:
    #    print("Leer")
    
    aapl.write("Testdaten", "CSV")


