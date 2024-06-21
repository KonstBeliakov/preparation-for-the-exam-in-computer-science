from turtle import *

tracer(0)
screensize(2000, 2000)

m = 10

for _ in range(100):
    fd(10 * m)
    rt(30)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(3, 'red')

done()