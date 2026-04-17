name = input(" Please enter Your name: ")

if len(name) > 12:
    print(" The given name is to long! ")
elif not name.find(" ")==-1:
    print(" Your username cant contain spaces!")
elif not name.isalpha():
    print(" Your username cant contain digits!")
else:
    print(f"Welcome:{name}")