import random

lehetőségek = ("kő", "papír", "olló")
játékos = None
számítógép = random.choice(lehetőségek)
running = True

while running:
    
    játékos = None
    számítógép = random.choice(lehetőségek)
    
    while játékos not in lehetőségek:
        játékos = input("Adja meg a választását(kő, papír, olló): ")

    print(f"Játékos: {játékos}")
    print(f"számítógép: {számítógép}")

    if játékos == számítógép:
        print("Döntetlen!")
    elif játékos == "olló" and számítógép == "papír":
        print("A játékos nyert!")
    elif játékos == "kő" and számítógép == "olló":
        print("A játékos nyert!")
    elif játékos == "papír" and számítógép == "kő":
        print("A játékos nyert!")
    else:
        print("A számítógép nyert!")
    if not input("Még egy menet? (y/n)").lower() == "y":
        running = False
print("Köszönöm a játékot!!")