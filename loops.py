import turtle
from turtle import *
t = Turtle()

""" for i in range(60):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(5) """

def square(length,angle):
    for _ in range (4):
        t.forward(length)
        t.right(angle)

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5)



turtle.done()