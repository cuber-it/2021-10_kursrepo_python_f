import random

class Lostrommel:
    def ziehung(self):
        self.num_list = random.sample(range(0, 50), 6)
        return self.num_list

if __name__ == "__main__":
    l = Lostrommel()
    print(l.ziehung())