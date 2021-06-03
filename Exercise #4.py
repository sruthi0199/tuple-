tup=('sachin-0-12','kapil-100-100','dhoni-34-80')
lis=[]
ctr=0
lis=list(tup)
print("PERSONS WHO SCORED CENTURY IN BOTH MATCHES:")
for i in lis:
    lis1=[]
    lis1=i.split("-")
    run1=int(lis1[1])
    run2=int(lis1[2])
    if(run1>=100 and run2>=100):
        print(lis1[0])
    else:
        ctr=ctr+1
if(ctr==len(lis)):
    print("NO ONE SCORED CENTURY IN BOTH MATCHES")

