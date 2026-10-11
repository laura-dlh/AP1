# l'entrada és un nombre
# retorna la suma de tots els seus divisors
import yogi
n = yogi.read(int)

def sum_divisors (n:int) -> int:
  a = 1
  suma = 0
  while a * a <= n:
    if n%a == 0:
     suma = suma + a
     if a != (n//a):
       suma = suma + (n//a)
    a = a+1
  return suma
print(sum_divisors(n))
