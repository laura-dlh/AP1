import yogi
n = yogi.read(int)
c = 1

for i in range (((2*n-1)//2)+1):
    print((n-1)*" " + c*"*")
    c = c +2
    n = n-1
c = c-2

while c > 1:
    c = c - 2
    print ((n+1)*" " + c*"*")
    n = n + 1