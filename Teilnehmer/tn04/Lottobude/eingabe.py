class Eingabe:

    def __init__(self):
        self.daten = None

    def read(self):
        self.daten = input("Bitte Wert eingeben: ")
        return self


