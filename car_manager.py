from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y = random.randint(-250, 250)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for i in range(0, len(self.all_cars)-1):
            self.all_cars[i].forward(self.move_speed)

    def move_increment(self):
        self.move_speed += MOVE_INCREMENT
        self.move_cars()