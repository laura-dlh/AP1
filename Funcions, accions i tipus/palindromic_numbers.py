from yogi import scan


def is_palindromic(n:int)->bool:
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        return True
    else:
        return False

def main():
    n=scan(int)
    while n is not None:
        print(is_palindromic(n))
        n = scan(int)

if __name__=="__main__":
    main()