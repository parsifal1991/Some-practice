matek = [5, 4, 3]
töri = [3, 5, 4]
info = [4, 5, 5]
tanulók = ['Anna', 'Béla', 'Csaba']

def combine_grades(matek, töri, info):
    eredmeny = []
    for nev, (m, t, i) in zip(tanulók, zip(matek, töri, info)):
        eredmeny.append((nev, m, t, i))
    return eredmeny

print(combine_grades(matek, töri, info))