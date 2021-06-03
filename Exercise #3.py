tup=(123,151,234,561,777)
for i in tup:
    n=i
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    if(r==i):
        print(i)