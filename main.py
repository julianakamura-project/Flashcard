from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")


#--

#--UI SETUP

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

##Images
wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

##Front Flashcard
card_canvas_ft = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas_ft.create_image(400, 263, image=card_front)
card_canvas_ft.grid(column=0,row=0, columnspan=2)
card_canvas_ft.create_text(400, 100, text=f"French", fill="black", font=LANGUAGE_FONT)
card_canvas_ft.create_text(400, 263, text=f"Placeholder", fill="black", font=WORD_FONT)

##Buttons
wrong_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=wrong_img)
wrong_button.grid(column=0, row=1)
right_button = Button(bg= BACKGROUND_COLOR, highlightthickness=0,image=right_img)
right_button.grid(column=1, row=1)





window.mainloop()