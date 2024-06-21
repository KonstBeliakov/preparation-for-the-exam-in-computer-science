from turtle import *

tracer(0)
screensize(2000, 2000)

m = 100

x1, y1 = 0, 0
for _ in range(10):
    x1 += 3
    y1 += 6
    setpos(x1 * m, y1 * m)
    x1 += 7
    y1 -= 2
    setpos(x1 * m, y1 * m)
    x1 -= 10
    y1 -= 4
    setpos(x1 * m, y1 * m)
    print(x1, y1)

up()
for x1 in range(-20, 20):
    for y1 in range(-20, 20):
        setpos(x1 * m, y1 * m)
        dot(6, 'red')
done()