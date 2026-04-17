
nevek = ["Anna", "Béla", "Csaba"]
jelenletek = [
    [True, True, False, True],
    [True, False, False, False],
    [True, True, True, True]
]

def vizsgara_bocsathatok(nevek, jelenletek):
    hianyzasok = {}
    bocsathatok = []

    for nev, jelenlet in zip(nevek, jelenletek):
        hianyzas = jelenlet.count(False)
        hianyzasok[nev] = hianyzas

        if hianyzas <= 1:
            bocsathatok.append(nev)

    print("Vizsgára bocsáthatók:", ", ".join(bocsathatok))
    return hianyzasok

print(vizsgara_bocsathatok(nevek, jelenletek))
                
