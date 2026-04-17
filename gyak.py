#def happy_birthday(név,kor):
#    print(f"Happy birthday to {név}!")
#    print(f"You are {kor} years old!")
#    print("Happy birthday to you!")
#    print()
    
#happy_birthday("Bro",10)
#happy_birthday("Steve",20)
#happy_birthday("Jho",30)

#def display_invoice(username, amount, due_date):
#    print(f"Hello {username}")
#    print(f"Your bill of ${amount:.2f} is due{due_date}")

#display_invoice("Csabi bácsi",42.51, "01/01")

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("bimbob","pereketina")

print(full_name)