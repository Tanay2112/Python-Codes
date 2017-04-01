m=int(input("enter first number"))
n=int(input("enter first number"))
c=0
for i in range(1,m+1):
    if m%i==0:
        for j in range(1,n+1):
            if n%j==0:
                if i==j:
                    c=c+1
if c==1:
    print("coprime numbers")
