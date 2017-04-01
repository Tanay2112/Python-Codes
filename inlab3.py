def gcdcal(x,y):
    gcd=0
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
t=()
n=int(input())
for i in range(n):
    t+=(int(input()),)
t=list(t)
for i in range(n):
    for j in range(1,n-1):
        if gcdcal(t[j],t[0])>gcdcal(t[j+1],t[0]):
            t[j],t[j+1]=t[j+1],t[j]
        if gcdcal(t[j],t[0])==gcdcal(t[j+1],t[0]) and t[j]>t[j+1]:
            t[j],t[j+1]=t[j+1],t[j]
print(t[0])
for i in t[1:]:
    print(i)
