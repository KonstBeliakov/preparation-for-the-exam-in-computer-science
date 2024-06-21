from turtle import *

tracer(0)
screensize(2000, 2000)

m = 30

for _ in range(15):
    fd(7 * m)
    rt(30)
    fd(8 * m)
    rt(150)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(3, 'red')
done()
