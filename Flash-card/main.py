'''
try: Something that might cause an Exception
except (type error): Do this if there was an Exception
.
.
except (type error).....
else: Do this if there were no Exceptions
finally: Do this no matter what happens

raise: (raise your own error)
'''
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient = 'recprds')
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(card_word, text = current_card['French'], fill = 'black')
    canvas.itemconfig(card_bg, image = card_front_img)
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = 'English', fill = 'white')
    canvas.itemconfig(card_word, text = current_card['English'], fill = 'white')
    canvas.itemconfig(card_bg, image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index = False)
    next_card()

window = Tk()
window.title('Flash Card')
window.config(padx = 50, pady = 50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(width = 800, height = 526)
card_front_img = PhotoImage(file = "images/card_front.png")
card_back_img = PhotoImage(file = "images/card_back.png")
card_bg = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400, 150,text = '', font=('Ariel', 48, 'italic'))
card_word = canvas.create_text(400, 263, text = "" , font=('Ariel', 60, 'bold'))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row = 0, column = 0, columnspan = 2)

cross_image = PhotoImage(file = 'images/wrong.png')
unknown_button = Button(image = cross_image, command = next_card)
unknown_button.grid(row = 1, column = 0)
unknown_button.config(bg = BACKGROUND_COLOR, highlightthickness = 0)

tick_image = PhotoImage(file = 'images/right.png')
know_button = Button(image = tick_image, command = is_known)
know_button.grid(row = 1, column = 1)
know_button.config(bg = BACKGROUND_COLOR, highlightthickness = 0)

next_card()

window.mainloop()