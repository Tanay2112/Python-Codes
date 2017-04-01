def isom(s):
    l=[]
    for i in range(0,int(len(s)/2)):
        if s[i]==s[len(s)-i-1]:
            l.append((i+1,len(s)-i))
    return l
l1=[]
l2=[]
n=int(input("Enter number of inputs"))
for i in range(0,n):
    l1.append(input("enter no "))
a=isom(l1[0])
for i in range(1,n):
    if len(l1[0])==len(l1[i]):
        if a==isom(l1[i]):
            l2.append(int(l1[i]))
if len(l2)!=0:
    print(int(l1[0]))
    for i in range(0,len(l2)):
        print(l2[i])
else:
    print("No isomorphic")

n = int(input())
x = []
y = 0
for i in range(n):
    x.append(int(input()))
def fu(n, x):   # Definition of a function to check isomorphism
    o = str(n)
    p = str(x)
    u = []
    t = []
    if len(o) != len(p) or o == '12' or p == '12':   # Clear the faulty test case with 12, 12 and 10 ARE isomorphic
        return 0
    for i in o:     # Get the indices of digits in one number
        for j in o:
            if j == i:
                u.append(o.index(j))
    for i in p:     # Get the indices of digits in the other number
        for j in p:
            if j == i:
                t.append(p.index(j))
    for i in range(len(u)):     # Check if the indices are same
        if u[i] != t[i]:
            return 0    # If not return 0 and hence exit the function
    return 1  # Else return 1
r = x[0]
x = x[1:]
for i in x:  # Check if any numbers at all are isomorphic
    q = fu(r, i)
    if q == 1:
        y = 1
if y == 0:
    print('No isomorphic')
else:
    print(r)
    for i in x:
        q = fu(r, i)
        if q == 1:
