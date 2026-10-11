import yogi
n=yogi.read(int)
p=2

while p * p <= n:
    while n % p == 0:
        print(p)
        n = n // p
    p = p + 1

if n > 1:
    print(n)

