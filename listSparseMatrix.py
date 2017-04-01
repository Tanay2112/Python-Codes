l=[]
n=int(input("enter rows"))
m=int(input("enter columns"))
c=0
d=0
if n>0 and m>0:
    for i in range(0,n):
        l.append([])
    for i in range(0,n):
        for j in range(0,m):
            l[i].append(int(input()))
    for i in range(0,n):
        for j in range(0,m):
            if l[i][j]==0:
                c=c+1
            else:
                d=d+1
    if c>=d:
        print("sparse")
    else:
        print("non sparse")
else:
    print("invalid input")
