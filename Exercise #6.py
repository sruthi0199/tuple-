s1=input("ENTER A STRING:")
lis=[]
new=[]
for i in s1:
    lis.append(i)
tup=tuple(lis)
new=[i for i in tup if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'or i=='E' or i=='I' or i=='O' or i=='U')]
print(new)