n=int(input("enter the number of plants"))
ID=[]
height=[]
c=1
for i in range(0,n):
    print("enter ID for ",i+1)
    a=int(input())
    print("enter height for ",i+1)
    b=int(input())
    if a<=0 and b<=0:
        c=0
        print("invalid input")
        break
    ID.append(a)
    height.append(b)
if c==1:
    for i in range(0,n):
        for j in range(0,n-1):
            if height[j]>height[j+1]:
                t=height[j]
                height[j]=height[j+1]
                height[j+1]=t
                t=ID[j]
                ID[j]=ID[j+1]
                ID[j+1]=t
    print("ID in ascending order of height")
    for i in range(0,n):
        print(ID[i])
