
questions = (("Mikor született a Beni: "),
           ("Mi a férjed kedvenc állata: "),
           ("Milyen programot szeretne készíteni a férjed: "),
           ("Mennyire szeret téged a férjed? 🫶🏻 "),
           ("Nézzünk ma még valamit szerinted: "))

options= (("A. 2024.10.28", "B. 2024.09.24 ", "C. 2025.01.02 ", "D. 1991.09.24 "),
          ("A. Cápa", "B. Farkas", "C. Kutya", "D. Ló"),
          ("A. Játék", "B. Üzleti", "C. Logisztikai", "D. Animációs"),
          ("A. Leírhatatlanul", "B. Picikit", "C. Nagyon-nagyon", "D. 200%"),
          ("A. Nem", "B. Lehetséges", "C. Igen", "D. De mit? :D"))


answers = ("A", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer! ")
    question_num +=1

print("----------")
print("---RESULT---")
print("----------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) *100)
print(f"Your score is: {score}%")