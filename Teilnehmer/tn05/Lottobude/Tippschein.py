class Tippschein:
    def __init__(self, eingabe):
        # Zerlegen
        # Umwandeln
        # check 1: 6 Zahlen
        # check 2: 1-49
        # check 3: keine Doppelten
        # speichern in: self.tipp - vom Typ Liste
        if isinstance(eingabe, str):
            eingabe = eingabe.split(",")
        if len(eingabe) == 6:
            for i, n in enumerate(eingabe):

    #def _convert_int(self, val):
        #    result = []
        #    for i in val:
        #        result.append(int(i))
        #    return result

        #def _check_len(self, val, len=6):
        #    if len(val) != len:
        #        raise RuntimeError(f"Länge: {len(val)}")

        #def _check_dups(self, val):
        #    if len(val)!=len(set(val)):
        #        raise RuntimeError(f"Duplicate: {val}")

        pass

if __name__ == "__main__":
    t = Tippschein("1,2,3,4,5,6")
    print(t.tipp)

    # Test mit Fehlern nicht vergessen! :-D
