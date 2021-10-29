#!/usr/bin/env python3
#from random import *

import random

class lostrommel:
    def ziehung(self):
        self.lottozahlen_gewinner = random.sample(range(1,50), 6)
        self.lottozahlen_gewinner.sort()
        #print(lottozahlen_gewinner.sort())
        return self.lottozahlen_gewinner
    

if __name__ == "__main__":
    l = lostrommel()
    print(l.ziehung())
