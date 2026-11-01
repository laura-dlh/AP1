"""
L’entrada és una base (b) entre 2 i 10 seguida de diversos naturals entre 0 i 10^9.
La sortida retorna el dígit més frequent i el nombre de vegades que apareix. 
En cas d’empat, tria el dígit més petit.
"""

from yogi import read, tokens


n = 10
contadors = [0] * n
resultat = -1


def nombre_en_basex(lista:list):
    b = read(int)
    for n in tokens(int):
        if n == 0:
            lista[0] += 1
        else:
            while n != 0:
                resultat = n % b   
                lista[resultat] += 1
                n = n // b


def major_contador(lista:list) -> tuple[int]:
    major = 0
    posicio = 0
    for i in range (len(lista)) :
        if lista[i] > major:
            major = lista[i]
            posicio = i 
    return (posicio, major)


def main():
    nombre_en_basex(contadors)
    a, b = major_contador(contadors)
    #print("a és el nombre més repetit amb b repeticions")
    print(a ,b)
    

if __name__ == "__main__":
    main()
