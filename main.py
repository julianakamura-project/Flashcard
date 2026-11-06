from tkinter import *
import pandas as pd
from random import *
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}
to_learn = {}

#--CSV FILE

##Check for progress
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#--FLASHCARD

##Card selector

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = choice(to_learn)

    card_canvas.itemconfig(flashcard, image=card_front)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=f"{current_card["French"]}", fill="black")
    flip_timer = window.after(3000, card_flip)

##Card Flip
def card_flip():
    global current_card

    card_canvas.itemconfig(flashcard, image=card_back)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=f"{current_card["English"]}", fill="white")

#Known card
def learned():
    global flip_timer, wrong_button, right_button

    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    if len(to_learn) == 0:
        card_canvas.itemconfig(flashcard, image=card_front)
        card_canvas.itemconfig(card_title, text="", fill="black")
        card_canvas.itemconfig(card_word, text="All words learned!", fill="black")
        window.after_cancel(flip_timer)

        wrong_button.grid_forget()
        right_button.grid_forget()
        close_button = Button(window, text="Exit", command=window.destroy, width=50)
        close_button.grid(column=0, row=1, columnspan=2)

    else:
        next_card()


#--UI SETUP

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

##Images
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

##Flashcard
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard = card_canvas.create_image(400, 263, image=card_front)
card_canvas.grid(column=0, row=0, columnspan=2)
card_title = card_canvas.create_text(400, 100, text=f"Flashy Flashcards", fill="black", font=LANGUAGE_FONT)
card_word = card_canvas.create_text(400, 263, text=f"French/English\nFlashcards", fill="black", font=WORD_FONT, justify="center")

##Buttons
wrong_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=wrong_img, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=right_img, command=learned)
right_button.grid(column=1, row=1)

flip_timer = window.after(1500, next_card)




window.mainloop()