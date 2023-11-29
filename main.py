import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
score = Scoreboard()
FINISH_LINE_Y = (0, 280)

screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # Detect collision with car
    for i in range(0, len(cars.all_cars)-1):
        if player.distance(cars.all_cars[i]) < 20:
            score.game_over()
            game_is_on = False

    # Detect crossing finish line
    if player.distance(FINISH_LINE_Y) < 10:
        player.goto(x=0, y=-280)
        score.level_up()
        cars.move_increment()


screen.exitonclick()
