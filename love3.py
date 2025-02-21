import math
from turtle import *

def heart_a(n):
    return 15 * math.sin(n) ** 3

def heart_b(n):
    return 12 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)

speed(10)
bgcolor("black")
color('#f73487') #set color outside of loop
hideturtle() # hide turtle outside of loop.
for i in range(700):
    goto(heart_a(i) * 15, heart_b(i) * 15)

done()