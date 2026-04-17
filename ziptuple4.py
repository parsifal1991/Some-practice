
nevek = ["Anna", "Béla", "Csaba"]
jegyek = [5, 4, 3]

def create_grade_dict(nevek, jegyek):
    for nev,jegy in nevek,jegyek:
        dict(zip(nevek,jegyek))