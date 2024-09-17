from turtle import *
import colorsys 
bgcolor("black")
tracer(5)
pensize(2)
h= 0.001

for i in range (1200):
    c= colorsys.hsv_to_rgb(h,1,1)
    h+=0.008
    color(c)
    up()
    goto(-8,25)
    down()
    fd(i/2)
    rt(859)
    fillcolor("black")
    begin_fill()
    circle(18,320)
    end_fill()
    bk(i/4)
    fd(i)
    rt(30)
done()

