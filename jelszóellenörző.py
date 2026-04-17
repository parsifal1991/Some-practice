password =input(" Adja meg a jelszavát: ")

def password_checker(password):
    special_chars = "!@#$%^&*()-_=+"
    
    if len(password) < 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for karakter in password:
        if karakter.islower():
            has_lower = True
        elif karakter.isupper():
            has_upper = True
        elif karakter.isdigit():
            has_digit = True
        elif karakter in special_chars:
            has_special = True

    if has_lower and has_upper and has_digit and has_special:
        return True
    else:
        return False
print(password_checker(password))