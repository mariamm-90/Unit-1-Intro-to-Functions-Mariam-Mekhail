import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.forward(200)

def message(input):
    print(input)
message("Hello Class")

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



turtle.done ()