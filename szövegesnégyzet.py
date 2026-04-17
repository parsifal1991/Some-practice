n = int(input("Adja meg a darabszámot: "))
def draw_square(n):
    for sor in range(n):
        if sor == 0 or sor == n - 1:
            print("#" * n)
        else:
            print("#" + " " * (n - 2) + "#")
print(draw_square(n))