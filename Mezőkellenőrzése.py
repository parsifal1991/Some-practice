word =input("Adja meg jelszavát:")
def vampire_password(word):
    if len(word) < 6:
        return False

    if word[-1] == "!":
        return False

    if "a" in word:
        return False

    has_v = False
    for karakter in word:
        if karakter == "v" or karakter == "V":
            has_v = True

    if not has_v:
        return False

    return True
print(vampire_password(word))