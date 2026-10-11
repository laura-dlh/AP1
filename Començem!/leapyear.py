import yogi
year= yogi.read(int)
if year%4==0 and year%100!=0: print("YES")
elif year%100==0 and (year//100)%4==0: print("YES") #lo mismo que leap_year%400==0:
else:
    print("NO")

"""
traspas implica que
year%4==0 and year%100!=0
or
year%4==0 and any%400==0
#traiem factor comú
year%4==0 and year%100!=0
               or
              year%400==0
finalment: traspas= (year%4==0) and (year%100!=0 or year%400==0)
if traspas:
 print("YES")
else:
 print ("NO")

"""
