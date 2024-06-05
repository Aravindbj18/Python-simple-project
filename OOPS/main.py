# from turtle import Turtle,Screen
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("black")
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.left(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.left(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.left(90)
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
import turtle as t
import random
tim = t.Turtle()

colors = ["medium aquamarine","DarkOrchid", "IndianRed","DeepsSkyBlue","medium aquamarine","DarkOrchid", "IndianRed","DeepsSkyBlue","medium aquamarine","DarkOrchid", "IndianRed"]
def draw_shape(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
        













screen = Screen()
screen.exitonclick()