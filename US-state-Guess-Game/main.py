'''pandas has 2 primary data structures:
    1. Series (a single column or 1-D)
    2. DataFrame (2-D)
'''

import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title = f"{len(guessed_states)}/50 Guess the state", prompt = "What's another state's name?").title()

    if answer == 'Exit':
        break

    if answer in data['state'].to_list():
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
    
missing_states = []
for x in data['state']:
    if x not in guessed_states:
        missing_states.append(x)
print(f"learn: {missing_states}")

turtle.mainloop()