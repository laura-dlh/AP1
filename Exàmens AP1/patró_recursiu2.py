from yogi import scan

lletra=scan(str)
n_lletra=ord(lletra)

def patró_recursiu():
    if n_lletra== 1:
        return "a"
    else:
        print(lletra)
        (n_lletra-1)*(patró_recursiu(n_lletra-1))

def main():
    print(patró_recursiu())

if __name__=="__main__":
    main()