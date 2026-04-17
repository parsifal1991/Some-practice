import math

# Bemenet bekérése
binaris = input("Kerek egy binaris szamot: ")

# Kiírás a bináris számra
print("Kerek egy binaris szamot:", binaris)

# Átalakítás decimálissá
decimalis = 0
hossz = len(binaris)

for i in range(hossz):
    bit = int(binaris[i])
    helyiertek = math.pow(2, hossz - 1 - i)
    decimalis += bit * helyiertek

# Eredmény kiírása
print("A decimalis ertek:", decimalis)