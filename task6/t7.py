from turtle import *

tracer(0)
screensize(2000, 2000)

m = 30

rt(315)
for _ in range(7):
    fd(16 * m)
    rt(45)
    fd(8 * m)
    rt(135)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(3, 'red')
done()