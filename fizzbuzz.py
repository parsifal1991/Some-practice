n = int(input("Adja meg a vizsgálni kívánt számok felső határát: "))

# FizzBuzz függvény
def fizzbuzz(n):
    eredmeny = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            eredmeny.append("FizzBuzz")
        elif i % 3 == 0:
            eredmeny.append("Fizz")
        elif i % 5 == 0:
            eredmeny.append("Buzz")
        else:
            eredmeny.append(i)
    return eredmeny

# Eredmény kiírása
print(fizzbuzz(n))
    