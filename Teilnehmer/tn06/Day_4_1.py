class Eingabe:
    def __init__(self):
        self.daten = None

    def _aufbereitung(self):
        self.daten = self.daten.split(",")

    def einlesen(self):
        self.daten = input("Tippdaten eingeben:")
        self._aufbereitung()
        return self

class DatenEingabe(Eingabe):
    def einlesen(self, fname):
        with open(fname) as fd:
            self.daten = fd.readline()
        self._aufbereitung()
        return self

if __name__ == "__main__":
    eingabe = DateiEingabe().einlesen("testdaten.txt")
    print(eingabe.daten)

