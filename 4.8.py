
megfejtes = 76

while True:
    try:
        szam = int(input())
        if szam < 1 or szam > 100:
            continue
    except ValueError:
        print("Ez nem egy ervenyes szam!")
        continue
    
    if szam > megfejtes:
        print("A keresett szam kisebb!")
    elif szam < megfejtes:
        print("A keresett szam nagyobb!")
        
    else:
        print("Gratulalok, eltalaltad a szamot!")
        break