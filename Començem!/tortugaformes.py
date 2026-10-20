#l'entrada és una figura: cercle, rectangle o quadrat. 
# I depenent de la figura el radi(cercle), el costat (quadrat) i l'alçada i l'amplada (rectangle).
#Imprimeix la forma amb les mides introduides.
import turtle
import yogi
figura = yogi.read(str)
if figura == "cercle":
    radi = yogi.read(int)
    turtle.circle(radi)

if figura == "quadrat":
    costat=yogi.read(int)
    for i in range (4):
     turtle.forward(costat)
     turtle.left(90)

if  figura == "rectangle" :
    amplada = yogi.read(int)
    alçada = yogi.read(int)
    for i in range (2):
     turtle.forward(amplada)
     turtle.left(90)
     turtle.forward(alçada)
     turtle.left(90)

turtle.done()
