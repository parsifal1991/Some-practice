számok_listája = []

# 5 szám bekérése a felhasználótól
while len(számok_listája) < 5:
    számok = int(input("Adja meg a vizsgálni kívánt számokat: "))
    számok_listája.append(számok)

# Függvény: visszaadja a legnagyobb és legkisebb közti különbséget
def max_difference(nums):
    legkisebb = nums[0]
    legnagyobb = nums[0]

    for szam in nums:
        if szam < legkisebb:
            legkisebb = szam
        elif szam > legnagyobb:
            legnagyobb = szam

    return legnagyobb - legkisebb

# Kiírás
print("A legnagyobb különbség:", max_difference(számok_listája))