import turtle
from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

class Snakemove:

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            snake_model = Turtle(shape="square")
            snake_model.color("white")
            snake_model.penup()
            snake_model.goto(position)
            self.all_turtles.append(snake_model)

    def move(self):
        for seg_num in range(len(self.all_turtles) -1, 0, -1):
            new_x = self.all_turtles[seg_num -1].xcor()
            new_y = self.all_turtles[seg_num -1].xcor()
            self.all_turtles[seg_num].goto(new_x,new_y)
        self.all_turtles[0].forward(20)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)







