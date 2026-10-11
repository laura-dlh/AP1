import yogi

def product_of_digits (n:int) -> None:
    nStr = str(n)
    product = 1

    for char in nStr:
        product *= int(char)
    print (f'The product of the digits of {n} is {product}.')
    if product // 10 != 0:
        product_of_digits(product)


def main() -> None:
    for entrada in yogi.tokens(int):
        product_of_digits (entrada)
        print ("----------")


if __name__ == "__main__":
    main()

 

    

 
        
