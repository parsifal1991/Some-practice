
szöveg = input("Adja meg a vizsgálni kívánt szöveget:")

def char_frequency(szöveg):
    szótár = {}
    for betű in szöveg:
        if betű.isalpha():
            betű = betű.lower()
            if betű in szótár:
                szótár[betű] += 1
            else:
                szótár[betű] = 1
    return szótár
    return szótár
print(char_frequency(szöveg))