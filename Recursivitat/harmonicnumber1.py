"""
La entrada consiste en un número natural (norte). 
La salida imprime Hnorte con 4 dígitos después del punto decimal.
Donde Hnorte es el norte-ésimo número armónico, es decir
H norte= 1/1 + 1/2 ...+1/norte.

"""
import yogi
norte=yogi.read(int)
Hnorte=0


while norte >= 1:
    Hnorte=(1/norte)+ Hnorte
    norte= norte-1
print (f"{Hnorte:.4f}")


