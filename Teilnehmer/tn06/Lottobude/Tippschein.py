#!/usr/bin/env python3
class Tippschein:

    def __init__(self, eingabe):
        self.tipp = eingabe
        self.input_check()

             
        #zerlegen
        #umwandeln
        #check1: 6 Zahlen
        #check2: 1-49
        #check3: keine doppelten
        #speichern in: self.t.tipp - vom typ liste
  

    def input_check(self):
        try:
            #split string zu einer Liste
            self.tipp = list(self.tipp.split(","))
            #Prüfe Länge und auf doppelte Einträge
            if len(self.tipp) <=6 and len(self.tipp) == len(set(self.tipp)):
                for i in self.tipp:
                    if 1 <= int(i) <= 49:
                        print("ok")
                    else:
                        print(f"Zahl üngültig: {i}") 
                        break
            else:
                print(f"Tipp üngültig: {self.tipp}") 
        except:
            raise RuntimeError(f"Unbekannter Dateityp: {i}")

if __name__ == "__main__":
    t=Tippschein("1,2,3,4,5,6")
    #t.input_check()
    print(t.tipp)



        #Test mit Fehlern nicht vergessen