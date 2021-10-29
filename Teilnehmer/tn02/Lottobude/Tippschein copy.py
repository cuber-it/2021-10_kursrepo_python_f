class Tippschein:
    def __init__(self, eingabe):
        self.eingabe=eingabe
   
    def tipp (self):
        if isinstance(self.eingabe, str):
            listeneu=self.eingabe.split(",")
        
        list_int=[]
        for i in listeneu:
            list_int.append(int(i))   
        if len(list_int)==6:
            return list_int
        if len(list_int)==len(set(list_int)):
            return list_int
        
        list_int_neu=[]
        for i in list_int:
            if i in range(1,50):
                list_int_neu.append(i)

        if len(list_int_neu)!=6:
            print("Du hast Zahlen angegeben, die außerhalb des zulässigen Wertebereichs von 1-49 liegen.")
        else:
            return list_int_neu
                    
if __name__=="__main__":
    t=Tippschein("1,2,9,3,10,50")
    print(t.tipp())