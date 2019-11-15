from turtle import *


shape('turtle')
speed(0)



def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)


def hexagon(sidelength=100):
    for i in range(6):
        forward(sidelength)
        right(60)


def polygon(sidelength=200):
        right(20)
        forward(sidelength)
        right(140)
        forward(sidelength)
        right(40)
        forward(sidelength)
        right(140)
        forward(sidelength)



for i in range(80):
    triangle()
    right(5)


for i in range(80):
    polygon()
    right(5)


for i in range(80):
    hexagon(200)
    right(5)

for i in range(80):
    square(400)
    right(5)


