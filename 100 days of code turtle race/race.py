import turtle
from random import randint


winner = 0
screen = turtle.Screen()
screen.listen()
screen.setup(1000, 350)
choice = screen.textinput(title="Who will win this race?",
                          prompt="Pick one: red / purple / blue / green / brown / black")


red = turtle.Turtle()
red.penup()
red.color('red')
red.shape("turtle")
red.goto(-490, -125)

purple = turtle.Turtle()
purple.penup()
purple.color('purple')
purple.shape("turtle")
purple.goto(-490, -75)

blue = turtle.Turtle()
blue.penup()
blue.color('blue')
blue.shape("turtle")
blue.goto(-490, -25)

green = turtle.Turtle()
green.penup()
green.color('green')
green.shape("turtle")
green.goto(-490, 25)

brown = turtle.Turtle()
brown.penup()
brown.color('brown')
brown.shape("turtle")
brown.goto(-490, 75)

black = turtle.Turtle()
black.penup()
black.color('black')
black.shape("turtle")
black.goto(-490, 125)

if choice:
    race = True

while race == True:
    red.forward(randint(1, 15))
    purple.forward(randint(1, 15))
    blue.forward(randint(1, 15))
    green.forward(randint(1, 15))
    brown.forward(randint(1, 15))
    black.forward(randint(1, 15))

    if red.xcor() > 470:
        winner = "red"
        break
    elif purple.xcor() > 470:
        winner = "purple"
        break
    elif blue.xcor() > 470:
        winner = "blue"
        break
    elif green.xcor() > 470:
        winner = "green"
        break
    elif brown.xcor() > 470:
        winner = "brown"
        break
    elif black.xcor() > 470:
        winner = "black"
        break

if winner == choice:
    print("You won your bet, congratulations!")
else:
    print(f"You lost, the winner was: {winner}")


screen.exitonclick()
