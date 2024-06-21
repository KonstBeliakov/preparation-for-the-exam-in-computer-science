from turtle import *

tracer(0)
screensize(2000, 2000)

m = 40

for _ in range(14):
    for _ in range(3):
        fd(3 * m)
        rt(90)
    lt(180)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(3, 'red')
done()
