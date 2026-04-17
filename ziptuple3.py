
adatok = [("Anna", 85), ("Béla", 92), ("Csaba", 78)]

def separate_data(adatok):
    nevek, pontok = zip(*adatok)
    return list(nevek), list(pontok)
print(separate_data(adatok))