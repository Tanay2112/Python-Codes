first = []
second = []
total = []

n = int(input("enter the degree of the first equation "))
for i in range(0,n+1):
    print("enter the coeffiecient of x^",n-i)
    first.append(int(input()))

                 
m = int(input("enter the degree of the second equation "))
for i in range(0,m+1):
    print("enter the coeffiecient of x^",m-i)
    second.append(int(input()))

                  
if n>m:
    for i in range(0,n-m):
        second.insert(0,0)
elif m>n:
    for i in range(0,m-n):
        first.insert(0,0)
                  
for i in range(0,n+1):
    total.append(first[i]+second[i])
print(total)
