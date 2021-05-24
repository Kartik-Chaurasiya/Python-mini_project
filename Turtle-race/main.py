from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your BET!", prompt = "Which turtle will win the race? Enter the color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_cord = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for new_turtle in range(6):
    new_t1 = Turtle(shape = "turtle")
    new_t1.color(colors[new_turtle])
    new_t1.penup()
    new_t1.goto(x = -230, y = y_cord[new_turtle])
    all_turtles.append(new_t1)
    

if user_bet:
     is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"The winner is {winning_color}, You won the Race...")
            else:
                print(f"You Lose the winner is {winning_color.upper()}")
            is_race_on = False
        speed = random.randint(0, 10)
        turtle.forward(speed)


screen.exitonclick()