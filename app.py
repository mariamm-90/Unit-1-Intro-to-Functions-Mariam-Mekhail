import turtle
from turtle import *
t = Turtle()
t.speed(10)


#turtle straight line
t.shape('turtle')
t.forward(200)


#function that sends message
def message(input):
    print(input)
message("Hello Class")


#function that makes turtle draw square
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)


#function that makes equilateral triangle
def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) 


#function that makes right triangle
def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()


#function that draws 1 rectangle with a width of 100px and a length of 125px
def rectangle(x):
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
rectangle(200)


#function that draws 1 triangle with 3 equal sides length 90
def equal(x):
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal(200)

turtle.done ()