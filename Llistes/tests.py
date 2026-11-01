
from yogi import read, tokens


size = 10
contadors = [0] * size
resultat = -1


def lectura(llista:list):
    b = read(int)
    for n in tokens(int):
       nombre_en_basex(llista, n , b)


def nombre_en_basex(llista:list, n:int, b:int):
    if n == 0:
        return
    resultat = n % b
    llista[resultat] += 1
    nombre_en_basex(llista, n // b , b)  

def major_contador(llista:list) -> tuple[int]:
    major = 0
    posicio = 0
    for i in range (len(llista)) :
        if llista[i] > major:
            major = llista[i]
            posicio = i 
    return (posicio, major)


def main():
    lectura(contadors)
    a, b = major_contador(contadors)
    print(f"{a} és el nombre més repetit amb {b} repeticions")
   
    

if __name__ == "__main__":
    main()

