#introdueixes un numero
#imprimeix quants digits te aquest numero
import yogi
n=yogi.read(int)
c=1
ninicial=n

while (n//10) >= 1: 
 n= n//10
 c= c+1

print("The number of digits of", ninicial, "is", str(c) + ".")