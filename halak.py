halak = {}
for _ in range(5):
    fajta = input("Add meg a hal fajtáját: ")
    while True:
        try:
            meret = float(input("Add meg a hal méretét (cm): "))
            break
        except ValueError:
            print("Hibás adat! Kérlek adj meg egy számot (pl. 5 vagy 5.0)")
    halak[fajta] = meret

# Méret szerinti szűrés
while True:
    try:
        meret_hatar = float(input("Add meg a méretet, ami alatti halakat keresel: "))
        break
    except ValueError:
        print("Hibás adat! Kérlek számot adj meg.")

print("Kisebb halak:")
for fajta, meret in halak.items():
    if meret < meret_hatar:
        print(f"Fajta: {fajta} Méret: {meret} cm")

# Hal fajta keresés
keresett_fajta = input("Melyik hal fajtát keresed? ")
if keresett_fajta in halak:
    print(f"Hal fajtája: {keresett_fajta} megtalálható az akváriumban!")
else:
    print(f"Hal fajtája: {keresett_fajta} nincs az akváriumban.")