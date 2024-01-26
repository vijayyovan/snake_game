import turtle
from turtle import Screen, Turtle
from Snakemove import Snakemove
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snakemove()

####
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
# screen.onkey(snake.left,"left")
screen.onkey(snake.right,"Right")

# all_turtles = []
#
# for position in x_positions:
#     snake = Turtle(shape="square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(position)
#     all_turtles.append(snake)
#
    # snake.pendown()
    # all_turtles.append(snake)

# screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# snake detects food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()

screen.exitonclick()
    # for seg in all_turtles:
    #     seg.forward(20)


    # for seg_num in range(len(all_turtles) -1, 0, -1):
    #     new_x = all_turtles[seg_num -1].xcor()
    #     new_y = all_turtles[seg_num -1].xcor()
    #     all_turtles[seg_num].goto(new_x,new_y)
    # all_turtles[0].forward(20)
    # all_turtles[0].left(90)



