import yogi
a1 = yogi.read(int)
b1 = yogi.read(int)
a2 = yogi.read(int)
b2 = yogi.read(int)
c1=max(a1,a2)
c2=min(b1,b2)
if a1 == a2 and b1 == b2:
    print("= , " f"[{c1},{c2}]")
elif a2 <= a1 and b1 <= b2:
    print("1 , " f"[{c1},{c2}]")
elif a1 <= a2 and b2 <= b1:
    print("2 , " f"[{c1},{c2}]")
else:
   if c2<c1:print("? , " "[]")
   elif c1==c2: print("? , "f"[{c1},{c2}]")
   elif c2>c1:print("? , "f"[{c1},{c2}]")
