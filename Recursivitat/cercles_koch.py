"""
 L'entrada és un nivell (n) i el radi de la circumferència (d).
 La sortida és un cercle de koch. 
 És a dir que per cada nivell dibuixa una rodona central i quatre rodones al voltant; 
 dreta, esquerra, amunt i avall. 
 La rodona central de mida d i les rodones al voltant de mida d/2.
  
"""

import turtle
import yogi


#assumim que d es radi i que els cercles no intersequen
def sub_cercles_koch(cx:float, cy:float, n:int, d:float)-> None:
    if n == 0:
        pass
    else:
        #avall
        turtle.up()
        turtle.goto(cx+0,cy-d)
        turtle.down()
        turtle.circle(d/2)
        #adalt
        turtle.up()
        turtle.goto(cx+0,cy+2*d)
        turtle.down()
        turtle.circle(d/2)
        #esquerra
        turtle.up()
        turtle.goto(cx+(-3/2)*d,cy+d/2)
        turtle.down()
        turtle.circle(d/2)
        #dreta
        turtle.up()
        turtle.goto(cx+(3/2)*d,cy+d/2)
        turtle.down()
        turtle.circle(d/2)

        sub_cercles_koch(cx+0,cy+2*d,n-1,d/2)
        sub_cercles_koch(cx+0,cy-d,n-1,d/2)
        sub_cercles_koch(cx-3/2*d,cy+d/2,n-1,d/2)
        sub_cercles_koch(cx+3/2*d,cy+d/2,n-1,d/2)


def cercles_koch(cx:float, cy:float, n:int, d:float)->None:
    turtle.speed(0)
    if n==0:
        pass  
    else: #cx == cy == 0
        turtle.down()
        turtle.circle(d)
        sub_cercles_koch(cx,cy,n,d)
    turtle.done()


def main()-> None:
    n = yogi.read(float)
    d = yogi.read(float)
    cx=cy=0
    cercles_koch(cx,cy,n,d)
    


if __name__== "__main__":
    main()

