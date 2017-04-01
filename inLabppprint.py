from pprint import pprint
n=int(input())
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
mydict={}
amount=0
for i in range(0,n):
    l1.append(input())
    l2.append(int(input()))
    l3.append(int(input()))
m=int(input())
for i in range(0,m):
    l4.append(input())
    l5.append(int(input()))
for i in range(0,n):
    for j in range(0,m):
        if(l1[i]==l4[j]):
            if(l5[j]<=l2[i]):
                amount+=(l5[j]*l3[i])
                l2[i]=l2[i]-l5[j]
for i in range(0,n):
    l1[i]=l1[i].rstrip()
    mydict.update({l1[i]:[l2[i],l3[i]]})
print (amount)
pprint(mydict)      
