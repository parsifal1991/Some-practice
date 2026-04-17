
username = str(input(" Adja meg a felhasználónevet: "))


def username_checker(username):
    if len(username) < 4:
        return False
    if username[0].isdigit():
        return False
    for karakter in username:
        if not (karakter.isalpha() or karakter.isdigit() or karakter == "_"):
            return False
    if username[-1] == "_":
        return False
    return True
print(username_checker(username))