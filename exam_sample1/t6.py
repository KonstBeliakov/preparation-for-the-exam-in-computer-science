from turtle import *

tracer(0)
screensize(2000, 2000)

m = 50

for _ in range(4):
    fd(12 * m)
    rt(90)

for _ in range(5):
    fd(4 * m)
    rt(45)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(6,'red')
done()