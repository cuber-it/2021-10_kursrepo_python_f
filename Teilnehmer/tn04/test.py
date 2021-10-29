# Lotto
import random
treffer, dreier, vierer, fünfer, x, y, z, a  = 0, 0, 0, 0, 0, 0, 0, []
print("Ziehe sechs Kugeln zwischen 1 und 49")
while y != 6:
    z = int(input("Zahl: "))
    if z in a or z < 1 or z > 49:
        print("Bitte eine Zahl zwischen 1 und 49 ohne Wiederholungen !!")
    else:
        a.append(z), a.sort()
        print ("Deine Wahl:", a)
        y += 1
while treffer != 6:
    x += 1
    b = (random.sample(range(1, 50), 6))
    c = [i for i in a if i in b]
    treffer = len(c)
    if treffer == 3:
        dreier += 1
    elif treffer == 4:
        vierer += 1
    elif treffer == 5:
        fünfer += 1
        print (dreier, "Dreier,", vierer, "Vierer und", fünfer, "Fünfer in", x, "Tipps")
    elif treffer == 6:
        print ("Die Ziehung brauchte", x, "Tipps bis zum Sechser,")
        print ("inkl.", fünfer, "Fünfer =", round(fünfer*100/x, 5), "% Chance,")
        print ("inkl.", vierer, "Vierer =", round(vierer*100/x, 5), "% Chance,")
        print ("inkl.", dreier, "Dreier =", round(dreier*100/x, 5), "% Chance.")