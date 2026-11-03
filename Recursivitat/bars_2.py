from yogi import read


n=read(int)


def bars_2(n:int)-> str:
    if n==1:
        print("*")
        return
    else:
        print(n*("*"))
        bars_2(n-1)
        bars_2(n-1)


def main()->None:
    bars_2(n)


if __name__=="__main__":
    main()