import random

class Lostrommel:

    def ziehung(self):
        self.ziehung = random.sample(range(1,50), 6)
        self.ziehung.sort()
        return self.ziehung

if __name__ == "__main__":
    l = Lostrommel()
    print(l.ziehung())
    
