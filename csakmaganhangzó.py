szó = input("Adja meg a vizsgálni kívánt szót: ")
javított_szó = szó.lower()

magánhangzók = "aáeéiíoóöőuúüű"

def only_vowels(szó):
    for betű in szó:
        if betű not in magánhangzók:
            return False
    return True

print(only_vowels(javított_szó))