import turtle


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        offset = 0
        for i in range(3):
            square = turtle.Turtle("square")
            square.penup()
            square.color("white")
            square.goto(offset, 0)
            self.body.append(square)
            offset -= 20

    def grow(self):
        square = turtle.Turtle("square")
        square.penup()
        square.color("white")
        square.goto(self.body[-1].position())
        self.body.append(square)

    def move(self):
        for part_num in range(len(self.body) - 1, 0, -1):
            move_x = self.body[part_num - 1].xcor()
            move_y = self.body[part_num - 1].ycor()
            self.body[part_num].goto(move_x, move_y)
        self.body[0].forward(20)

    def d(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def a(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def w(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def s(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)
