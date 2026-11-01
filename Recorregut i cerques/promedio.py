from yogi import tokens


def promedio()->int:
    resultado = 0
    resultadofinal = 0
    c = 0
    for n in tokens(float):
        resultado += n
        c += 1
    resultadofinal= resultado/c
    return f"{resultadofinal:.2f}"

def main():
    print(promedio())


if __name__ == "__main__":
    main()


