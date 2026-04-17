
nevek = ["Anna", "Béla", "Csaba"]
pontok = [85, 92, 78]

def match_scores(nevek, pontok):
    eredmény = []
    for nev, pont in zip(nevek,pontok):
        eredmény.append((nev,pont))
    return eredmény

print(match_scores(nevek,pontok))