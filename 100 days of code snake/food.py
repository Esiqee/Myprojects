import turtle
from random import randint


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.66, stretch_len=0.66)
        self.color("green")
        self.speed("fastest")
        self.yummy()

    def yummy(self):
        self.goto(randint(-280, 280), randint(-280, 280))
