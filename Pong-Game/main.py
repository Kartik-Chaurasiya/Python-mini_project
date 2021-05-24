'''
STEPS:
    1. Create a Screen
    2. Create and move a paddle
    3. Create another paddle
    4. Create the ball and make it move
    5. Detect collision with the ball
    6. Detect collision with paddle
    7. Detect when paddle misses
    8. Keep Score
'''
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle((-350, 0)) 
paddle_r = Paddle((350, 0)) 
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up, 'Up')
screen.onkey(paddle_r.go_down, 'Down')
screen.onkey(paddle_l.go_up, 'w')
screen.onkey(paddle_l.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision with wall
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce_y()

    #collision with paqddle
    if (ball.distance(paddle_r) < 50) and (ball.xcor() > 320):
        ball.bounce_x()
    if (ball.distance(paddle_l) < 50) and (ball.xcor() < -320):
        ball.bounce_x()
    
    #check if ball miss()
    if (ball.xcor() > 380):
        ball.reset_pos()
        scoreboard.l_point()
    if (ball.xcor() < -380):
        ball.reset_pos()
        scoreboard.r_point()





screen.exitonclick()