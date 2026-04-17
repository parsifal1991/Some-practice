import random

számok = []
kategori0_20 = []
kategori21_40 = []
kategori41_60 = []
kategori61_80 = []
kategori81_100 = []

# 20 darab véletlenszám generálása
while len(számok) < 20:
    szám = random.randint(1, 100)
    számok.append(szám)

# Számok kategorizálása
for szám in számok:
    if 0 <= szám <= 20:
        kategori0_20.append(szám)
    elif 21 <= szám <= 40:
        kategori21_40.append(szám)
    elif 41 <= szám <= 60:
        kategori41_60.append(szám)
    elif 61 <= szám <= 80:
        kategori61_80.append(szám)
    elif 81 <= szám <= 100:
        kategori81_100.append(szám)

# Átlag számítás
átlag = sum(számok) / len(számok)

# Kategória méretek összehasonlítása
kategóriák = {
    "0-20": len(kategori0_20),
    "21-40": len(kategori21_40),
    "41-60": len(kategori41_60),
    "61-80": len(kategori61_80),
    "81-100": len(kategori81_100)
}

legtöbb = max(kategóriák, key=kategóriák.get)

# Eredmények kiírása
print("Generált számok:", számok)
print("Átlag:", round(átlag, 2))
print("0-20:", kategori0_20)
print("21-40:", kategori21_40)
print("41-60:", kategori41_60)
print("61-80:", kategori61_80)
print("81-100:", kategori81_100)
print("Legtöbb szám a(z)", legtöbb, "kategóriában van.")