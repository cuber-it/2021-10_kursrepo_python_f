#!/usr/bin/env python3
import random

class lostrommel():
    def ziehung(self):
        self.ziehung = random.sample(range(1, 50), 6)
        return self.ziehung

if __name__ == "__main__":
    l = lostrommel()
    print(l.ziehung())