#!/usr/bin env python3
import pandas as pd
import pprint
df = pd.read_csv('/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv')
print(df)


#!/usr/bin/bin python3

def read_quotes(fname, encoding="utf-8"):
    with open(fname, encoding=encoding) as file:
        return file.read().splitlines()

def prepare_quotes(raw):
    result = []
    header = raw[0].replace(" ", "").split(",")
    for zeile in raw[1:]:
        zeile = zeile.replace(" ", "").replace("$", "").split(",")
        zeile[0] = f"{zeile[0][3:5]}.{zeile[0][:2]}.{zeile[0][6:]}"
        eintrag = {header[0]:zeile[0]}
        for i, key in enumerate(header[1:], start=1):
            eintrag[key] = float(zeile[i])
        result.append(eintrag)   
    return result

def write_quotes(target, data, encoding="utf-8"):
    with open(target, "w", encoding=encoding) as file:
        file.write(pprint.pformat(data))
        file.flush()        

if __name__=="__main__":
    import pprint
    #Testbereich bzw für standalone Einsatz
    FNAME = '/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv'
    raw = read_quotes(FNAME)
    quotes = prepare_quotes(raw)
    write_quotes("Ergebnis_st.txt", quotes)

df.to_excel('aktientest.xlsx', sheet_name='Aktien', index=False)