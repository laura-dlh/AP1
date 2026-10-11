import yogi
n=yogi.read(int)
h=n//3600
s=n%3600
m=s//60
s=s%60
print(h,m,s)
