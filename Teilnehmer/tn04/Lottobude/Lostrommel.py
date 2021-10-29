import random

class Lottotrommel:
    
    def ziehung(self):
        self.lottozahlen = random.sample(range(1, 50), 6)
        return self.lottozahlen




if __name__ == "__main__":
    l = Lottotrommel()
    print(l.ziehung())
    