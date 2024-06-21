from turtle import *

x = 30

t = Turtle()

screen = Screen()
screen.tracer(0)
screen.screensize(1500, 1500)



for i in range(4):
    for j in range(4):
        t.fd(6 * x)
        t.rt(90)
    t.fd(10 * x)
    t.rt(90)
    t.fd(3 * x)

t.up()
for i in range(-50, 50):
    for j in range(-50, 50):
        t.goto(i * x, j * x)
        t.dot(5)
        
