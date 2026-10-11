import yogi
a = yogi.read(int)
b = yogi.read(int)
c = yogi.read(int)
d = yogi.read(int)

def gcd (a:int, b:int) -> (int): 
   while b>0:
     a,b= b, a%b
   return a
def gcd4 (a:int, b:int, c:int, d:int) -> (int):
    return gcd(gcd(a,b), gcd(c,d))

print (gcd4(a,b,c,d)) 