s1=input("Enter comma-separated alphabets:")
lis=s1.split(",")
tup=tuple(lis)
print(tup)
print("SECOND METHOD")
lis1=[]
s2=input("Enter a string:")
for i in s2:
    lis1.append(i)
tup1=tuple(lis1)
print(tup1)
print("THIRD METHOD")
l1=[]
while(True):
    s2=input("Enter an alphabet:")
    if(s2.isalpha()):
        l1.append(s2)
        t1=tuple(l1)
    else:
        break
print(t1)




