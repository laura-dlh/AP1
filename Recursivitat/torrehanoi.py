

def hanoi (n:int, ori:str, dst:str, aux:str) -> None:
    if n>0:
        hanoi (n-1, ori , aux, dst)
        print (ori, "=>", dst)
        hanoi(n-1, aux, dst, ori)

def main () -> None:
    import yogi
    n= yogi.read(int)
    hanoi(n, "A", "C", "B")

if __name__ == "__main__":
    main()

