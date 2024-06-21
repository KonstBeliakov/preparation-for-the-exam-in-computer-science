from turtle import *

screen = Screen()
screen.tracer(0)
t = Turtle()

x = 10

for i in range(4):
    t.fd(10 * x)
    t.rt(270)
t.up()

t.fd(3 * x)
t.rt(270)
t.fd(5 * x)
t.rt(90)

t.down()

for i in range(2):
    t.fd(10 * x)
    t.rt(270)
    t.fd(12 * x)
    t.rt(270)

t.up()
for i in range(-50, 50):
    for j in range(-50, 50):
        t.goto(i * x, j * x)
        t.dot(2)
