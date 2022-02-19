# Event Listeners in Python

import random
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()


# Higher order function
# We can pass a function to a function to perform some activity
# calculator is a higher order func and can use other functions to do something


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def calculator(n1, n2, fun):
    return fun(n1, n2)


print(calculator(2, 3, add))
print(calculator(2, 3, multiply))


# Etch a sketch using the above concept of event listeners and higher order functions
# W=Forwards, S=Backwards A=Counter-clockwise D=Clockwise C= Clear Drawing and go back to center


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
