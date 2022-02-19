# build a turtle race

from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1024, height=1024)
race_is_on = False
userBet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race?")
print(userBet)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
initial_pos = [-300, -200, -100, 0, 100, 200, 300]

players = []

for i in range(0,7):
    players.append(Turtle(shape="turtle"))
    players[i].speed("fastest")
    players[i].penup()
    players[i].fillcolor(colors[i])
    players[i].goto(-500, initial_pos[i])

race_is_on = True

while race_is_on:
    for player in players:
        if player.xcor() > 475:
            print(f"{player.fillcolor()} has Won the game!")
            race_is_on = False
            if userBet != player.fillcolor():
                print(f"Your bet was wildly off!")
            else:
                print(f"Your bet matches the actual win")
        player.forward(randint(0, 30))


screen.exitonclick()