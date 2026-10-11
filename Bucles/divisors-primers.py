#programa que ens diu tots els divisors d'un número
import yogi
n=yogi.read(int)
i=1
while i * i <= n: #és el mateix que dir que i ha de ser més gran que arrel de n
 if n % i ==0:
  print(i)
 i= i+1
i=i-2
while i >= 1: 
 if n % i ==0:
  print(n // i)
 i= i-1
    