tup=(10,'sachin',False,67.23,20,20,'bunny','gautham',True)
lis=[]
print("Length of tuple:",len(tup))
print("Count of item in tuple:",tup.count(20))
print("Index of item:",tup.index('sachin'))
print("FIRST FIVE ITEMS IN TUPLE:")
for i in range(0,5):
    print(tup[i],end=" ")
print(" ")
print("TUPLE REVERSE:")
for i in range(len(tup)-1,0,-1):
    print(tup[i],end=" ")
print(" ")
lis=list(tup)
lis.append('gambhir')
tup=tuple(lis)
print("After appending an item:",tup)
print("String items in tuple:")
for i in tup:
    if(type(i)==str):
        print(i,end=" ")