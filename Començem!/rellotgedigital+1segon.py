#programa que suma un segon a una hora de rellotge
import yogi
h=yogi.read(int)
m=yogi.read(int)
s=yogi.read(int)
#sumar un segon
s=s+1
if s==60:
    s = 0
    m = m+1
if m==60:
      m = 0
      h = h+1
if h==24:
        h=0
print(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))