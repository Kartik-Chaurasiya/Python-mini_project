'''
STEPS: 
    1. move the turtle with keypress
    2. create and move the cars
    3. Detect collision with car
    4. Detect when turtle reaches the other side
    5. create a scoreboard
'''

from turtle import Screen
import time
from car import Car
from player import Player
from scoreboard import Scoreboard 

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, 'Up')
car = Car()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    #check collision with cars
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        player.goto_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()