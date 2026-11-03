from yogi import read
import turtle


def dibuixar_quadrat(a:int):
    #dibuixar un quadrat
    for i in range(4):
        turtle.down()
        turtle.forward(a)
        turtle.left(90)
   

def subamenaça_fractal(cx:int, cy:int, n:int, d:int):
    #dibuixar els quadrats del voltant
    if n==0:
        return
    else:
        #quadrat esquerra a baix
        turtle.up()
        turtle.goto(cx-d/2, cy-d/2)
        turtle.down()
        dibuixar_quadrat(a=d/2)
        #quadrat dreta a baix
        turtle.up()
        turtle.goto(cx+d, cy-d/2)
        turtle.down()
        dibuixar_quadrat(a=d/2)
        #quadrat dreta a dalt
        turtle.up()
        turtle.goto(cx+d,cy+d)
        turtle.down()
        dibuixar_quadrat(a=d/2)
        subamenaça_fractal(cx-d/2, cy-d/2, n-1, d/2)
        subamenaça_fractal(cx+d, cy-d/2, n-1, d/2)
        subamenaça_fractal(cx+d, cy+d, n-1, d/2)

def amenaça_fractal(cx:int, cy:int, n:int, d:int):
    turtle.speed(0)
    if n==0:
        return
    else: 
        dibuixar_quadrat(d)
        subamenaça_fractal(cx, cy, n-1, d)
    turtle.done()

def main():
    n = read(int)
    d = read(int)
    cx=0
    cy=0
    a = 0
    amenaça_fractal(cx,cy,n,d)

if __name__=="__main__":
    main()
