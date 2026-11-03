from yogi import read


n = read(int)


def bars_3(n:int)->str:
    if n==1:
        print("*")
        return 
    else:
        bars_3(n-1)
        bars_3(n-1)
        print (n*"*")


def main()->None:
    bars_3(n)


if __name__=="__main__":
    main()
    
