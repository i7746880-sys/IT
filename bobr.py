#!/usr/bin/python3
import turtle
from math import pi, sin, cos
t = int(input())
turtle.shape('turtle')
for i in range(1000):
    l = i/10
    dx = t * l * cos(l)
    dy = t * l * sin(l)
    turtle.goto(dx, dy)
