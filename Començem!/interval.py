import yogi
a1=yogi.read(int)
a2=yogi.read(int)
b1=yogi.read(int)
b2=yogi.read(int)
c1=max(a1,b1)
c2=min(a2,b2)
if c2<c1: print("[]")
else:
    print(f"[{c1},{c2}]")


