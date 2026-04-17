roplabdajatekosok = set()
ifjusagi_jatekosok = []

for i in range(5):
    nev = input("Nev:")
    kor = int(input("Kor:"))
    roplabdajatekosok.add((nev, kor))
    if kor < 18:
        ifjusagi_jatekosok.append((nev, kor))  # lista, hogy megtartsa a sorrendet

for _ in ifjusagi_jatekosok:
    print("Nev: Kor:", end=" ")
print()
for nev, kor in ifjusagi_jatekosok:
    print(f"{nev}, {kor}", end=" ")