nevek = []

while True:
    nev = input("Adj meg egy nevet (Enter a kilépéshez): ")
    if nev == "":
        break
    if nev not in nevek:
        nevek.append(nev)
    leghosszabb = max(nevek, key=len)

print(f"A leghosszabb név: {leghosszabb}")
for nev in nevek:
    print(nev)
