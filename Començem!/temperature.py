import yogi
temperature=yogi.read(int)
if 30<temperature<100: print("it's hot")
elif temperature>=100: 
    print("it's hot")
    print("water would boil")
elif 0<temperature<10: print("it's cold")
elif temperature<=0: 
    print("it's cold")
    print("water would freeze")
else:
    print("it's ok")