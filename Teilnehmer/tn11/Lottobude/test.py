import random
class lostrommel:
    def ziehung(self):
        self.lottozahlen_gewinner = []
        self.lottozahlen_gewinner = random.sample(range(1,50), 6)
        self.lottozahlen_gewinner.sort()
        #print(self.test)
        return self.lottozahlen_gewinner

def machwas(fp, daten):
    result = []
    for v in daten:
        result.append(fp(v))
    return result

if __name__ == "__main__":
    l = [1,2,3,4]
    print(machwas(lambda x: x * x, l))
    x_werte = [ {"NAME" : "Willi"}, {"NAME" : "Heinz"},{"NAME" : "Klaus"} ]
    print(machwas(lambda x: x["NAME"] if "i" in x["NAME"] else None, x_werte))
   # l = lostrommel()
   # print(l.ziehung())


    # self.ziehung = random.sample(range(1,50), 6)