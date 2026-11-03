from yogi import scan


def number_of_digits(n:int)->int:
    resultado=0
    if n==0:
        return 1
    else:
        while n!=0:
            n = n//10
            resultado += 1
    return resultado


def main()->None:
    n = scan(int)
    while n is not None:
        print(number_of_digits(n))
        n=scan(int)

if __name__=="__main__":
    main()

