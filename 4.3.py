def jelek(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("+", end="")
        else:
            print("-", end="")

n = int(input("Adjon meg egy számot: "))
jelek(n)