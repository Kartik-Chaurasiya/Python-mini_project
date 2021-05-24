from turtle import Turtle, Screen

new_t= Turtle()
screen = Screen()

def move_forward():
    new_t.forward(10)
def move_backward():
    new_t.backward(10)
def turn_left():
    new_heading = new_t.heading() + 10
    new_t.setheading(new_heading)
def turn_right():
    new_heading = new_t.heading() - 10
    new_t.setheading(new_heading)
def clear():
    new_t.clear()
    new_t.penup()
    new_t.home()
    new_t.pendown()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()