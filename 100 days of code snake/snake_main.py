import time
import turtle
from snake import Snake
from food import Food

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snakeeeeeeee")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = turtle.Turtle()

screen.onkey(snake.w, "w")
screen.onkey(snake.a, "a")
screen.onkey(snake.d, "d")
screen.onkey(snake.s, "s")

score = 0
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.color("white")
scoreboard.penup()
scoreboard.write(f"Score : {score}", move=False, align='center', font=('Arial', 25, 'normal'))

gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # snake eats food
    if snake.body[0].distance(food) < 14:
        print("Yummy")
        food.yummy()
        snake.grow()
        score += 1
        scoreboard.clear()
        scoreboard.write(f"Score : {score}", move=False, align='center', font=('Arial', 25, 'normal'))

    # snake collides with wall
    if (snake.body[0].xcor() > 285 or snake.body[0].xcor() < -285
            or snake.body[0].ycor() > 285 or snake.body[0].ycor() < -285):
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER!", move=False, align='center', font=('Arial', 25, 'normal'))
        gameon = False


    # snake collides with self
    for part in snake.body[1:]:
        if snake.body[0].distance(part) < 10:
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER!", move=False, align='center', font=('Arial', 25, 'normal'))
            gameon = False

screen.exitonclick()

