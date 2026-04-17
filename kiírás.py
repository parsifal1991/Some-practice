
n = int(input("Adja meg a mennyiséget: "))

def draw_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)
draw_pyramid(n)