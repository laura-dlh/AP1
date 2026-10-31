from yogi import scan, read

antes = -1
actual = -1
futuro = -1
contador = 0
resultado = 0
resultado_final = 0
resultado_actual = 0
resultado_antes = 0

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
            resultado_actual = 1 
            if resultado_antes == 1:
                resultado_final += 1
        # para la siguiente iteración
        antes = actual
        actual = futuro
        resultado_antes = resultado_actual
        resultado_actual = -1
        
    contador +=1

def main():
    n = read(int)
    for _ in range (n):
        print(resultado_final)

#solo hace falta verificar que xi-1>xi+1 porque xi-1 + xi > xi + xi+1 se tacha xi
# y si pones que cuando n=-1 return -1 directamente para asegurar