# snake game

from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# start positions to create the segments on the screen.
# the snake starts with 3 segments
my_snake = Snake()
screen.update()

screen.listen()
screen.onkey(fun=my_snake.move, key="space")
screen.onkey(fun=my_snake.up, key="Up")
screen.onkey(fun=my_snake.down, key="Down")
screen.onkey(fun=my_snake.left, key="Left")
screen.onkey(fun=my_snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    my_snake.move()

screen.exitonclick()


