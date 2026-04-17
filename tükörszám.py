
n = int(input("Adja meg a számot:"))

def is_mirrored(n):
    forditott = str(n)[::-1]
    if str(n) == forditott:
        return True
    else:
        return False
print(is_mirrored(n))