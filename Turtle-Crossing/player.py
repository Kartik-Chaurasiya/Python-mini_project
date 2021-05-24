from turtle import Turtle

POSITION = (0, -280)
MOVE_SPEED = 10
FINISH_LINE = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_SPEED)
    
    def goto_start(self):
        self.goto(POSITION)

    #win situation
    def is_at_finish(self):
        return self.ycor() > FINISH_LINE
