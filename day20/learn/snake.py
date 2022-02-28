from turtle import Turtle, Screen
import time

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# Functionality of the snake
# Create a Snake Body.
# Move the snake.
# Control the snake.
# Detect collision with food.
# Create a score board.
# Detect collision with wall.
# Detect collision with itself


class Snake:

    def __init__(self):
        self.segments = []
        self.num_of_segments = 3
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(self.num_of_segments):
            segment = Turtle(shape="square")
            segment.fillcolor("white")
            segment.color("white")
            segment.penup()
            segment.setpos(STARTING_POS[i])
            self.segments.append(segment)

    def move(self):
        # this ensures to move all the segments but the first one to the segment in pos-1
        for seg_num in range(self.num_of_segments - 1, 0, -1):
            cur_segment = self.segments[seg_num]
            prev_segment = self.segments[seg_num - 1]
            prev_segment_pos = (prev_segment.xcor(), prev_segment.ycor())
            cur_segment.goto(prev_segment_pos)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
