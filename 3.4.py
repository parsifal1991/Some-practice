
szam1= int(input())
szam2 = int(input())

szam = max(szam1, szam2)

while True:
    if szam % szam1 == 0 and szam % szam2 == 0:
        print("A legkisebb közös többszörös:", szam)
        break
    szam += 1