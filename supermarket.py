item1=[]
item2=[]
common=[]
n=int(input("enter number of items purchased by first customer"))
m=int(input("enter number of items purchased by second customer"))
print("Enter ",n," items of first customer")
for i in range(0,n):
    item1.append(input())
print("Enter ",m," items of second customer")
for i in range(0,m):
    item2.append(input())
for i in range(0,n):
    for j in range(0,m):
        if item1[i]==item2[j]:
            common.append(item1[i])
print("Common list")
for i in range(0,len(common)):
    print(common[i])
