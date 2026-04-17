penz = 10000

csoki = int(input("Hany csokit vasarol? "))
gumicukor = int(input("Hany gumicukrot vasarol? "))
keksz = int(input("Hany kekszet vasarol? "))
sutemeny = int(input("Hany doboz sutemenyt vasarol? "))
borravalo = int(input("Mennyi borravalot ad? "))

osszeg = csoki * 600 + gumicukor * 400 + keksz * 550 + sutemeny * 1200 + borravalo

if osszeg <= penz:
    marad = penz - osszeg
    print("Megmaradt:", marad, "Ft")
else:
    hitel = osszeg - penz
    print("Hitelre vasarolt:", hitel, "Ft ertekben")
