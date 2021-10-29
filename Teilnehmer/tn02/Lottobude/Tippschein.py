class Tippschein:
    def __init__(self, eingabe):
        self.eingabe=eingabe
   

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

    def tipp (self):
        if not isinstance(self.eingabe, str):
            print("Die Eingabe muss als String erfolgen")
        else:
            listeneu=self.eingabe.split(",")
            #list_int = self._convert_int(listeneu)
            list_int = []
            for i in listeneu:
                list_int.append(int(i))   

            #self._check_len(list_int)
            #self._check_dups(list_int)

            if len(list_int)!=6:
                print("Es muss eine Eingabe von exakt 6 Zahlen erfolgen.")
            elif len(list_int)!=len(set(list_int)):
                print("Du hast doppelte Werte angegeben.")
            else:
                list_int_neu=[]
                for i in list_int:
                    if i in range(1,50):
                        list_int_neu.append(i)

                if len(list_int_neu)!=6:
                    print("Du hast Zahlen angegeben, die außerhalb des zulässigen Wertebereichs von 1-49 liegen.")
                else:
                    return list_int_neu
                    
if __name__=="__main__":
    t=Tippschein("1,2,9,3,4,5")
    print(t.tipp())