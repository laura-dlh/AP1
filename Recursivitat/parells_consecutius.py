from yogi import scan

antes = -1
actual = -1
futuro = -1
contador = 0
resultado = 0


actual = scan(int)
while actual != -1: # 5 4 3 2 1

    if contador == 0:
        antes = actual
        #preparando la siguiente iteración
        actual = scan(int)
    else:
        # antes y actual=x
        #actual=x
        futuro = scan(int)
        if actual + futuro < antes + actual:
            resultado += 1  
        # para la siguiente iteración
        antes = actual
        actual = futuro
    contador += 1
print(resultado)