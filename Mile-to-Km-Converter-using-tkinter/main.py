# import tkinter_theory

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height = 100)
window.config(padx = 10, pady=10)

def calculate():
    mile = input.get()
    km = round(float(mile) * 1.609)
    text3.config(text=f"{km}")
    
input = Entry(width = 10)
input.grid(column = 2, row = 1)

text1 = Label(text = 'Miles')
text1.grid(column = 3, row = 1)

text2 = Label(text = 'is equal to')
text2.grid(column = 1, row = 2)

text3 = Label(text = '0')
text3.grid(column = 2, row = 2)

text4 = Label(text = 'Km')
text4.grid(column = 3, row = 2)

button = Button(text='Calculate', command = calculate)
button.grid(column = 2, row = 3)



window.mainloop()