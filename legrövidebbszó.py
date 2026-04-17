
mondat = input("Adja meg a mondatot:")

def shortest_word(mondat):
    szavak = mondat.split()
    legrövidebb = min(szavak,key=len)
    
    return legrövidebb
print(shortest_word(mondat))