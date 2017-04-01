##n=int(input("enter number of students"))
##if n>=0:
##    k=1
##    l=[]
##    for i in range(0,n):
##        l.append(input("Enter regitration number"))
##    r=input("enter registration number to be found")
##    for i in range(0,n-k):
##        for j in range(i+1,n-1-k):
##            if l[i]==l[j]:
##                l.pop(j)
##                k=k+1
##    for i in range(0,n-k):
##        print(l[i])
##    if l.index(r)!=-1:
##        print("Found")
##    else:
##        print("Not Found")
n=int(input('enter no of students: '))
name=[]
name1=[]
for i in range(0,n):
    name.append(input())
for i in range(0,n):
    """if name[i] in name1:
        continue
    else:
        name1.append(name[i])"""
    if name[i] not in name1:
        name1.append(name[i])
for i in range(0,len(name1)):
    name1[i]=name1[i].rstrip()
print(name1)
r=input()
if r in name1:
    print('Found')
else:
    print('Not found')
