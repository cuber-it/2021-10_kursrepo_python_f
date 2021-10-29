import pandas

class Quotes:
    def __init__(self, stockname, fname):
        self.fname = fname
        self.stockname = stockname.upper() # Aktien werden bei NASDAQ immer groß geschrieben
        self.data = pandas.DataFrame()

    def __raed_txt_and_prepare(self): # echt private und ist von außen nicht zugreifbar
        result = []    # Gesamtform ist dann [{}]
        with open(self.fname) as fd:
            raw = fd.read().splitlines()
        header = raw[0].replace(" ", "").split(",")
        for zeile in raw[1:]:
            zeile = zeile.replace(" ", "").replace("$", "").split(",")
            zeile[0] = f"{zeile[0][3:5]}.{zeile[0][:2]}.{zeile[0][6:]}"
            eintrag = {header[0]:zeile[0]}
            for i, key in enumerate(header[1:], start=1):
                eintrag[key] = float(zeile[i])
            result.append(eintrag)   
        self.data = pandas.DataFrame(result)

    def read(self):
        self.__raed_txt_and_prepare()
        return self

    def write(self, target, filetype):
        ftype = filetype.upper()
        if ftype =="CSV":
            self.data.to_csv(f"{target}.csv", index=False)
        else:
            raise RuntimeError(f"Unbekannter Datentyp: {ftype}")

if __name__=="__main__":
    aapl = Quotes("AAPL", "/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv")
    aapl.read(print(aapl.data)
    aapl.write("Testdaten", "csv")    
