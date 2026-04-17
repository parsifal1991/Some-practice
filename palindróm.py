
szöveg = input("Adja meg a vizsgálni kívánt szöveget: ")
def is_palindrome_sentence(s):
    javított_szöveg = ''.join(c for c in s.lower() if c.isalnum())
    
    return javított_szöveg == javított_szöveg [::-1]
print(is_palindrome_sentence(szöveg))