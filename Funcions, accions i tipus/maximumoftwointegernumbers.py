
import yogi
a= yogi.read(int)
b= yogi.read(int)

def max2(a:int, b:int) -> int:
    if a>=b:
      return a
    if b>a:
       return b

print(max2(a,b))

