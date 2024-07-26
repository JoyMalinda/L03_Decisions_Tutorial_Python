import turtle as t
from turtle import *


def t_triangle():
    t.forward(250)
    t.left(120)
    t.forward(250)
    t.left(120)
    t.forward(250)
    t.left(120)


def t_square():
    t.forward(250)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(250)
    t.right(90)


def turtle_shape():
    shape1 = input("Do you want a triangle or a square? ")
    shape2 = shape1.lower()

    if shape2 == "triangle":
        t_triangle()
    elif shape2 == "square":
        t_square()
    else:
        print("Invalid Input: Please enter 'triangle' or 'square'.")


turtle_shape()
