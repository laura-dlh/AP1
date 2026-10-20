"""
La entrada es un número (x) y los coeficientes de un polinomio,
donde p(x) = co*(x**0)+ c1*(x**1)... cn*(x**n).
La salida imprime el resultado de operar x en el polinomio con 
4 dígitos después de la coma. 

"""

import yogi
x = yogi.read(float)
resultado=0
potencia=0


for coeficiente in yogi.tokens(float):
    resultado = coeficiente* (x**potencia) +resultado
    potencia = potencia + 1
print(f"{resultado:.4f}")



