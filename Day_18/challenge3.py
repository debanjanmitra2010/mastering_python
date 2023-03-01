from turtle import Turtle, Screen
import random

tim = Turtle()

########### Challenge 3 - Draw Shapes ########

colors = ["cornflower blue", "aquamarine", "gold", "dark red",
          "salmon", "indigo", "dark green", "gray", "olive drab", "olive"]


def draw_shapes(num_side):
    for _ in range(num_side):
        tim.forward(100)
        tim.right(360//num_side)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shapes(shape_side_n)


screen = Screen()
screen.exitonclick()