import random
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.bgcolor("lightblue")

tim = Turtle()
tim.shape("turtle")
tim.color("red", "black")

def random_color():
    screen.colormode(255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tim.pencolor((r, g, b))


#draw a square
for _ in range(4):
    tim.forward(100)
    tim.right(90)

#draw a dashed line with a 10 paces gap for 50 times

for _ in range(50):
    tim.forward(10)
    if not tim.isdown():
        tim.pendown()
    else:
        tim.penup()

#draw a triangle, square, pentagon hexagon, heptagon, octagon, nonagon, decagon, one over the other
#each corner for each of the shapes in 360/num of sides

for num_sides in range(3,11):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

#or



def draw_shape(num_sides):
    angle = 360/num_sides
    screen.colormode(255)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    tim.pencolor((r,g,b))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for num_sides in range(3, 11):
    draw_shape(num_sides)


#Draw a random walk
angles_to_turn = [0,90,180,270]
dist = 2
tim.colormode(255)
tim.pensize(10)
tim.speed("fastest")

for _ in range(300):
    colour_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
    direction = random.choice(angles_to_turn)
    tim.pencolor(colour_tuple)
    tim.setheading(direction)
    tim.forward(30)


#circle

tim.speed("fastest")
num_of_circles = 50
angle = 360/num_of_circles
for _ in range(num_of_circles+1):
    random_color()
    tim.circle(100)
    tim.setheading(tim.heading() + angle)
screen.exitonclick()


"""
Different styles of importing

import turtle
tim = turtle.Turtle()

from turtle import Turtle
tim = Turtle()

from turtle import *
#This is a little confusing cause we don't knwo where it comes from.
#avoid this

Aliasing Modules
import Turtle as T
tim = t.Turtle()


Installing modules
import heros #this may be a module that is not a part of a python package
You can install the package from the internet




"""