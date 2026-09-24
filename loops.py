import turtle
from turtle import *
t = Turtle()
t.speed(0)


#defining square
def square(length,angle):
    for _ in range (4):
        t.forward(length)
        t.right(angle)


#function that draws 60 squares, turning right 5 degrees after each square
def drawSpiral ():
    for i in range(60):
        square (100,90)
        t.right(5)
drawSpiral()


#5 squares doubling in size each time
def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length,90)
        length += 25
addSquares(5)


#Star Flower
def star(length,angle):
    for i in range(4):
        for j in range(4):
            t.toward(length)
            t.right(5)

def starSpiral(iRange):
    length = 5
    for i in range(iRange):
        star(length,144)
        length += 5
starSpiral(60)


#function drawing 60 squares, turning 5 degrees after each square and making each successive square bigger
def drawSpiral():
    length = 5
    for i in range(60):
        square(length,90)
        t.right(5)
        length += 5
drawSpiral()


#defining star
def star(length):
    for _ in range(5):
        t.forward(length)
        t.right(144)

#function drawing a 5 pointed star using the angle 144
def starSpiral():
    length = 5
    for i in range(60):
        star(length)
        t.right(5)
        length += 5
starSpiral()


turtle.done()