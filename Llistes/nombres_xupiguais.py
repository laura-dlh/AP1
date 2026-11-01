from yogi import read
n = read(int)
b = read(int)
i = 0

def comprobar(n:int, b:int, i:int) -> int:
    if n == 0:
        return 1
    digito = n % b
    if i % 2 == 0:
        if digito < b//2:
            return 0
    else:
        if digito >= b//2:
            return 0

    return comprobar(n//b, b, i+1)


def es_xupiguai(n:int, b:int) -> int:
    if n == 0:
        return 0
    return comprobar(n, b, 0)

print(es_xupiguai(n,b))

            
        
    
   



