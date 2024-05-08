from turtle import Turtle, Screen

tim = Turtle()

num_sides = 5

for _ in range(num_sides):
    angle = 360 / num_sides
    tim.forward(100)
    tim.right(angle)
