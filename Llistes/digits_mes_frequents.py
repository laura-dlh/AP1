from yogi import read, tokens
resultat = -1
descomposicio = -1
contador_de0=-1
contador_de1=-1
contador_de2=-1
contador_de3=-1
contador_de4=-1
contador_de5=-1
contador_de6=-1
contador_de7=-1
contador_de8=-1
contador_de9=-1
contadors= [contador_de0, contador_de1, contador_de2, contador_de3, contador_de4, contador_de5, contador_de6,contador_de7, contador_de8, contador_de9]
major = contadors[0]
posicio = 0

def nombre_en_basex():
    b = read(str)
    for n in tokens():
        while n != 0:
            resultat = n%b
            if resultat == 0:
                descomposicio = n//b
                if descomposicio == 0:
                    contador_de0 += 1
                if descomposicio == 1:
                    contador_de1 += 1
                if descomposicio == 2:
                    contador_de2 += 1
                if descomposicio == 3:
                    contador_de3 += 1
                if descomposicio == 4:
                    contador_de4 += 1
                if descomposicio == 5:
                    contador_de5 += 1
                if descomposicio == 6:
                    contador_de6 += 1
                if descomposicio == 7:
                    contador_de7 += 1
                if descomposicio == 8:
                    contador_de8 += 1
                if descomposicio == 9:
                    contador_de9 += 1

def major_contador ():
    for i in range (10) :
        if contadors[i] > major:
            major = contadors[i]
            posicio = i 
    return (posicio, major)

def main():
    print (nombre_en_basex())
    print(major_contador())

if __name__ == "__main__":
    main()

