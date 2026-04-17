
a = int(input(""))
b = int(input(""))

oszto = min(a, b)

while True:
    if a % oszto == 0 and b % oszto == 0:
        print("A legnagyobb közös osztó:", oszto)
        break
    oszto -= 1