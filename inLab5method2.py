s=input().lower()
l=s.split()
for i in range(len(l)):
        for j in range(len(l)-1):
                if l[j]>l[j+1]:
                        l[j],l[j+1]=l[j+1],l[j]
l.append("")
        ##a=[]
        ##for i in range(len(l)-1):
        ##	if l[i]!=l[i+1]:
        ##		a.append(l[i])
        ##for i in range(len(a)):
        ##	print(a[i],"\t",s.count(a[i]))
for i in range(len(l)-1):
        if l[i]!=l[i+1]:
              print(l[i],"\t",s.count(l[i]))
