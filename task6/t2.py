from turtle import *

tracer(0)
screensize(2000, 2000)

m = 30
setpos(0, 0)
setpos(1000, 0)
setpos(0, 0)
setpos(0, 1000)
setpos(0, 0)

lt(90)
for _ in range(15):
    fd(3 * m)
    rt(40)




up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(3, 'red')
done()