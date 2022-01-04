c = ['grey', 'yellow']
dist = 700

from turtle import *
hideturtle()
bgcolor('black')
speed(11)
while True:
    color(c[dist%2])
    forward(dist)
    left(90)
    dist = dist - 3
    