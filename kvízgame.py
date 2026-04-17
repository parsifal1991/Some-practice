import tkinter as tk
from tkinter import messagebox
import pygame
import random

# Pygame inicializálás a hangokhoz és zenelejátszáshoz





# Kérdések különböző témákban
questions_easy = [
    ("Melyik sportágban használják a legkisebb labdát?", ["A. Golf", "B. Tenisz", "C. Pingpong", "D. Biliárd"], "C"),
    ("Ki festette a Mona Lisát?", ["A. Van Gogh", "B. Leonardo da Vinci", "C. Michelangelo", "D. Picasso"], "B"),
    ("Melyik állat a sivatag királya?", ["A. Oroszlán", "B. Hiéna", "C. Kígyó", "D. Teve"], "D"),
    ("Hány csillag van az amerikai zászlón?", ["A. 48", "B. 50", "C. 52", "D. 45"], "B"),
    ("Mi a Föld legnagyobb kontinense?", ["A. Amerika", "B. Európa", "C. Ázsia", "D. Afrika"], "C"),
    ("Hány perc egy focimeccs normál játékideje?", ["A. 60", "B. 90", "C. 120", "D. 80"], "B"),
    ("Mi a víz kémiai jele?", ["A. CO2", "B. H2O", "C. O2", "D. NaCl"], "B"),
    ("Melyik bolygón található a Valles Marineris kanyon?", ["A. Vénusz", "B. Mars", "C. Merkúr", "D. Jupiter"], "B"),
    ("Mi a neve Harry Potter legjobb barátjának?", ["A. Draco Malfoy", "B. Ron Weasley", "C. Neville Longbottom", "D. Sirius Black"], "B"),
    ("Melyik állat a legnagyobb a világon?", ["A. Kék bálna", "B. Elefánt", "C. Medve", "D. Zsiráf"], "A")
]

questions_medium = [
    ("Milyen színű a rubin?", ["A. Zöld", "B. Kék", "C. Piros", "D. Sárga"], "C"),
    ("Ki volt az első ember a Holdon?", ["A. Buzz Aldrin", "B. Yuri Gagarin", "C. Neil Armstrong", "D. Alan Shepard"], "C"),
    ("Melyik évben történt a Titanic katasztrófája?", ["A. 1905", "B. 1912", "C. 1931", "D. 1898"], "B")
]

# Kérdésválasztás nehézségi szint alapján
questions = questions_easy  # Alapértelmezett nehézség: könnyű

current_question = 0
score = 0
guesses = []

def play_click():
    click_sound.play()

def check_answer(selected_option):
    global current_question, score
    play_click()
    guesses.append((questions[current_question][0], selected_option, questions[current_question][2]))
    
    if selected_option == questions[current_question][2]:
        score += 1
        messagebox.showinfo("Eredmény", "Helyes válasz! ✅")
    else:
        messagebox.showinfo("Eredmény", f"Rossz válasz! ❌ A helyes válasz: {questions[current_question][2]}")
    
    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        show_summary()

def show_summary():
    summary_text = "Eredmények:\n\n"
    for i, (question, user_answer, correct_answer) in enumerate(guesses):
        summary_text += f"{i+1}. {question}\n  - A te válaszod: {user_answer}\n  - Helyes válasz: {correct_answer}\n\n"
    percentage = (score / len(questions)) * 100
    summary_text += f"Pontszámod: {score}/{len(questions)} ({percentage:.2f}%)\n"
    messagebox.showinfo("Kvíz vége", summary_text)
    root.quit()

def load_question():
    question_label.config(text=questions[current_question][0])
    for i in range(4):
        buttons[i].config(text=questions[current_question][1][i], command=lambda opt=questions[current_question][1][i][0]: check_answer(opt))

def change_difficulty(level):
    global questions, current_question, score
    if level == "könnyű":
        questions = questions_easy
    elif level == "közepes":
        questions = questions_medium
    
    current_question = 0
    score = 0
    load_question()

def start_game():
    menu_frame.pack_forget()
    game_frame.pack()
    load_question()

# Tkinter ablak létrehozása
root = tk.Tk()
root.title("Kvíz Játék")
root.geometry("1000x700")
root.state("zoomed")
root.configure(bg="black")

menu_frame = tk.Frame(root, bg="black")
menu_frame.pack()

start_button = tk.Button(menu_frame, text="Új játék", font=("Comic Sans MS", 24, "bold"), bg="green", fg="white", command=start_game)
start_button.pack(pady=20)

difficulty_menu = tk.Menubutton(menu_frame, text="Nehézség", font=("Comic Sans MS", 20), relief=tk.RAISED, bg="blue", fg="white")
difficulty_menu.pack(pady=20)
menu = tk.Menu(difficulty_menu, tearoff=0)
menu.add_command(label="Könnyű", command=lambda: change_difficulty("könnyű"))
menu.add_command(label="Közepes", command=lambda: change_difficulty("közepes"))
difficulty_menu.config(menu=menu)

game_frame = tk.Frame(root, bg="black")

question_label = tk.Label(game_frame, text="", font=("Comic Sans MS", 24, "bold"), wraplength=800, bg="black", fg="white")
question_label.pack(pady=20)

buttons = []
for _ in range(4):
    btn = tk.Button(game_frame, text="", font=("Comic Sans MS", 18), width=50, bg="gray", fg="white")
    btn.pack(pady=10)
    buttons.append(btn)

root.mainloop()