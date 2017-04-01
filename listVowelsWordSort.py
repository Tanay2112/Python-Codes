l=[]
n=int(input("Enter the number of names"))
for i in range(0,n):
    print("Enter name ",i+1)
    l.append(input())
for i in range(0,n):
    for j in range(0,n-1):
        c=0
        for ch in l[j]:
            if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
                p=c
            c=c+1
        d=0
        for ch in l[j+1]:
            if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
                k=d
            d=d+1
        if p>k:
            t=l[j];
            l[j]=l[j+1]
            l[j+1]=t
for i in range(0,n):
    print(l[i])
