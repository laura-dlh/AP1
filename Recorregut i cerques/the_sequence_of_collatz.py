from yogi import scan


def the_sequence_of_collatz(n:int)->int:
    contador = 0
    if n == 1:
        return 0
    while n!= 1:
        if n%2==0:
            n=n/2
            contador += 1
        else:
            n = 3*n + 1
            contador += 1
    return contador


def main():
    n = scan(int)
    while n is not None:
        print(the_sequence_of_collatz(n))
        n = scan(int)


if __name__=="__main__":
    while True:
        main()