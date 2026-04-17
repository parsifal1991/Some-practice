
szo1 = input()
szo2 = input()

szo1_hossz = len(szo1)
szo2_hossz = len(szo2)

if szo1_hossz == szo2_hossz:
    print("A ket szo egyforma hosszu.")
elif szo1_hossz > szo2_hossz:
    különbség = szo1_hossz-szo2_hossz
    print(f"A ket szo kozul a {szo1} a hosszabb, {különbség} karakterrel.")
elif szo2_hossz > szo1_hossz:
    különbség = szo2_hossz-szo1_hossz
    print(f"A ket szo kozul a {szo2} a hosszabb, {különbség} karakterrel.")
    
