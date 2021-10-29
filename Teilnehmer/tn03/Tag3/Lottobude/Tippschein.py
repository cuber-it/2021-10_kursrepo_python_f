from random import *

class Tippschein:
    def __init__(self, eingabe):
        # Zerlegen
        # Umwandeln
        self.tipreihe = tipreihe
        self.results = []
        
    def get_results(self):
        # Check 1: 6 Zahlen
        while len(self.results) < 6:
            # Check 2: 1-49
            self.random_number = randint(1, 49)
            if self.random_number not in self.results:
                self.results.append(randint(1, 49))
        
        # Check 3: keine doppelten Zahlen
        # speichern in: self.tipp - vom Typ Liste

if __name__ == "__main__":
    t = Tippschein("1,2,3,4,5,6")
    print(t.tipp)

    # Test mit Fehlern nicht vergessen! :-D

class Lotto:

    def __init__(self, tipreihe):
        self.tipreihe = tipreihe
        self.results = []

    def __str__(self):
        text = "Ziehung der Lottozahlen:\n"
        text += f"Tip: {self.tipreihe}\n"

        return text

    def get_results(self):
        while len(self.results) < 6:
            self.random_number = randint(1, 49)
            if self.random_number not in self.results:
                self.results.append(randint(1, 49))


      #  random.sample(list(range(1,50),6)
        print(self.results)
           

    def compare_results(self):
        print(self.tipreihe)
        print(lotto.get_results())

    def stat_results(self):
        print()


if __name__ == "__main__":
    lotto = Lotto([1,2,3,4,5,6]) # __init__
    lotto.get_results()
    print(lotto.get_results())
    #print(lotto.compare_results())