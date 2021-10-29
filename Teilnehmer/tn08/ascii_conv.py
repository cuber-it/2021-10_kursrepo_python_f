item=[]
for x in range(32,128):
    print(str(x) + " " + repr(chr(x)))

print("Dictionary (long) number:ascii")
d={}
for x in range(32,128):
    d[str(x)] = chr(x)
print(d)

print()
print("Dictionary (Comprehension) number:ascii")
d={}
d = {str(x):chr(x) for x in range(32,128)}
print(d)

print()
print("Dictionary (Comprehension) ascii:number")
d={}
d = {chr(x):str(x) for x in range(32,128)}
print(d)

print()
def cmp(x):
    if x > 100:
        return True
    else:
        return False

daten=[200,50,500,100]
true_liste = list(filter(cmp,daten))
print(true_liste)