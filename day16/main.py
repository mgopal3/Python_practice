# OOP
"""
Classes and objects.
"""
from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()

my_screen = Screen()


if __name__ == '__main__':

    print(timmy)
    timmy.shape("turtle")
    timmy.color("DarkGreen")
    timmy.forward(100)
    timmy.circle(100)

    print(my_screen.canvheight)
    print(my_screen.canvwidth)
    my_screen.exitonclick()
    
     # using prettyTable and creating an object
    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pokemon", "Squirtle", "Charmander"])
    table.add_column("acquired", [True, False, False])
    table.align = "r"
    print(table)









