from turtle import *

tracer(0)
screensize(2000, 2000)

m = 50

fd(9 * m)
rt(90)

for _ in range(2):
    fd(3 * m)
    rt(90)
    fd(3 * m)
    rt(270)

for _ in range(2):
    fd(3 * m)
    rt(90)

fd(9 * m)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(3, 'red')
done()