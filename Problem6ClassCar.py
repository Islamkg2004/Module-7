# Islam Syndanbekov
# Date: November 4, 2026
# Problem 5: Draw squares using Python Turtle

import turtle


def drawSquare(t, sz):
    # Draw a square with sides of size sz
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

drawSquare(alex, 100)

wn.exitonclick()