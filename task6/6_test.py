from turtle import *
tracer(0)

m = 50
screensize(2000, 2000)

lt(90)

for i in range(6):
    fd(6 * m)
    rt(60)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(5, 'red')
done()