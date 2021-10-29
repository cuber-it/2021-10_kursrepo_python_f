#Aufgabe a:
asciidict = {}
for i in range(32,128):
    asciidict[str(i)] = chr(i)
print(asciidict)

#Aufgabe b:
asciidict={str(i):chr(i) for i in range(32,128)}
print(asciidict)