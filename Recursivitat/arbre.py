import yogi
import turtle
d =yogi.read(int)
angle= yogi.read(int)

def arbre (n:int, a:float) -> None:
 if n == 1:
    turtle.left(90)
    turtle.forward(d)
    turtle.right(angle)
    turtle.forward(0.75*d)
    turtle.back(0.75*d)
    turtle.left(2*angle)
    turtle.forward(0.75*d)
    turtle.back(0.75*d)
    turtle.right(angle)
    turtle.back(d)
    turtle.done()

 