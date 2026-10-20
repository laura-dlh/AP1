import yogi

# cas base= un digit
def product_of_digits(n:int) -> int:
    if n<10:
        return n
    else:
        resultado=n%10
        n = n//10
        return resultado*product_of_digits(n)

    
def baja_niveles(n:int) -> None:
    producto=product_of_digits(n)
    if producto<10:
        print(f"The product of the digits of {n} is {producto}.")
    else:
        print(f"The product of the digits of {n} is {producto}.")
        baja_niveles(producto)


def main() -> None:
    n = yogi.read(int)
    baja_niveles(n)
    print("-"*10)


if __name__ == "__main__":
    while True:
        main()
        

    

    

 
        
