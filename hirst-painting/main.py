import turtle as t
import random

t.colormode(255)
new_t = t.Turtle()
new_t.speed('fastest')
new_t.penup()
new_t.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

new_t.setheading(225)
# new_t.penup()
new_t.forward(300)
# new_t.pendown()
new_t.setheading(0)
number_of_dots = 100

for x in range(1, number_of_dots + 1):
    new_t.dot(20, random.choice(color_list))
    # new_t.penup()
    new_t.forward(50)
    # new_t.pendown()

    if x%10 == 0:
        # new_t.penup()
        new_t.setheading(90)
        new_t.forward(50)
        new_t.setheading(180)
        new_t.forward(500)
        new_t.setheading(0)
        # new_t.pendown()

screen = t.Screen()
screen.exitonclick()