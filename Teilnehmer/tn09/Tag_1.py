
import sys

# Tabelle erstellen

def build_tabel():
    haeder = ["  "]
    for col in range(0,10):
        haeder.append(str(col))
    table = [haeder]
    for i in range(30,130,10):
        row = [str(i)]
        for j in range(0,10):
            c = chr(i+j)
            if c.isprintable():
                row.append(c)
            else:
                row.append(".")    
        table.append(row)
    return table

# Tabelle ausgeben

def print_table(table):
     print("|".join(table[0]))
     for row in table[1:]:
         print(f"{row[0]}|{' '.join(row[1:])}")

if __name__=="__main__":
    table = build_tabel()
    print_table(table)
    sys.exit(0)


