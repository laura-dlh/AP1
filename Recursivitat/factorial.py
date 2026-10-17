"""
Escriviu una funció recursiva que, donat un natural, retorni el seu factorial @n@!.
Interfície
Python	
factorial(n: int) -> int
Precondició
Es compleix 0≤n≤1000.
Observació
Només cal enviar el procediment demanat; el programa principal serà ignorat.

"""
import yogi


n=yogi.read(int)


def factorial (n:int) -> int:
    number=0
    if n==0:    
        number=1
        return number
    else: 
      number= n*factorial(n-1)
      return number
print(factorial(n))
