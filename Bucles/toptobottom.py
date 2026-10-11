#l'entrada són 2 nombres enters
#imprimeix els nombres enters compresos entre l'interval dels 2 nombres en ordre decreixent
import yogi
n=yogi.read(int)
m=yogi.read(int)

if m >= n:
  for i in range(n,m):
    print(m)
    m = m-1


if n >= m: 
  for i in range(m,n):
   print(n)
   n = n-1
print(m)
