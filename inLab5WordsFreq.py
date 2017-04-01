s=input().lower().rstrip()
l=s.split()
##for i in range(len(l)):
##        for j in range(len(l)-1):
##                if l[j]>l[j+1]:
##                        l[j],l[j+1]=l[j+1],l[j]
##l.append("")
##for i in range(len(l)-1):
##        if l[i]!=l[i+1]:
##              print(l[i],"\t",s.count(l[i]))
s1=sorted(set(l))
for i in s1:
        print(i,"\t",s.count(i))
