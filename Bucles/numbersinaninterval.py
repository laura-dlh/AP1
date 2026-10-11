import yogi
a=yogi.read(int)
b=yogi.read(int)

if a > b:
 print("")

elif b >= a:
 while a < b:
    print(str(a), end = ",")
    a=a+1
 print(b)