class Eingabe:
    daten=None

    def _aufbereitung (self):
        self.daten=self.daten.split(",")

    def einlesen (self):
        self.daten=input("Tippdaten eingeben:")
        self._aufbereitung()
        return self

class Dateieingabe(Eingabe):
    def __init__(self,)
    #eigenes einlesen

if __name__=="__main__":
    eingabe=Dateieingabe().einlesen("Dateiname.txt")
    print(eingabe.daten)