
from yogi import read
n=read(int)

def bars(n:int):
    if n==1:
        print ("*")
        return
    else:
        bars(n-1)
        print (n*"*")
        bars(n-1)

def main():
    bars(n)

if __name__=="__main__":
    main()
