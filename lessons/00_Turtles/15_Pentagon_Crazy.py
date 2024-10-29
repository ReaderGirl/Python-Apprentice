"""
Pentagon Crazy

This program already works. Run it, then change it to make it draw a different pattern.
"""

import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600, startx=0, starty=0)

colors = ("white", "red", "grey", "maroon", "green" , "purple" , "yellow" , )

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)
myTurtle.width(10)

sides = 5
angle = 190 / sides

for i in range(360):
    if i == 300:
        myTurtle.width(10)
    if i == 400:
        myTurtle.width(10)
    myTurtle.pencolor(getNextColor(i))
    myTurtle.forward(i)
    myTurtle.right(angle + 1)

myTurtle.hideturtle()

turtle.done()
