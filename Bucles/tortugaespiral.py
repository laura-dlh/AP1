import turtle
import yogi
n=yogi.read(int)
m=yogi.read(int)
c=1
for _ in range (n):
    turtle.forward(c*m)
    turtle.left(90)
    turtle.forward(c*m)
    turtle.left(90)
    c=c+1
turtle.done()