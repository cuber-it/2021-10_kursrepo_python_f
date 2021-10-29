# 6 Zufallzahlen zwischen 6 und 49 ohne Dopplungen

import random


class Lostrommel:

    def ziehung():
        return random.sample(range(1,49), 6)

if __name__ == '__main__':
    l = Lostrommel
    print(l.ziehung())