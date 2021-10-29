class Tippschein:
    def __init__(self, eingabe):
        
            self.tipp = eingabe
            self.input_check()
    
    def input_check(self):
        try:
            self.tipp = list(self.tipp.split(",")) #zerlegen #umwandeln #speichern in: self.tipp - vom typ liste
           
            if len(self.tipp) <=6 and len(self.tipp) == len(set(self.tipp)): #check1: 6 Zahlen und #check3: keine doppelten
                for i in self.tipp:
                    if 1 <= int(i) <= 49: #check2: 1-49 und Integer-Wert
                        pass #print(f"ok: {i}")
                    else:
                        #print(f"Zahl üngültig: {i}") 
                        return print(f"Zahl üngültig: {i}") 
            else:
                
                return print(f"Tipp üngültig: {self.tipp}") 
        except:
            raise RuntimeError(f"Keine Zahl: {i}")

#if self.tipp.isdigit():
if __name__ == "__main__":
        t=Tippschein("1,2,3,4,5,6")
      #  t.input_check()
        print(t.tipp)

        #Test mit Fehlern nicht vergessen
