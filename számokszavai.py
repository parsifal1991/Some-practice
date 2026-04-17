szöveg = input("Adja meg a vizsgálni kívánt szöveget: ")

def count_digits_and_letters(szöveg):
    számjegyek = []
    betűk = []

    for c in szöveg:
        if c.isdigit():
            számjegyek.append(c)
        elif c.isalpha():
            betűk.append(c)

    return (len(betűk), len(számjegyek))

print(count_digits_and_letters(szöveg))