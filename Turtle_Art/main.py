## Extracting colors from an image
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('images.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed('fastest')
color_list = [(1, 9, 30), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

timmy.hideturtle()
timmy.setheading(225)
timmy.penup()
timmy.forward(300)
print(timmy.xcor())
timmy.setheading(0)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        if _ < 9:
            timmy.forward(50)

    y = timmy.ycor() + 50

    timmy.setposition(-212.13203435596424, y)










my_screen = Screen()
my_screen.exitonclick()
