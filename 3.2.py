
rate = int(input())

print("Ft\tEuro")
for euro in range(1, 201, 25):
    forint = euro * rate
    print(f"{forint}\t{euro}")