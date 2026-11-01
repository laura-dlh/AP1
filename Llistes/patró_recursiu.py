import yogi
n = yogi.read(int)


def patró_recursiu(n:int):
        if n == 1:
            print("1")
            return
        patró_recursiu(n-1) 
        imprimir_especial2(n)
        patró_recursiu(n-1)

def imprimir_especial(n:int):
    frase= ""
     #bucle
    for i in range(n):
        frase += str(n) 
        if i == (n-1):
            pass 
        else:
            frase += " "
    print(frase)

def imprimir_especial2(n:int):
    for i in range(n):
        print(n,end="")
        if i == (n-1):
            print() 
        else:
            print(" ",end="")

def main():
    patró_recursiu(n)

if __name__=="__main__":
    main()

   